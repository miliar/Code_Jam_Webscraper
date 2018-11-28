#include<cstdio>
#include<iostream>
#include<cmath>
#include<vector>
#include<map>
#include<cstring>
#include<string>

using namespace std;
char s[501][501];
long long a[501][501];
int main()
{
    int t,T,r,c,d,i,j,l,i1,j1;
    freopen("B-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);   
    scanf("%d",&T);
    for(t=1;t<=T;t++)
    {
        scanf("%d%d%d",&r,&c,&d);
        for(i=0;i<r;i++)
            scanf("%s",&s[i]);
        for(i=0;i<r;i++)
            for(j=0;j<c;j++)
                a[i][j]=s[i][j]-'0'+d;
        int ans=0;
        for(i=1;i<r-1;i++)
            for(j=1;j<c-1;j++)
                for(l=1;i-l>=0&&j-l>=0&&i+l<r&&j+l<c;l++)
                {
                    long long x=0,y=0;
                    for(i1=i-l;i1<=i+l;i1++)
                        for(j1=j-l;j1<=j+l;j1++)
                        {
                            if(abs(i1-i)==l&&abs(j1-j)==l) continue;
                            x+=(i1-i)*a[i1][j1];
                            y+=(j1-j)*a[i1][j1];
                        }
                    if(x==0&&y==0) ans=max(2*l+1,ans);
                }
        for(i=1;i<r-2;i++)
            for(j=1;j<c-2;j++)
                for(l=2;i-l+1>=0&&j-l+1>=0&&i+l<r&&j+l<c;l++)
                {
                    double x=0,y=0;
                    for(i1=i-l+1;i1<=i+l;i1++)
                        for(j1=j-l+1;j1<=j+l;j1++)
                        {
                            if(fabs(fabs(i1-i-0.5)-l+0.5)<1e-6&&fabs(fabs(j1-j-0.5)-l+0.5)<1e-6) continue;
                            x+=(i1-i-0.5)*a[i1][j1];
                            y+=(j1-j-0.5)*a[i1][j1];
                        }
                    if(fabs(x)<1e-8&&fabs(y)<1e-8) ans=max(2*l,ans);
                }
        
        printf("Case #%d: ",t);
        if(ans) printf("%d\n",ans);
        else printf("IMPOSSIBLE\n");
    }
//system("pause");
    return 0;
}
