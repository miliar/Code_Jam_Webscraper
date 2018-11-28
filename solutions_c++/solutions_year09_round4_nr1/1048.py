/*
Program:
Author: ldl
Method:
DataStructure:
Date: 2009-7-16
Status:
Remark:
*/
#include<iostream>
#include<algorithm>
#include<cmath>
#include<cstring>
#include<string>

using namespace std;
#define MaxN 100

int n;
int f[MaxN];

void init()
{
    char s[100];
    scanf("%d", &n);
    for (int i = 1; i <= n ; i++)
    {
        scanf("%s", s + 1);
        f[i] = 0;
        for (int j = n; j >= 1 ; j--)
           if (s[j] == '1') 
           {
               f[i] = j;
               break;
           }
    }
}

void solve()
{
    int ans = 0;
    for (int i = 1; i <= n ; i++)
    {
        int k;
        for (int j = i; j <= n; j++)
          if (f[j] <= i)
          {
              k = j;
              break;
          }
        ans += k - i;
        for (int j = k; j > i; j--)
            f[j] = f[j - 1];
    }
    printf("%d\n", ans);
}

int main()
{
//    freopen("test.in","r",stdin);
//    freopen("test.out","w",stdout);
    int Case;
    scanf("%d", &Case);
    for (int i = 1; i <= Case ; i++)
    {
       printf("Case #%d: ", i);  
       init();
       solve();
    }
    return 0;
}

