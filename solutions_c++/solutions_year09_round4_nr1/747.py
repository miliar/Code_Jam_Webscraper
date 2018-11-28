#include <iostream>

using namespace std;

int t,n;
int jjj,i,j;
char x[105];
int tmp[105];
int is[105];
int ans;
int j1;

int main()
{
    FILE *fin=fopen("A-large.in","r");
    FILE *fout=fopen("A.out","w");
    fscanf(fin,"%d",&t);
    for(jjj=1;jjj<=t;jjj++)
    {
        ans=0;
        fscanf(fin,"%d",&n);
        for(i=1;i<=n;i++)
        {
            is[i]=0;
            fscanf(fin,"%s",&x);
            for(j=n-1;j>0;j--)
            {
                if(x[j]=='1')
                {
                    break;
                }
            }
            j++;
            tmp[i]=j;
        }
        for(i=1;i<=n;i++)
        {
            for(j=1;j<=n;j++)
            {
                if(tmp[j]<=i&&is[j]==0)
                {
                    break;
                }
            }
            is[j]=1;
            for(j1=1;j1<j;j1++)
            {
                if(is[j1]==0)
                ans++;
            }
        }
        fprintf(fout,"Case #%d: %d\n",jjj,ans);
    }
    return 0;
}
