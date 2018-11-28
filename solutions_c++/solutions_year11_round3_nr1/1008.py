#include<iostream>
#include<sstream>
#include<algorithm>
#include<numeric>
#include<vector>
#include<string>
#include<map>
#include<set>
#include<list>
#include<stack>
#include<queue>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<cctype>
#include<climits>
#include<cfloat>
#include<cassert>
#define dbge( x ) cout << #x << " : " <<  x << endl;
using namespace std;

int gr, gc;

string s[51];
bool isValid(int i, int j)
{
    return (i >= 0 && i < gr && j >= 0 && j < gc && s[i][j] != '.' && s[i][j] != '/' && s[i][j] != '\\');
}

int di[] = { 0, 0, +1, +1 };
int dj[] = { 0, +1, 0, +1 };
char dc[] = { '/', '\\', '\\', '/'};



int main()
{
    int T;
    scanf("%d", &T);
    for(int t = 1; t <= T; t++)
    {
        printf("Case #%d:\n", t);
        int r, c;
        cin >> r >> c;
        gr = r, gc = c;
        for(int i = 0; i < r; i++)
            cin >> s[i];
        int poss = 1;
        for(int i = 0; i < r; i++)
        {
            for(int j = 0; j < c; j++)
            {
                if(s[i][j] == '#')
                {
                    for(int k = 0; k < 4; k++)
                    {
                        if(isValid(i + di[k], j + dj[k]))
                            ;
                        else
                        {
                            poss = 0;
                            break;
                        }
                    }
                    if(poss != 0)
                    {
                        for(int k = 0; k < 4; k++)
                        {
                            s[i + di[k]][j + dj[k]] = dc[k];
                        }
                    }
                        else
                            break;


                }
            }
            if(poss == 0)
                break;
        }
        if(poss == 0)
            cout << "Impossible" << endl;
        else
        {
            for(int i = 0; i < r; i++)
                cout << s[i] << endl;
        }
    }
    return 0;
}

