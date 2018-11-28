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
    int T;
    fin >> T;
    for(int testCase = 1; testCase <= T; testCase++)
    {
        int N;
        int result = 0;
        fin >> N;
        int v1[1000], v2[1000];
        int used1[1000], used2[1000];
        for(int i = 0; i < N; i++)
        {
            fin >> v1[i];
            used1[i] = 0;
        }
        for(int i = 0; i < N; i++)
        {
            fin >> v2[i];
            used2[i] = 0;
        }
        for(int go = 0; go < N; go++)
        {
            int maxVal = -1;
            int maxSign = 0;
            int maxP = -1;
            int maxVec = -1;
            for(int i = 0; i < N; i++)
            {
                if(used1[i] != 1)
                {
                    if(maxVal < abs(v1[i]))
                    {
                        maxP = i;
                        maxVec = 1;
                        maxSign = -1;
                        if(v1[i] > 0)
                            maxSign = 1;
                        maxVal = abs(v1[i]);
                    }
                }
                if(used2[i] != 1)
                {
                    if(maxVal < abs(v2[i]))
                    {
                        maxP = i;
                        maxVec = 2;
                        maxSign = -1;
                        if(v2[i] > 0)
                            maxSign = 1;
                        maxVal = abs(v2[i]);
                    }
                }
            }
            if(maxVec == 2)
            {
                used2[maxP] = 1;
            } else
            {
                used1[maxP] = 1;
            }
            if(maxSign == 1)
            {
                if(maxVec == 2)
                {
                    int pos = 0;
                    for(int i = 0; i < N; i++)
                    {
                        if((v1[pos] > v1[i] || used1[pos] == 1) && used1[i] != 1)
                        {
                            pos = i;
                        }
                    }
                    used1[pos] = 1;
                    result = result + v1[pos]*maxVal*maxSign;
                } else
                {
                    int pos = 0;
                    for(int i = 0; i < N; i++)
                    {
                        if((v2[pos] > v2[i] || used2[pos] == 1) && used2[i] != 1)
                        {
                            pos = i;
                        }
                    }      
                    used2[pos] = 1;
                    result = result + v2[pos]*maxVal*maxSign;          
                }
            } else
            {
                if(maxVec == 2)
                {
                    int pos = 0;
                    for(int i = 0; i < N; i++)
                    {
                        if((v1[pos] < v1[i] || used1[pos] == 1) && used1[i] != 1)
                        {
                            pos = i;
                        }
                    }
                    used1[pos] = 1;
                    result = result + v1[pos]*maxVal*maxSign;
                } else
                {
                    int pos = 0;
                    for(int i = 0; i < N; i++)
                    {
                        if((v2[pos] < v2[i] || used2[pos] == 1) && used2[i] != 1)
                        {
                            pos = i;
                        }
                    }      
                    used2[pos] = 1;
                    result = result + v2[pos]*maxVal*maxSign;          
                }
            } 
        }
        fout << "Case #" << testCase << ": " << result << endl;  
    }
    
}
