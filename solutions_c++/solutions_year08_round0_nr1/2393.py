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
ofstream fout ("A.out");
ifstream fin ("A.in");
int main()
{
    int N;
    fin >> N;
    for(int n = 1; n <= N; n++)
    {
        int S, Q;
        fin >> S;
        string se[100];
        string dummy;
        getline(fin, dummy);
        for(int i = 0; i < S; i++)
        {
            getline(fin, se[i]);
        }        
        fin >> Q;
        string qe[1000];
        getline(fin, dummy);
        for(int i = 0; i < Q; i++)
        {
             getline(fin, qe[i]);
        }
        int bCases[1000][100];
        if(Q == 0 || Q == 1)
        {
          fout << "Case #" << n << ": 0" << endl;
        } else
        {
            for(int i = 0; i < S; i++)
            {
                bCases[0][i] = 0;
                if(strcmps(qe[0], se[i]) == 0)
                    bCases[0][i] = 10000;
            }
            for(int i = 1; i < Q; i++)
            {
                for(int j = 0; j < S; j++)
                {
                    bCases[i][j] = 10000;
                    if(strcmps(qe[i], se[j]) != 0)
                    {
                        for(int k = 0; k < S; k++)
                        {
                            bCases[i][j] = min(bCases[i][j], bCases[i - 1][k] + 1);
                        }
                        bCases[i][j] = min(bCases[i][j], bCases[i - 1][j]);
                    }
                }
            }
            int mn = 10000;
            for(int i = 0; i < S; i++)
            {
                mn = min(mn, bCases[Q - 1][i]);
            }
            fout << "Case #" << n << ": " << mn << endl;        
        } 
    }
}
