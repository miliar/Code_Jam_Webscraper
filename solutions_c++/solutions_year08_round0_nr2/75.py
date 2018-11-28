
#include <algorithm>
#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <list>

using namespace std;

#define PATH "c:\\jam3\\debug\\"

int main(void)
{
    ifstream fin(PATH "s.in");
    ofstream fout(PATH "s.out");

    int count;
    fin >> count;
    for (int x = 1; x <= count; ++x)
    {
        char buf[1024];

        // 0<=T<=60
        // 0<=NA,NB<=100
        int atime[100][2], btime[100][2];

        int T, NA, NB;
        fin >> T;
        fin >> NA >> NB; // NA: a=>b NB b=>a
        //printf("%d %d %d\n", T, NA, NB);
        fin.getline(buf, 1024);
        {
        for (int a = 0; a < NA; ++a)
        {
            fin.getline(buf, 1024);
            int sh, sm, eh, em;
            sscanf(buf, "%d:%d %d:%d", &sh, &sm, &eh, &em);
            //printf("A%d:%d %d %d %d\n",a, sh, sm, eh, em);
            atime[a][0] = sh * 60 + sm;
            atime[a][1] = eh * 60 + em + T;
        }
        for (int b = 0; b < NB; ++b)
        {
            fin.getline(buf, 1024);
            int sh, sm, eh, em;
            sscanf(buf, "%d:%d %d:%d", &sh, &sm, &eh, &em);
            //printf("B%d:%d %d %d %d\n",b, sh, sm, eh, em);
            btime[b][0] = sh * 60 + sm;
            btime[b][1] = eh * 60 + em + T;
        }
        }
        int ansA = 0;
        int ansB = 0;
        int stA = 0;
        int stB = 0;
        for (int t = 0; t <= 23*60+59+60; ++t)
        {
            int a, b;
            for (a = 0; a < NA; ++a)
            {
                if (atime[a][1] == t)
                {
                    stB++;
                }
            }
            for (b = 0; b < NB; ++b)
            {
                if (btime[b][1] == t)
                {
                    stA++;
                }
            }

            for (a = 0; a < NA; ++a)
            {
                if (atime[a][0] == t)
                {
                    if (stA > 0)
                        stA--;
                    else
                        ansA++;
                }
            }
            for (b = 0; b < NB; ++b)
            {
                if (btime[b][0] == t)
                {
                    if (stB > 0)
                        stB--;
                    else
                        ansB++;
                }
            }
        }


        fout << "Case #" << x << ": " << ansA << " " << ansB << "\n";
    }

    return 0;
}

