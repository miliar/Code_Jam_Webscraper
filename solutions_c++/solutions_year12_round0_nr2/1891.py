#include <WTypes.h>
#include <direct.h>
#include <cmath>
#include <assert.h>

//#include <algorithm>
#include <vector>
//#include <list>
//#include <map>
using namespace std;

enum {MAX_LINE_LEN = 512};
#include "InputUtils.h"


int runCase(vector<int> v, int S, int p)
{
    int ok = 0;
    int okWS = 0;
    for (int i=0; i<v.size(); i++)
    {
        int remain = v[i]-p; // for two
        if (remain < 0)
            continue;

        int diff = p - remain/2;
        if (diff <= 1)
            ok++;
        else if (diff == 2)
            okWS++;
    }

    return ok + min(okWS, S);
}

void Run(char* a_inputFile)
{
    FILE* hInput;
    errno_t err = fopen_s(&hInput, a_inputFile, "r");
    if (err != 0) {
        printf("File not found \n");
        return;
    }

    int T = readNumLine(hInput);  // number of cases

    LineType line;
    for (int i=0; i < T; i++)
    {
        readLine(hInput, line);
        int N = ReadFirstNumToken(line);
        int S = ReadNextNumToken();
        int p = ReadNextNumToken();

        vector<int> vTotal(N);
        for (int j=0; j<N; j++)
            vTotal[j] = ReadNextNumToken();

        int ans = runCase(vTotal, S, p);

        printf("Case #%d: %i \n", i+1, ans);
    }
}


void main()
{
    _chdir(".\\Src");
    bool fOk = SetStdoutToFile("B-large.out");

    Run("B-large.in");

    system("pause");
}

