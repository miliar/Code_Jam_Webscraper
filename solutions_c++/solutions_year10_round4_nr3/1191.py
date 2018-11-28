#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
using namespace std;

int n;
int num[110][110];
int copys[110][110];
const int row=101;
const int col=101;

bool ok()
{
    for(int i=1;i<col;i++)
        for(int j=1;j<row;j++)
            if(num[i][j])
                return false;
    return true;
}

int main()
{
    freopen("C-small-attempt8.in","r",stdin);
    freopen("res.out","w",stdout);
    int test;
    scanf("%d",&test);
    for(int cas=1;cas<=test;cas++)
    {
        scanf("%d",&n);
        int xa,xb,ya,yb;
        memset(num,0,sizeof(num));
        for(int k=0;k<n;k++)
        {
            scanf("%d%d%d%d",&xa,&ya,&xb,&yb);
            for(int i=xa;i<=xb;i++)
                for(int j=ya;j<=yb;j++)
                    num[j][i]=1;
        }
        int res=0;
        while(!ok())
        {
                res++;
                for(int i=1;i<col;i++)
                    for(int j=1;j<row;j++)
                    {
                        if(num[i][j])
                        {
                            if(!num[i-1][j]&&!num[i][j-1])
                                copys[i][j]=0;
                            else copys[i][j]=1;
                        }
                        else
                        {
                            if(num[i-1][j]&&num[i][j-1])
                                copys[i][j]=1;
                            else copys[i][j]=0;
                        }
                    }
                memcpy(num,copys,sizeof(copys));
        }
        printf("Case #%d: %d\n",cas,res);
    }
    return 0;
}
            
