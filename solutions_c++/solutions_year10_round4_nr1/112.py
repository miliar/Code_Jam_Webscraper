#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>

using namespace std;

int a[200][200];
int real[220][220];
int ans,len,n;

void cal(int x,int y)
{
    memset(real,255,sizeof(real));
    for (int i=0;i<n;i++)
        for (int j=0;j<n;j++)
            real[x+i][y+j]=a[i+1][j+1];
    for (int i=1;i<=len;i++)
    {
        int x1=i,y1=1,x2=1,y2=i;
        while (x1>x2)
        {   
            if (real[x1][y1]!=-1 && real[x2][y2]!=-1 && real[x1][y1]!=real[x2][y2]) return;
            x1--; y1++; x2++; y2--;
        }
    }
    for (int i=1;i<=len;i++)
    {
        int x1=len,y1=i,x2=i,y2=len;
        while (x1>x2)
        {
            if (real[x1][y1]!=-1 && real[x2][y2]!=-1 && real[x1][y1]!=real[x2][y2]) return;
            x1--; y1++; x2++; y2--;
        }
    }
    for (int i=1;i<=len;i++)
    {
        int x1=len,y1=i,x2=len-i+1,y2=1;
        while (x1>x2)
        {   
            if (real[x1][y1]!=-1 && real[x2][y2]!=-1 && real[x1][y1]!=real[x2][y2]) return;
            x1--; y1--; x2++; y2++;
        }
    }
    for (int i=1;i<=len;i++)
    {
        int x1=len-i+1,y1=len,x2=1,y2=i;
        while (x1>x2)
        {
            if (real[x1][y1]!=-1 && real[x2][y2]!=-1 && real[x1][y1]!=real[x2][y2]) return;
            x1--; y1--; x2++; y2++;
        }
    }
    ans=min(ans,len*len-n*n);
}

int main()
{
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    int T;
    scanf("%d",&T);
    for (int casnum=0;casnum<T;casnum++)
    {
        ans=1000000;
        scanf("%d",&n);
        memset(a,255,sizeof(a));
        for (int i=1;i<=n;i++)
        {
            int x=i;
            for (int j=1;x>=1;j++,x--) scanf("%d",&a[x][j]);
        }
        for (int j=2;j<=n;j++)
        {
            int y=j;
            for (int i=n;y<=n;i--,y++) scanf("%d",&a[i][y]);
        }
        for (len=n;len<210 && ans==1000000;len++)
            for (int i=1;i<=len-n+1;i++) 
                {cal(i,1);cal(i,len-n+1);cal(1,i);cal(len-n+1,i);}
        printf("Case #%d: %d\n",casnum+1,ans);
    }
}
