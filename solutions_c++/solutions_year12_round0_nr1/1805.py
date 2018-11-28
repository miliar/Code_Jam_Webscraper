#include <stdlib.h>
#include <stdio.h>
#include <string.h>


typedef char LineType[MAX_LINE_LEN];    // MAX_LINE is defined outside to match the problem needs

bool readLine(FILE* a_hInput, LineType a_line)
{
    char* ret = fgets(a_line, sizeof(LineType), a_hInput);
    if (ret == NULL)
        return false;

    return true;
}

int readNumLine(FILE* a_hInput)
{
    LineType line;
    bool fOk = readLine(a_hInput, line);
    if (line == NULL)
        return 0;

    int num; 
    sscanf_s(line, "%d", &num);
    return num;
}

//////////////////////////// Tokens /////////////////////////
static char* next_token;

char* ReadFirstToken(LineType a_line)
{
    return strtok_s(a_line, " ", &next_token);  
}

char* ReadNextToken()
{
    return strtok_s(NULL, " ", &next_token);
}

int ReadFirstNumToken(LineType a_line)
{
    char* token = ReadFirstToken(a_line);  
    return atoi(token);
}

int ReadNextNumToken()
{
    char* token = ReadNextToken();
    return atoi(token);
}

char* SkipToken(char* a_line)
{ 
    while ((*a_line != 0) && (*a_line != 32))
        ++a_line;

    return ++a_line;
}

template<class TNum>
void ReadLineOfNumbers(char* a_line, int N, vector<TNum>& a_list)
{
    int num = ReadFirstNumToken(a_line);    
    a_list.push_back(num);

    for (int i=0; i<N-1; i++)
    {
        int num = ReadNextNumToken();
        a_list.push_back(num);
    }
}

//////////////////////////////////////////////////////////////////

bool SetStdoutToFile(char* a_pFilename)
{
    FILE* hOutput;
    errno_t err = fopen_s(&hOutput, a_pFilename, "w");
    if (err != 0)
        return false;

    *stdout = *hOutput;
    return true;
}
