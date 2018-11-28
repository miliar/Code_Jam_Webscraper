//Copyright by Le Viet Thanh Long
#include <iostream>
#include <cstring>
#include <algorithm>
#include <cstdio>
#include <string>
#include <queue>
#include <stack>
#include <iomanip>
#include <map>
#include <set>
#include <vector>
#include <cmath>
#include <cstdlib>

#define maxn 100+7
#define eps 1e-6
#define oo 1000000000

using namespace std;
typedef long long LL;
typedef pair<int,int> II;
typedef pair<II,int> III;

int n,s,p;
int A[maxn];

void Input()
{
    scanf("%d%d%d",&n,&s,&p);
    for (int i = 1; i <= n; i++)
        scanf("%d",&A[i]);
}

void Solve(int t)
{
    sort(A+1, A+1+n);
    int res = 0;
    for (int i = 1; i <= n; i++)
        if (A[i] >= p)
        if (s == 0)
        {
            if (A[i] % 3 == 0 && A[i] / 3 >= p)
                res++;
            else if (A[i] % 3 == 1 && A[i] / 3 + 1 >= p)
                res++;
            else if (A[i] % 3 == 2 && A[i] / 3 + 1 >= p)
                res++;
        }
        else
        {
            if (A[i] % 3 == 0 && A[i] / 3 + 1 >= p)
            {
                s--;
                res++;
            }
            else if (A[i] % 3 == 1 && A[i] / 3 + 1 >= p)
            {
                s--;
                res++;
            }
            else if (A[i] % 3 == 2 && A[i] / 3 + 2 >= p)
            {
                s--;
                res++;
            }
        }
    printf("Case #%d: %d\n",t,res);
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("ProblemB.out","w",stdout);
    int t;
    scanf("%d",&t);
    for (int i = 1; i <= t; i++)
    {
        Input();
        Solve(i);
    }
    return 0;
}
