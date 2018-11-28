#include <cstdio>
#include <iostream>
#include <cstring>
#define MAXN 100
#define MAXL 255
using namespace std;

char word[MAXN+1][MAXL+1];
int len[MAXN+1],cnt[MAXL+1];
char s[MAXL+1];
int k,l,n,d,ans;

int CAL()
{
    int i,pro,ret;
    pro=1;
    ret=0;
    for(i=0;i<l;i++)
    {
        if(s[i]=='+')
        {
            ret=(ret+pro)%10009;
            pro=1;
        }
        else
        {
            pro=(pro*cnt[s[i]])%10009;
        }
    }
    return ret;
}

void DFS(int step,int start)
{
    int i,j;
    if(step==d)
    {
        ans=(ans+CAL())%10009;
        return;
    }
    for(i=0;i<n;i++)
    {
        for(j=0;j<len[i];j++)
        {
            cnt[word[i][j]]++;
        }
        DFS(step+1,start+1);
        for(j=0;j<len[i];j++)
        {
            cnt[word[i][j]]--;
        }
    }
}

int main()
{
    freopen("B-small-attempt1.in","r",stdin);
    freopen("B-small-attempt1.out","w",stdout);
    int c,i,t;
    scanf("%d",&t);
    for(c=0;c<t;c++)
    {
        scanf("%s %d",s,&k);
        l=strlen(s);
        s[l++]='+';
        s[l]='\0';
        scanf("%d",&n);
        for(i=0;i<n;i++)
        {
            scanf("%s",word[i]);
            len[i]=strlen(word[i]);
        }
        printf("Case #%d:",c+1);
        for(d=1;d<=k;d++)
        {
            memset(cnt,0,sizeof(cnt));
            ans=0;
            DFS(0,0);
            printf(" %d",ans);
        }
        printf("\n");
    }
    return 0;
}
