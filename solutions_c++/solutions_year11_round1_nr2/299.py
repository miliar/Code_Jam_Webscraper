#include<stdlib.h>
#include<string.h>
#include<stdio.h>
#include<string>
#include<iostream>
using namespace std;
int n,m;
string s[1005];
string w[105];
bool u[1005];
bool has[30];
int judge(int p,int t)
{

    int res=0;
    memset(has,0,sizeof(has));
    memset(u,0,sizeof(u));
    int i,j,k;
    for(i=0;i<s[p].size();i++)
        has[s[p][i]-'a']=1;
    bool temp[15 ];
    for(i=0;i<n;i++)
        if(s[i].size()!=s[p].size()) u[i]=1;
    for(i=0;i<26;i++)
    {
        //if(u[p]==1) while(1);
        for(j=0;j<n;j++)
        {
            if(u[j]==0)
            {
                for(k=0;k<s[j].size();k++)
                {
                    if(s[j][k]==w[t][i])
                        break;
                }
                if(k<s[j].size()) break;
            }
        }
        if(j<n)
        {
            if(has[w[t][i]-'a']==0)
            {
                int len=s[p].size();
                res++;
                for(j=0;j<n;j++)
                {
                    if(u[j]) continue;
                    if(s[j].size()!=len)
                    {
                        u[j]=1;
                        continue;
                    }
                    for(k=0;k<len;k++)
                    {
                       if(s[j][k]==w[t][i])
                        break;
                    }
                    if(k<len)
                    {
                        u[j]=1;
                    }
                }
            }
            else
            {
                memset(temp,0,sizeof(temp));
                int len=s[p].size();
                for(j=0;j<s[p].size();j++)
                {
                    if(s[p][j]==w[t][i])
                        temp[j]=1;
                }
                for(j=0;j<n;j++)
                {
                    if(u[j]) continue;
                    if(s[j].size()!=len)
                    {
                        u[j]=1;
                        continue;
                    }
                    for(k=0;k<len;k++)
                    {
                        if((temp[k]&&s[j][k]!=w[t][i])||(temp[k]==0&&s[j][k]==w[t][i]))
                            break;
                    }
                    if(k<len)
                    {
                        u[j]=1;
                    }
                }
            }
        }
    }
    return res;
}
int main()
{
     freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    int i,j,k;
    int T,case_cnt=0;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%d%d",&n,&m);
        for(i=0;i<n;i++) cin>>s[i];
        for(i=0;i<m;i++) cin>>w[i];
        string res;
        printf("Case #%d: ",++case_cnt);
        for(i=0;i<m;i++)
        {
            int cnt=-1;
            for(j=0;j<n;j++)
            {
                int temp=judge(j,i);
                if(temp>cnt)
                {
                    cnt=temp;
                    res=s[j];
                }
            }
            cout<<res;
            if(i<m-1) putchar(' ');
            else putchar('\n');
        }
    }
}
