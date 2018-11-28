#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;

struct node
{
    int to[26];bool bad;
};

node trie[15*5000*24];
int size=1;
int l,d,n,idx;
char s[500000];
string tmp[20];

void insert()
{
    int i,p,j,x;char s[20];
    for(i=0;i<d;i++)
    {
        scanf("%s",s);
        for(p=1,j=0;s[j]!=0;j++)
        {
            x=s[j]-'a';
            if(trie[p].to[x]==0) trie[p].to[x]=++size;
            p=trie[p].to[x];
        }
        trie[p].bad=true;
    }
}

int dfs(int m,int p)
{
    int i;
    if(m==idx) return 1;
    int sum=0;
    for(i=0;i<tmp[m].length();i++)
    {
		//cout<<tmp[m][i]<<endl;
        if(trie[p].to[tmp[m][i]-'a'])
            sum+=dfs(m+1,trie[p].to[tmp[m][i]-'a']);
    }
    return sum;
}

int getnum()
{
    int i;
    return dfs(0,1);
}

int main()
{
	FILE *fp=freopen("out.txt","w",stdout);
    scanf("%d%d%d",&l,&d,&n);
    insert();
    int i;
    for(i=1;i<=n;i++)
    {
        scanf("%s",s);
        int j=0;bool newword=true;
		idx=0;
        while(s[j]!=0)
        {
            if(s[j]=='(') 
                newword=false;
            if(s[j]>='a' && s[j]<='z')
            {
                tmp[idx].push_back(s[j]);
                if(newword) idx++;
            }
            if(s[j]==')') newword=true,idx++;
            j++;
        }
        printf("Case #%d: %d\n",i,getnum());
		for(j=0;j<=idx;j++) tmp[j].clear();
    }
    return 0;
}