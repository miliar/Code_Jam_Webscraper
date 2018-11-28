#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <cctype>
#include <algorithm>
#include <map>
#include <iomanip>
#include <windows.h>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <stdio.h>
using namespace std;

int strcmps(string a, string b)
{
    if(b.length() != a.length())
        return 1;
    for(int i = 0; i < a.length(); i++)
    {
        if(a[i] != b[i])
            return 1;
    }
    return 0;
}
ofstream fout ("B.out");
ifstream fin ("B.in");

int main()
{
    int TC;
    fin >> TC;
    for(int testCase = 1; testCase <= TC; testCase++)
    {
        int N, M;
        fin >> N >> M;
        int minM = 11;
        int solution[10];
        int malted[10];
        for(int i = 0; i < N; i++)
        {
            malted[i] = 0;
        }
        bool customer[100][10][2];
        for(int i = 0; i < M; i++)
        {
            for(int j = 0; j < N; j++)
            {
                customer[i][j][0] = false;
                customer[i][j][1] = false;
            }
            int T;
            fin >> T;
            for(int j = 0; j < T; j++)
            {
                int f, m;
                fin >> f;
                fin >> m;
                customer[i][f - 1][m] = true;
            }
        }
        bool finished = false;
        while(!finished)
        {
            bool anyD = false;
            for(int i = 0; i < M; i++)
            {
                bool cH = false;
                for(int j = 0; j < N; j++)
                {
                    cH = (cH || customer[i][j][malted[j]]);
                }
                if(!cH)
                    anyD = true;
            }
            int mCount = 0;
            for(int i = 0; i < N; i++)
            {
                mCount += malted[i];
            }
            if(!anyD && (mCount < minM))
            {
                for(int i = 0; i < N; i++)
                {
                    solution[i] = malted[i];
                }
                minM = mCount;
            }
            malted[0]++;
            for(int i = 1; i < N; i++)
            {
                if(malted[i - 1] == 2)
                    malted[i]++;
            }
            for(int i = 0; i < N - 1; i++)
            {
                if(malted[i] == 2)
                    malted[i] = 0;
            }
            if(malted[N - 1] == 2)
                finished = true;
        }
        if(minM == 11)
        {
            fout << "Case #" << testCase << ": IMPOSSIBLE" << endl;  
        } else
        {
            fout << "Case #" << testCase << ": ";
            for(int i = 0; i < N - 1; i++)
            {
                fout << solution[i] << " ";
            }
            fout << solution[N - 1] << endl;
        }
    }
    
}
