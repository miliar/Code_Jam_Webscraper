#include<cstdio>
#include<algorithm>
#include<queue>
#include<set>
#include<utility>
#include<list>
#include<vector>
using namespace std;
#define PB push_back
#define ST first
#define ND second
#define MAXN 1000
#define OO (1<<20)
char s[MAXN+1];
char c[MAXN+1];
int k;
vector<int> p;
bool dbg=0;
void readCase()
{
	scanf("%d%s",&k,s);
	if(dbg)printf("s:%s\n",s);
}

void code()
{
	int i=0;
	for(;s[i]!='\0';i++)
		c[i]=s[(i/k)*k+p[i%k]];
	c[i]='\0';
	if(dbg)printf("c:%s\n",c);
}
int len()
{
	int l=1;
	for(int i=1;c[i]!='\0';i++)
	{
		if(c[i]!=c[i-1])l++;
	}
	if(dbg)printf("len():%d\n",l);
	return l;
}

void computeCase(int cas)
{
	p.clear();
	for(int i=0;i<k;i++)
		p.PB(i);
	int res=OO;
	do
	{
		code();
		res=min(res,len());
	}
	while(next_permutation(p.begin(),p.end()));
	printf("Case #%d: %d\n",cas,res);
}
int main()
{
	int n;
	scanf("%d",&n);
	for(int i=1;i<=n;i++)
	{
		readCase();
		computeCase(i);
	}
	return 0;
}
