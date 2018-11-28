#include <WTypes.h>
#include <stdlib.h>
#include <ctype.h>
#include "stdio.h"
#include "string.h"
#include <vector>
using namespace std;

enum {MAX_LINE = 8*1024};
char Line[MAX_LINE];

typedef vector<int> ListType;
int g_Total = 0;

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

bool readCase(FILE* a_hInput, ListType& a_list)
{
    int N = readNumLine(a_hInput);
    if (N == 0)
        return true;

    char* ret = fgets(Line, MAX_LINE, a_hInput);
    if (ret == NULL)
        return false;

    char* token = strtok_s(Line, " ", &next_token);    
    a_list.push_back(atoi(token));

    for (int i=0; i<N-1; i++)
    {
        token = ReadNextToken();
        a_list.push_back(atoi(token));
    }
    return true;
}

// Num represents the split between piles
int calcValue(int a_num, ListType& a_list)
{
    int A_xor = 0;
    int A_total = 0;
    int B_xor = 0;

    for (UINT i=0; i < a_list.size(); ++i)
    {
        if (a_num & (1<<i))
        {
            A_xor ^= a_list[i];
            A_total += a_list[i];
        }
        else 
            B_xor ^= a_list[i];
    }

    if ((A_xor == B_xor) && (A_total > 0))
    {
        int B_total = g_Total - A_total;
        return max(A_total, B_total);
    }
        
    return -1;
}

int XOR_List(ListType& a_list)
{
    int sum = 0;
    for (UINT i=0; i<a_list.size(); i++)
        sum ^= a_list[i];

    return sum;
}

int Total_List(ListType& a_list)
{
    int sum = 0;
    for (UINT i=0; i<a_list.size(); i++)
        sum += a_list[i];

    return sum;
}

// return -1 if there is no solution
int runCase(ListType& a_list)
{
    int XOR_result = XOR_List(a_list);
    if (XOR_result != 0)
        return -1;

    g_Total = Total_List(a_list);

    if (a_list.size() > 32)
        return -1;

    int maxValue = -1;
    int loopTo = 1 << (a_list.size()-1);

    for (int i=0; i < loopTo; ++i)
    {
        int currVal = calcValue(i, a_list);
        if (currVal > maxValue)
            maxValue = currVal;
    }

    return maxValue;
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
        ListType candyList;
        bool fOk = readCase(hInput, candyList);
        int maxVal = runCase(candyList);

        if (maxVal == -1)
            printf("Case #%d: NO \n", i+1);
        else
            printf("Case #%d: %d \n", i+1, maxVal);
    }
}

void main()
{
    //Run(".\\Candy_sample.in");
    Run(".\\C-small-attempt0.in");
    //Run(".\\B-large.in");
    system("Pause");
}

