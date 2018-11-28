#include <stdio.h>
#include <algorithm>
#include <iostream>

using namespace std;

const int MaxA = 100000;

int t,T,n,m,i,j,k,Min,l;
int a[1100],b[1100][110];
char s[110];
string name[110],st;

bool cmp(string a,string b)
{
     return (a<b);
}

int find()
{
    int l = 1,r = n,mi;
    
    while (l!=r)
    {
        mi = (l + r) / 2;
        if (name[mi]<st) l = mi + 1; else r = mi;
    }
    return l;      
}

int min(int a,int b)
{
    if (a<b) return a; else return b;
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&t);
    for (T=1;T<=t;T++)
    {
        scanf("%d\n",&n);
        for (i=1;i<=n;i++) { gets(s); name[i] = s; }
        sort(name + 1,name + n + 1,cmp);
        scanf("%d\n",&m);
        memset(a,0,sizeof(a));
        for (i=1;i<=m;i++)
        {
            gets(s); st = s;
            a[i] = find();
        }
        memset(b,0,sizeof(b));
        for (i=1;i<=m;i++)
        {
            Min = b[i-1][1]; l = 1;
            for (j=2;j<=n;j++) if (b[i-1][j]<Min) { Min = b[i - 1][j]; l = j; }
            for (j=1;j<=n;j++) b[i][j] = min(Min + 1,b[i - 1][j]);
            b[i][a[i]] = MaxA;
        }
        Min = b[m][1];
        for (i=2;i<=n;i++) Min <?= b[m][i];
        printf("Case #%d: %d\n",T,Min);
    }
    return 0;
}
