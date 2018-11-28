#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std ;

int n,l,q;
char str[5005][20];
//       qry  ltr canornot
bool psb[505][20][30];
char temps[1005];
int trie[80000][30];
bool vis[80000];
int best[80000];
int nn;
int qi;

void push(int ind)
{
    int cur=0;
    int c,c2;
    for (c=0;c<l;c++)
    {
        if (trie[cur][str[ind][c]-'a']!=-1)cur=trie[cur][str[ind][c]-'a'];
        else
        {
            cur=trie[cur][str[ind][c]-'a']=nn;
            nn++;
        }
    }
    vis[cur]=1;
    return;
}
int solve(int node,int ind)
{
    if (ind==l)return 1;
    if (best[node]!=-1)return best[node];
    int c,c2;
    int ret=0;
    for (c=0;c<26;c++)
    if (psb[qi][ind][c]&&trie[node][c]!=-1)
    ret+=solve(trie[node][c],ind+1);
    return best[node]=ret;
}

int main()
{
    FILE *in=fopen("aln.in","r");
    freopen("aln.out","w",stdout);
    int c,c2;
    fscanf(in,"%d%d%d",&l,&n,&q);
    for (c=0;c<n;c++)fscanf(in,"%s",str[c]);
    memset(psb,0,sizeof(psb));
    for (c=0;c<q;c++)
    {
        fscanf(in,"%s",temps);
        int cnt=0;
        for (c2=0;c2<strlen(temps);c2++)
        {
            if (isalpha(temps[c2]))psb[c][cnt][temps[c2]-'a']=1;
            else
            {
                for (c2++;temps[c2]!=')';c2++)
                psb[c][cnt][temps[c2]-'a']=1;
            }
            cnt++;
        }
    }
    memset(trie,-1,sizeof(trie));
    memset(vis,0,sizeof(vis));
    nn=1;
    for (c=0;c<n;c++)push(c);
    for (c=0;c<q;c++)
    {
        memset(best,-1,sizeof(best));
        qi=c;
        int ret=solve(0,0);
        printf("Case #%d: %d\n",c+1,ret);
    }
//    system("pause");
    return 0;
}
