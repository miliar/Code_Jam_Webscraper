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

int f[110][258];
int a[110]; 
int n,m,I,D;

int myabs(int a)
{
    if (a<0) return -a;
        else return a;
}

void DP()
{
    memset(f,127,sizeof(f));
    int Max=f[0][0];
    f[0][256]=0;
    for (int i=0;i<n;i++)
    {
        for (int j=0;j<256;j++)
        if (f[i][j]!=Max)
        {
            for (int k=0;k<=255;k++)
            {
                int delta=myabs(k-j)-1;
                if (delta<0) delta=0;
                else
                if (m!=0) delta=(delta/m)*I;
                else
                    continue;
                f[i+1][k]=min(f[i+1][k],f[i][j]+delta+myabs(k-a[i+1]));
            }
            f[i+1][j]=min(f[i+1][j],f[i][j]+D);
        }
        for (int k=0;k<=255;k++) f[i+1][k]=min(f[i+1][k],f[i][256]+myabs(k-a[i+1]));
        f[i+1][256]=f[i][256]+D;
    }
}

int main()
{
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    int T;
    scanf("%d",&T);
    for (int casenum=1;casenum<=T;casenum++)
    {
        scanf("%d%d%d%d",&D,&I,&m,&n);
        for (int i=1;i<=n;i++) scanf("%d",&a[i]);
        DP();
        int ans=100000000;
        for (int i=0;i<=256;i++) 
            ans=min(ans,f[n][i]);
        printf("Case #%d: %d\n",casenum,ans);
    }
}
