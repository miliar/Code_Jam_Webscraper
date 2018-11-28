#include <iostream>
#include <cstring>

using namespace std;

int l;
int n;
int d;
int i,j,k;
int ans;
int cntpar;
int is[20][26];
int m;
int now;
int chk;
char in[5005][20];
char tmp[5005];

int main()
{
    FILE *fin=fopen("A-large.in","r");
    FILE *fout=fopen("A-large.out","w");
    fscanf(fin,"%d %d %d",&l,&d,&n);
    for(i=0;i<d;i++)
    {
        fscanf(fin,"%s",&in[i]);
    }
    for(i=0;i<n;i++)
    {
        for(j=0;j<l;j++)
        {
            for(k=0;k<26;k++)
            is[j][k]=0;
        }
        ans=0;
        cntpar=0;
        now=-1;
        fscanf(fin,"%s",&tmp);
        m=strlen(tmp);
        for(j=0;j<m;j++)
        {
            if(tmp[j]=='(')
            {
                cntpar=1;
                now++;
            }
            else if(tmp[j]==')')
            {
                cntpar=0;
            }
            else
            {
                if(cntpar==0)
                {
                    now++;
                }
                is[now][tmp[j]-'a']=1;
            }
        }
        for(j=0;j<d;j++)
        {
            chk=1;
            for(k=0;k<l;k++)
            {
                if(is[k][in[j][k]-'a']==0)
                {
                    chk=0;
                }
            }
            ans+=chk;
        }
        fprintf(fout,"Case #%d: %d\n",i+1,ans);
    }
    return 0;
}
