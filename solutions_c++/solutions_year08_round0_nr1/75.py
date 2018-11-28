
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
    //FILE *fp = fopen(PATH "s.in", "r");
    ifstream fin(PATH "s.in");
    ofstream fout(PATH "s.out");

    char engine[100][102];
    char query[1000][102];
    int queryN[1000];
    int flag[100];
    char buf[1024];

    int count;
    fin >> count;
    //fscanf(fp, "%d\n", &count);
    for (int x = 1; x <= count; ++x)
    {
        int i;
        int numEngine;
        fin >> numEngine;
        fin.getline(buf, 1024);
        printf("Engine:%d\n", numEngine);
        //fscanf(fp, "%d\n", &numEngine);
        for (i = 0; i < numEngine; ++i)
        {
            fin.getline(engine[i], 101);
            //fgets(engine[i], 101, fp);
            //fscanf(fp, "%s", engine[i]);
            printf("Engine%d:%s\n", i, engine[i]);
        } 

        int numQuery;
        fin >> numQuery;
        fin.getline(buf, 1024);
        printf("Query:%d\n", numQuery);
        //fscanf(fp, "%d\n", &numQuery);
        for (i = 0; i < numQuery; ++i)
        {
            fin.getline(query[i], 101);
            //fgets(query[i], 101, fp);
            printf("Query%d:%s\n", i, query[i]);
            int j;
            for (j = 0; j < numEngine; ++j)
            {
                if (strcmp(query[i], engine[j]) == 0)
                    break;
            }
            if (j == numEngine)
                fout << "Error\n";
            printf("%d\n", j);
            queryN[i] = j;
        }

        int useEngine = 0;
        int ans = 0;
        {
            for (int j = 0; j < numEngine; ++j)
            {
                flag[j] = 0;
            }
            useEngine = 0;
        }
        for (i = 0; i < numQuery; ++i)
        {
            int engine = queryN[i];
            if (flag[engine] == 0)
            {
                useEngine++;
                flag[engine] = 1;
            }
            if (useEngine >= numEngine)
            {
                ans++;

                for (int j = 0; j < numEngine; ++j)
                {
                    flag[j] = 0;
                }
                useEngine = 0;

                useEngine++;
                flag[engine] = 1;
            }
        }

        fout << "Case #" << x << ": " << ans << "\n";
    }
    //fin >> count;

    //fin >> a >> b >> c;

    return 0;
}

