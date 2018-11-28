#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<vector>
#include<cmath>
using namespace std;

vector<int> V;
char s[150];
int T;

bool check(char* s)
{
	long long ret=0;
	for(int i=0;i<strlen(s);i++)
	{
		ret<<=1;
		ret+=s[i]-'0';
	}
	long long t=sqrt(ret);
	if(t*t==ret||(t+1)*(t+1)==ret)
		return true;
	return false;
}

char* dfs(char* s,int p)
{
	if(p==V.size())
		if(check(s))
			return s;
		else
			return 0;
	for(int i=0;i<2;i++)
	{
		s[V[p]]=i+'0';
		if(dfs(s,p+1))
			return s;
	}
	return 0;
}

int main()
{
	freopen("D-small-attempt0.in","r",stdin);
	freopen("D-small.out","w",stdout);
	scanf("%d",&T);
	for(int test=1;test<=T;test++)
	{
		V.clear();
		scanf("%s",s);
		for(int i=0;i<strlen(s);i++)
			if(s[i]=='?')
				V.push_back(i);
		printf("Case #%d: %s\n",test,dfs(s,0));
	}
	return 0;
}

