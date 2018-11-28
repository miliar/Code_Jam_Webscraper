#include <cstdio>
#include <iostream>
#include <cstring>
#define MAXD 5000
#define MAXL 15
#define MAXC 26
using namespace std;

char word[MAXD+1][MAXL+1],mark[MAXL+1][MAXC+1];
char line[1<<MAXL];
int l,d,n;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int i,j,k,len,cnt;
    gets(line);
    sscanf(line,"%d %d %d",&l,&d,&n);
    for(i=0;i<d;i++)
    {
        gets(word[i]);
    }
    for(k=0;k<n;k++)
    {
        memset(mark,0,sizeof(mark));
        gets(line);
        len=strlen(line);
        j=0;
        for(i=0;i<len;i++)
        {
            if(line[i]=='(')
            {
                for(i++;line[i]!=')';i++)
                {
                    mark[j][line[i]-'a']=1;
                }
                j++;
            }
            else
            {
                mark[j++][line[i]-'a']=1;
            }
        }
        cnt=0;
        for(i=0;i<d;i++)
        {
            for(j=0;j<l;j++)
            {
                if(mark[j][word[i][j]-'a']==0)
                {
                    break;
                }
            }
            if(j>=l)
            {
                cnt++;
            }
        }
        printf("Case #%d: %d\n",k+1,cnt);
    }
    return 0;
}
