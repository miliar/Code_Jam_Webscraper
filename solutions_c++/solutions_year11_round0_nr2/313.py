#include <cstdio>
#include <iostream>
#include <cstring>
#include <string>
#include <algorithm>
#define MAXC 36
#define MAXD 28
#define MAXN 100
#define SIZE 3
using namespace std;

string ans;
char com[MAXC+1][SIZE+1],opp[MAXD+1][SIZE+1];
char str[MAXN+1];
int c,d,n;

void process()
{
    int i,j,k,l,flag;
    ans="";
    for(k=0;k<n;k++)
    {
        ans+=str[k];
        flag=0;
        for(i=0;i<c;i++)
        {
            if(((ans[ans.length()-1]==com[i][0])&&(ans[ans.length()-2]==com[i][1]))||((ans[ans.length()-1]==com[i][1])&&(ans[ans.length()-2]==com[i][0])))
            {
                flag=1;
                break;
            }
        }
        if(flag==1)
        {
            ans=ans.substr(0,ans.length()-2)+com[i][2];
            continue;
        }
        flag=0;
        for(l=0;l<ans.length()-1;l++)
        {
            for(j=0;j<d;j++)
            {
                if(((ans[ans.length()-1]==opp[j][0])&&(ans[l]==opp[j][1]))||((ans[ans.length()-1]==opp[j][1])&&(ans[l]==opp[j][0])))
                {
                    flag=1;
                    break;
                }
            }
            if(flag==1)
            {
                break;
            }
        }
        if(flag==1)
        {
            ans="";
            continue;
        }
    }
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int i,j,l,p,t;
    scanf("%d",&t);
    for(p=0;p<t;p++)
    {
        scanf("%d",&c);
        for(i=0;i<c;i++)
        {
            scanf("%s",com[i]);
        }
        scanf("%d",&d);
        for(j=0;j<d;j++)
        {
            scanf("%s",opp[j]);
        }
        scanf("%d",&n);
        scanf("%s",str);
        process();
        printf("Case #%d: [",p+1);
        for(l=0;l<ans.length();l++)
        {
            if(l==0)
            {
                printf("%c",ans[l]);
            }
            else
            {
                printf(", %c",ans[l]);
            }
        }
        printf("]\n");
    }
    return 0;
}
