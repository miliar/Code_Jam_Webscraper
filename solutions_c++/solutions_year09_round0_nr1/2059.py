#include<stdio.h>
#include<vector>
using namespace std;

int l,d,n;

struct trie
{
    bool ma[510];
    trie* c[26];
}mem[100010],*root;
int pp=0;
char s[550],t[20];
vector<char> v[20];
bool us[20][30];
int ca;
__int64 ans;

trie* cr()
{
    int i;
    for(i=0;i<510;i++)
        mem[pp].ma[i]=false;
    for(i=0;i<26;i++)
        mem[pp].c[i]=NULL;
    return &mem[pp++];
}

void ins(trie *root,char *s)
{
    trie *p=root;
    while(*s)
    {
        if(p->c[*s-'a']==NULL)
            p->c[*s-'a']=cr();
        p=p->c[*s-'a'];
        s++;
    }
    for(int i=0;i<510;i++)
        p->ma[i]=true;
}

int find(trie *root,char *s,int e)
{
    trie *p=root;
    while(*s)
    {
        if(p->c[*s-'a']==NULL)
            return 0;
        p=p->c[*s-'a'];
        s++;
    }
    if(p->ma[e])
    {
        p->ma[e]=0;
        return 1;
    }
    return 0;
}

void init()
{
    ca=1;
    pp=0;
    ans=0;
    root=cr();
    for(int i=0;i<20;i++)
    {
        for(int j=0;j<26;j++)
            us[i][j]=false;
        v[i].clear();
    }
}


int reads(char *s,int p)
{
    while(!('a'<=s[p]&&s[p]<='z'||s[p]=='(') )
        p++;
    if('a'<=s[p]&&s[p]<='z')
        return p+1;
    while(s[p]!=')')
        p++;
    return p+1;
}

void dfs(int p,int ca,trie* root)
{
    if(p==l)
    {//puts(t);
        if(root->ma[ca])
        {
            root->ma[ca]=false;
            ans++;
        }
        return;
    }
    int i,n=v[p].size();
    for(i=0;i<n;i++)
    {
        t[p]=v[p][i];
        if(root->c[t[p]-'a']!=NULL)
            dfs(p+1,ca,root->c[t[p]-'a']);
    }
}

int main()
{
 //   freopen("A-large.in","r",stdin);
 //   freopen("out.txt","w",stdout);
    scanf("%d%d%d",&l,&d,&n);
    int i,j;
    init();
    for(i=0;i<d;i++)
    {
        scanf("%s",s);
        ins(root,s);
        for(j=0;j<l;j++)
            us[j][s[j]-'a']=true;
    }
    for(ca=1;ca<=n;ca++)
    {
        ans=0;
        scanf("%s",s);
        int tmp=0;
        for(i=0;i<l;i++)
        {   
            v[i].clear();
            int p=reads(s,tmp);
            for(j=tmp;j<p;j++)
            {
                if('a'<=s[j]&&s[j]<='z'&&us[i][s[j]-'a'])
                    v[i].push_back(s[j]);
            }
            tmp=p;
        }
        t[l]='\0';
        dfs(0,ca,root);
        printf("Case #%d: %I64d\n",ca,ans);
    }
    
    return 0;
}