#include<iostream>
using namespace std;
int n,m;
char s[100][100];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("a.out","w",stdout);
    int i,t,j,k;
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        scanf("%d%d",&n,&m);
        for(j=0;j<n;j++)
        scanf("%s",s[j]);
        int ans=0;
        for(j=0;j<n;j++)
        for(k=0;k<m;k++)
        {
            if(ans==1) break;
            if(s[j][k]=='#')
            {
                if(j+1==n || k+1==m) {ans=1;break;}
                if(s[j][k+1]=='#' && s[j+1][k]=='#' && s[j+1][k+1]=='#' )
                {
                    s[j][k]='/';
                    s[j][k+1]='\\';
                    s[j+1][k]='\\';
                    s[j+1][k+1]='/';
                }
                else ans=1;

            }
        }
       // for(j=0;j<n;j++)
          //  puts(s[j]);

        printf("Case #%d:\n",i);
        if(ans==1){
            puts("Impossible");
        }else{
            for(j=0;j<n;j++)
            puts(s[j]);
        }
    }
    return 0;
}
