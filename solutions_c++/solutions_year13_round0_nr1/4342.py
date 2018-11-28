#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>

#include<algorithm>
#include<vector>
#include<string>
#include<stack>
#include<queue>
#include<map>
#include<sstream>
#include<utility>



#define FOR(i, s, e) for(int i=s; i<e; i++)
#define loop(i, n) for(int i=0; i<n; i++)
#define getint(n) scanf("%d", &n)
#define pb(a) push_back(a)
#define ll long long
#define dd double
#define SZ(a) int(a.size())
#define read() freopen("input.txt", "r", stdin)
#define write() freopen("output.txt", "w", stdout)
#define mem(a, v) memset(a, v, sizeof(a))
#define all(v) v.begin(), v.end()
#define pi acos(-1.0)
#define INF 1<<29
#define mod abs
#define pf printf
#define sf scanf
#define mp make_pair
#define paii pair<int, int>
#define padd pair<dd, dd>
#define pall pair<ll, ll>
#define fr first
#define sc second

using namespace std;

#define XXX 0
#define OOO 1
#define TTT 2
#define DOT 3

#define MAXX 0

int grid[4][4];
int cnt[4];
bool found;




int main()
{
    read();
    write();
    char str[6];
    int kases, kaseno = 0;
    getint(kases);

    while(kases--)
    {
        pf("Case #%d: ", ++kaseno);
        found = 0;

        loop(i, 4)
        {
            sf("%s", str);
            loop(j, 4)
            {
                if(str[j] == 'X')
                    grid[i][j] = XXX;
                else if(str[j] == 'O')
                    grid[i][j] = OOO;
                else if(str[j] == 'T')
                    grid[i][j] = TTT;
                else grid[i][j] = DOT;
            }
        }



        loop(i, 4)
        {
            mem(cnt, 0);
            loop(j, 4)
            {
                cnt[ grid[i][j] ]++;
            }

            if(cnt[XXX] + cnt[TTT] == 4)
            {
                found = 1;
                pf("X won\n");
                break;
            }
            else if(cnt[OOO] + cnt[TTT] == 4)
            {
                found = 1;
                pf("O won\n");
                break;
            }
        }

        if(found) continue;

        loop(i, 4)
        {
            mem(cnt, 0);
            loop(j, 4)
            {
                cnt[ grid[j][i] ]++;
            }

            if(cnt[XXX] + cnt[TTT] == 4)
            {
                found = 1;
                pf("X won\n");
                break;
            }
            else if(cnt[OOO] + cnt[TTT] == 4)
            {
                found = 1;
                pf("O won\n");
                break;
            }
        }

        if(found) continue;


        mem(cnt, 0);
        for(int i=0, j=0; i<4; i++, j++)
        {
            cnt[ grid[i][j] ]++;
        }


        if(cnt[XXX] + cnt[TTT] == 4)
        {
            found = 1;
            pf("X won\n");
        }
        else if(cnt[OOO] + cnt[TTT] == 4)
        {
            found = 1;
            pf("O won\n");
        }

        if(found) continue;



        mem(cnt, 0);

        for(int i=0, j=3; i<4; i++, j--)
        {
            cnt[grid[i][j] ]++;
        }

        if(cnt[XXX] + cnt[TTT] == 4)
        {
            found = 1;
            pf("X won\n");
        }
        else if(cnt[OOO] + cnt[TTT] == 4)
        {
            found = 1;
            pf("O won\n");
        }

        if(found) continue;



        loop(i, 4)
        {
            loop(j, 4)
            {
                if(grid[i][j] == DOT)
                {
                    found = 1;
                }
            }
        }

        if(found)
        {
            pf("Game has not completed\n");
        }
        else
        {
            pf("Draw\n");
        }
    }

    return 0;
}

