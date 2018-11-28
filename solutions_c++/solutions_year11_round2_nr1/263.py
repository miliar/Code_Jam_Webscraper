#include<cstdio>
#include<cstring>
#define _clr(x,v) memset(x,0,sizeof(x))
using namespace std;

char s[110][110];
int n,m;
int win[110],comp[110];
double wp[110],owp[110],oowp[110];
void input()
{
    _clr(win,0);
    _clr(comp,0);
    _clr(wp,0);
    _clr(owp,0);
    _clr(oowp,0);
    scanf("%d",&n);
    for(int i=0;i<n;i++)
    {    
        scanf("%s",s[i]);
        for(int j=0;j<n;j++)
        {
            if(s[i][j]!='.') comp[i]++;
            if(s[i][j]=='1') win[i]++;
        }
    }        
}
void cal()
{
        //wp
    for(int i=0;i<n;i++)
        wp[i]=1.0*win[i]/comp[i];
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<n;j++)
            if(s[i][j]!='.' && comp[j]>1){
                owp[i]+=1.0*(win[j]-(s[j][i]=='1'))/(comp[j]-1);
            }
        owp[i]/=comp[i];
//        printf("--%lf\n",owp[i]);
    }
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<n;j++)
            if(s[i][j]!='.') oowp[i]+=owp[j];
        oowp[i]/=comp[i];
     }
        //output
    for(int i=0;i<n;i++)
        printf("%.8lf\n",0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]);
}
int main()
{
    freopen("A.out","w",stdout);
    int cs;
    scanf("%d",&cs);
    for(int t=1;t<=cs;t++)
    {
        printf("Case #%d:\n",t);
        input();
        cal();
    }
    return 0;
}
