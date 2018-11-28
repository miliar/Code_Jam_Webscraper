#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstring>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define pb push_back
#define clean(a,b) memset(a,b,sizeof(a))
#define oo 1<<20
#define dd double
#define ll long long
#define ull unsigned long long
#define ff float
#define EPS 10E-10
#define fr first
#define sc second
#define MAXX 100000
#define PRIME_N 1000000
#define INFI 1<<30
#define SZ(a) ((int)a.size())
#define all(a) a.begin(),a.end()
#define MODD 1000000007
#define bpcnt(a) __builtin_popcount(a)
#define REP(i,n) for (i=0;i<n;i++)
#define FOR(i,p,k) for (i=p; i<k;i++)

//int rx[] = {0,-1,0,1,1,-1,-1,0,1}; //four direction x
//int ry[] = {0,1,1,1,0,0,-1,-1,-1};   //four direction y
//int rep[] = {1,1,4,4,2,1,1,4,4,2}; //repet cycle for mod
//void ullpr(){printf("range unsigned long long : %llu\n",-1U);} //for ull
//void ulpr(){printf("range unsigned long : %lu\n",-1U);} //for ull
//void upr(){printf("range unsigned : %u\n",-1U);} //for ull

vector<string>v;

int main()
{
    freopen("al.in","r+",stdin);
    freopen("out.out","w+",stdout);
    int tcase,cas=1;
    scanf(" %d",&tcase);
    while(tcase--)
    {
        v.clear();
        string str;
        for(int i = 0 ; i<4  ;i++)
        {
            cin>>str;
            v.pb(str);
        }
        int iswin = 0;
        int wino = 0,winx = 0,notend = 0,draw = 0;
        if(iswin==0)
        {
            for(int i = 0 ; i<4 && !iswin ; i++)
            {
                int o = 0,x = 0,t = 0;
                for(int j = 0 ; j<4 && !iswin; j++)
                {
                    if(v[i][j]=='X') x++;
                    else if(v[i][j]=='O') o++;
                    else if(v[i][j]=='T') t++;
                }
                if(x+t== 4 || o+t ==4)
                {
                    iswin = 1;
                    wino = (o+t==4);
                    winx = (x+t==4);
                }
            }

        }
        if(iswin==0)
        {
            for(int i = 0 ; i<4 && !iswin ; i++)
            {
                int o = 0,x = 0,t = 0;
                for(int j = 0 ; j<4 && !iswin; j++)
                {
                    if(v[j][i]=='X') x++;
                    else if(v[j][i]=='O') o++;
                    else if(v[j][i]=='T') t++;
                }
                if(x+t== 4 || o+t ==4)
                {
                    iswin = 1;
                    wino = (o+t==4);
                    winx = (x+t==4);
                }
            }

        }
        if(iswin==0)
        {
            int o = 0,x = 0,t = 0;
            for(int i = 0 , j = 0 ; i<4  ; i++,j++)
            {
                if(v[i][j]=='X') x++;
                else if(v[i][j]=='O') o++;
                else if(v[i][j]=='T') t++;
            }
            if(x+t== 4 || o+t ==4)
            {
                iswin = 1;
                wino = (o+t==4);
                winx = (x+t==4);
            }
        }

        if(iswin==0)
        {
            int o = 0,x = 0,t = 0;
            for(int i = 0 , j = 3 ; i<4  ; i++,j--)
            {
                if(v[i][j]=='X') x++;
                else if(v[i][j]=='O') o++;
                else if(v[i][j]=='T') t++;
            }
            if(x+t== 4 || o+t ==4)
            {
                iswin = 1;
                wino = (o+t==4);
                winx = (x+t==4);
            }
        }

        if(iswin==0)
        {
            int dot = 0;
            for(int i = 0 ; i<4  ; i++)
                for(int j = 0 ; j<4 ; j++)
                    if(v[i][j]=='.') dot++;
            if(dot==0)
                draw = 1;
            else notend = 1;
        }

        printf("Case #%d: ",cas++);
        if(iswin)
        {
            if(winx)
                cout<<"X won"<<endl;
            else cout<<"O won"<<endl;
        }
        else
        {
            if(draw)
                cout<<"Draw"<<endl;
            else cout<<"Game has not completed"<<endl;
        }
    }
    return 0;
}
