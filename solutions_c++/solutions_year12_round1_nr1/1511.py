#include <stdlib.h>
#include <stdio.h>
#include <string.h>

typedef char LineType[MAX_LINE_LEN];    // MAX_LINE is defined outside to match the problem needs

// exposed API 
bool readLine(LineType a_line, FILE* a_hInput = stdin);
int  readNumLine(FILE* a_hInput);

char* readFirstToken(LineType a_line);
char* readNextToken();
int   readFirstNum(LineType a_line);
int   readNextNum();
char* skipToken(char* a_line);  // return the next token

#ifdef STL
    template<class TNum>
        void readLineOfNumbers(char* a_line, int N, vector<TNum>& a_list);

    void readLineOfD(char* a_line, int N, vector<double>& a_list);
#endif

///////////////////////////////////////////////////////////////////////////////
bool setStdinFromFile(char* a_pFilename);
bool setStdoutToFile (char* a_pFilename);

////////////////////////////// Implementation /////////////////////////////////

inline bool readLine(LineType a_line, FILE* a_hInput)
{
    char* ret = fgets(a_line, sizeof(LineType), a_hInput);
    if (ret == NULL)
        return false;

    return true;
}

inline int readNumLine(FILE* a_hInput = stdin)
{
    LineType line;
    bool fOk = readLine(line, a_hInput);
    assert(fOk);
    if (! fOk)
        return 0;

    int num; 
    sscanf_s(line, "%d", &num);
    return num;
}

//////////////////////////// Tokens /////////////////////////
static char* next_token;

inline char* readFirstToken(LineType a_line)
{
    return strtok_s(a_line, " ", &next_token);  
}

inline char* readNextToken()
{
    return strtok_s(NULL, " ", &next_token);
}

inline int readFirstNum(LineType a_line)
{
    char* token = readFirstToken(a_line);  
    return atoi(token);
}

inline double readFirstD(LineType a_line)
{
    char* token = readFirstToken(a_line);  
    return atof(token);
}

inline int readNextNum()
{
    char* token = readNextToken();
    return atoi(token);
}

inline double readNextD()
{
    char* token = readNextToken();
    return atof(token);
}

inline char* skipToken(char* a_line)   // return the next token
{ 
    while ((*a_line != 0) && (*a_line != 32))
        ++a_line;

    return ++a_line;
}

#ifdef STL

template<class TNum>
void readLineOfNumbers(char* a_line, int N, vector<TNum>& a_list)
{
    int num = readFirstNum(a_line);    
    a_list.push_back(num);

    for (int i=0; i<N-1; i++)
    {
        int num = readNextNumToken();
        a_list.push_back(num);
    }
}

void readLineOfD(char* a_line, int N, vector<double>& a_list)
{
    double num = readFirstD(a_line);    
    a_list.push_back(num);

    for (int i=0; i<N-1; i++)
    {
        double num = readNextD();
        a_list.push_back(num);
    }
}

#endif

//////////////////////////////////////////////////////////////////

inline bool setStdinFromFile(char* a_pFilename)
{
    FILE* hInput;
    errno_t err = fopen_s(&hInput, a_pFilename, "r");
    assert(err == 0);
    if (err != 0)
        return false;

    *stdin = *hInput;
    return true;
}

inline bool setStdoutToFile(char* a_pFilename)
{
    FILE* hOutput;
    errno_t err = fopen_s(&hOutput, a_pFilename, "w");
    assert(err == 0);
    if (err != 0)
        return false;

    *stdout = *hOutput;
    return true;
}
