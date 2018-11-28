#include <stdio.h>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int T,na,nb;
vector<int> ma[2001][2];
vector<int> v[2001][2];

int gimme(string s)
{
    int cont=s[4]-'0';
    cont+=(s[3]-'0')*10;
    cont+=(s[1]-'0')*60;
    cont+=(s[0]-'0')*600;
    return cont;
}

void rec(int no,int r,int id)
{
    v[no][r][id]=1;
    for(int i=ma[no][r][id]+T;i<=24*60;i++)
    {
        if(ma[i][(r+1)%2].size()!=0)
        {
            for(int k=0;k<ma[i][(r+1)%2].size();k++)
            {
                if(!v[i][(r+1)%2][k])
                {
                    rec(i,(r+1)%2,k);
                    return;
                }
            }
        }
    }
}   

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int N;
    char s1[10],s2[10];
    int a,b;
    int f[2];
    scanf("%d",&N);
    for(int I=0;I<N;I++)
    {
        for(int i=0;i<2001;i++)for(int k=0;k<2;k++)ma[i][k].clear();
        for(int i=0;i<2001;i++)for(int k=0;k<2;k++)v[i][k].clear();
        f[0]=f[1]=0;
        scanf("%d%d%d",&T,&na,&nb);
        for(int i=0;i<na;i++)
        {
            scanf("%s%s",s1,s2);
            a=gimme(s1);
            b=gimme(s2);
            ma[a][0].push_back(b);
            v[a][0].push_back(0);
        }
        for(int i=0;i<nb;i++)
        {
            scanf("%s%s",s1,s2);
            a=gimme(s1);
            b=gimme(s2);
            ma[a][1].push_back(b);
            v[a][1].push_back(0);
        }
        for(int i=0;i<=24*60;i++)
        {
            for(int k=0;k<2;k++)
            {
                if(ma[i][k].size()!=0)
                {
                    for(int j=0;j<ma[i][k].size();j++)
                    {
                        if(!v[i][k][j])
                        {
                            f[k]++;
                            rec(i,k,j);
                        }
                    }
                }
            }
        }
        printf("Case #%d: %d %d\n",I+1,f[0],f[1]);
    }
}
