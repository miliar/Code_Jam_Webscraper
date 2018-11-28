#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <vector>
#include <string>
#include <map>
#include <queue>
#include <stack>
#include <set>
#include <list>
#include <iostream>
#include <sstream>
#include <algorithm>

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

//int rx[] = {0,-1,0,1,1,-1,-1,0,1}; //four direction x
//int ry[] = {0,1,1,1,0,0,-1,-1,-1   //four direction y
//int rep[] = {1,1,4,4,2,1,1,4,4,2}; //repet cycle for mod
//void ullpr(){printf("range unsigned long long : %llu\n",-1U);} //for ull
//void ulpr(){printf("range unsigned long : %lu\n",-1U);} //for ull
//void upr(){printf("range unsigned : %u\n",-1U);} //for ull


int arr[1000];

int main()
{
    freopen("be.in","r",stdin);
    freopen("b.out","w",stdout);
    int i,j,k,p,n,s;
    int tcase,cas=1;
    scanf(" %d",&tcase);
    while(tcase--)
    {
        scanf(" %d %d %d",&n,&s,&p);
        int val;
        int cnt=0,sur = 0;
        for(i=1 ;i<=n ; i++)
        {
            scanf(" %d",&val);
            if(val<p) continue;
            val -= p;
            if(val>=2*p) cnt++;
            else if(abs((val/2) - p) <= 1) {cnt++;}
            else
            {
                if(val>=(p-2)*2 &&s )
                {
                    s--;cnt++;
                }
            }
        }
        printf("Case #%d: %d\n",cas++,cnt);
    }
    return 0;
}
