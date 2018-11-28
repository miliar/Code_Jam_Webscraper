#include <WTypes.h>
#include <stdlib.h>
#include <ctype.h>
#include "stdio.h"
#include "string.h"
#include <vector>
using namespace std;

enum {MAX_LINE = 1024};
char Line[MAX_LINE];

class Combine
{
public:
    bool IsCombine(char prev, char curr)
    {
        if ((prev == C_First) && (curr == C_Second))
            return true;

        if ((curr == C_First) && (prev == C_Second))
            return true;

        return false;
    }

    char C_First;
    char C_Second;
    char C_Combine;
};
typedef vector<Combine> CombinesArr;

class Oppose
{
public:
    bool IsOpposed(char A, char B)
    {
        if ((A == O_First) && (B == O_Second))
            return true;

        if ((B == O_First) && (A == O_Second))
            return true;

        return false;
    }

    char O_First;
    char O_Second;
};
typedef vector<Oppose> OpposeArr;

typedef vector<char> BaseElements;


int readNumLine(FILE* a_hInput)
{
    char* ret = fgets(Line, MAX_LINE, a_hInput);
    if (ret == NULL)
        return 0;

    int num; 
    sscanf_s(Line, "%d", &num);
    return num;
}

static char* next_token;
char* ReadNextToken()
{
    return strtok_s(NULL, " ", &next_token);
}

bool readCase(FILE* a_hInput, CombinesArr& a_combines, OpposeArr& a_opposes, BaseElements& a_baseE)
{
    char* ret = fgets(Line, MAX_LINE, a_hInput);
    if (ret == NULL)
        return false;

    char* token = strtok_s(Line, " ", &next_token);    
    int C = atoi(token);

    for (int i=0; i<C; i++)
    {
        token = ReadNextToken();
        if (strlen(token) != 3)
        {
            printf("combine token len should be 3");
            return false;
        }

        Combine newCombine;
        newCombine.C_First = token[0];
        newCombine.C_Second = token[1];
        newCombine.C_Combine = token[2];

        a_combines.push_back(newCombine);
    }

    token = ReadNextToken(); 
    int D = atoi(token);

    for (int i=0; i<D; i++)
    {
        token = ReadNextToken();
        if (strlen(token) != 2)
        {
            printf("oppose token len should be 2");
            return false;
        }

        Oppose newOppose;
        newOppose.O_First = token[0];
        newOppose.O_Second = token[1];

        a_opposes.push_back(newOppose);
    }

    // Read base elements
    token = ReadNextToken(); 
    int N = atoi(token);

    token = ReadNextToken(); 
    for (int i=0; i<N; i++)
        a_baseE.push_back(token[i]);

    return true;
}

bool IsEndCombine(CombinesArr& a_combines, char prev, char curr, char& a_new)
{
    for (UINT i=0; i<a_combines.size(); i++)
    {
        if (a_combines[i].IsCombine(prev, curr))
        {
            a_new = a_combines[i].C_Combine;
            return true;
        }
    }
    return false;
}

bool IsOpposed(OpposeArr& a_opposes, char A, char B)
{
    for (UINT i=0; i<a_opposes.size(); ++i)
    {
        if (a_opposes[i].IsOpposed(A, B))
            return true;
    }
    return false;
}

bool IsOpposed(OpposeArr& a_opposes, BaseElements& a_currList, char a_curr)
{
    for (UINT i=0; i<a_currList.size(); i++)
    {
        if (IsOpposed(a_opposes, a_currList[i], a_curr))
            return true;
    }
    return false;
}

BaseElements runCase(CombinesArr& a_combines, OpposeArr& a_opposes, BaseElements& a_baseE)
{
    char prev = ' ';
    BaseElements newElements;

    for (UINT i=0; i<a_baseE.size(); ++i)
    {
        char curr = a_baseE[i];

        char newCombine = ' ';
        if (IsEndCombine(a_combines, prev, curr, newCombine))
        {
            newElements.pop_back();
            newElements.push_back(newCombine);
            prev = newCombine;
        }
        else if (IsOpposed(a_opposes, newElements, curr))
        {
            newElements.clear();
            prev = ' ';
        }
        else
        {
            prev = curr;
            newElements.push_back(curr);
        }
    }

    return newElements;
}

void Run(char* a_inputFile)
{
    FILE* hInput;
    errno_t err = fopen_s(&hInput, a_inputFile, "r");
    if (err != 0)
        return;

    int T = readNumLine(hInput);  // num of cases

    for (int i=0; i < T; i++)
    {
        CombinesArr combineA;
        OpposeArr   opposeA;
        BaseElements baseE;

        bool fOk = readCase(hInput, combineA, opposeA, baseE);
        BaseElements output = runCase(combineA, opposeA, baseE);

        printf("Case #%d: [", i+1);

        for (UINT i=0; i<output.size(); ++i)
        {
            printf("%c", output[i]);
            if (i < output.size()-1)
                printf(", ");
        }

        printf("]\n");
    }
}

void main()
{
    //Run(".\\Magic_sample.in");
    //Run(".\\B-small-attempt0.in");
    Run(".\\B-large.in");
    //system("Pause");
}

