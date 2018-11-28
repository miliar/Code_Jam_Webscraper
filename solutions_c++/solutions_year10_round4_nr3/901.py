#include<stdio.h>
#include<iostream>
#include<string>
#include<cstring>
#include<queue>
#include<vector>
#include<map>
#include<sstream>
#include<math.h>
#include<algorithm>
#define ll long long
#define clr(x) memset(x,0,sizeof(x))
#define _clr(x) memset(x,-1,sizeof(x))
#define fr(i,a,b) for(int i=a;i!=b;i++)
#define frr(i,a,b) for(int i=a;i!=b;i--)
#define pf printf
#define sf scanf
#define mp make_pair
#define pb push_back
using namespace std;
const int N = 110;

int a[N][N][2];
int f;

const int M = 100;

bool ok()
{
    for(int i = 1; i <= M; i++)
    {
        for(int j = 1; j <= M; j++)
        {
            if(a[i][j][f]) return 0;
        }
    }
    return 1;
}

void modle()
{

}

void solve(int tcase)
{
    int res = 0;
    while(1)
    {
        if(ok()) break;
        res++;
        modle();
        f ^= 1;
    }
    printf("Case #%d: %d\n", tcase, res);
}

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T;
    cin>>T;
    int ca=0;
    while(T--)
    {
        int n;
        cin>>n;
        memset(a, 0, sizeof(a));
        f = 0;
        for(int i = 1; i <= n; i++)
        {
            int X1, Y1, X2, Y2;
            cin>>X1>>Y1>>X2>>Y2;
            swap(X1, Y1);
            swap(X2, Y2);

            for(int i = X1; i <= X2; i++)
            {
                for(int j = Y1; j <= Y2; j++)
                {
                    a[i][j][f] = 1;
                }
            }
        }
        int res = 0;
        while(1)
        {
            if(ok()) break;
            res++;
            for(int i = 1; i <= M; i++)
            {
                for(int j = 1; j <= M; j++)
                {
                    a[i][j][f^1] = a[i][j][f];
                    if(a[i][j][f])
                    {
                        if(!a[i-1][j][f] && !a[i][j-1][f]) a[i][j][f^1] = 0;
                    }
                    else
                    {
                        if(a[i-1][j][f] && a[i][j-1][f]) a[i][j][f^1] = 1;
                    }
                }
            }
            f ^= 1;
        }
        printf("Case #%d: %d\n", ++ca, res);
    }
}
