#pragma warning(disable:4786)
#include<iostream>
#include<assert.h>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<functional>
#include<string>
#include<cstring>
#include<cstdlib>
#include<queue>
#include<utility>
#include<fstream>
#include<sstream>
#include<math.h>
#include<stack>
using namespace std;

#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define MIN(a,b) ((a) < (b) ? (a) : (b)
#define ABS(X) ((X) < 0 ? (-(X)) : (X))
#define S(X) ((X)*(X))

typedef pair<int,int> PII;
typedef __int64 LL;

//int dr[]={0,-1,-1,-1,0,1,1,1};
//int dc[]={-1,-1,0,1,1,1,0,-1};

typedef pair<string,int> PSI;

map<string,int> mnode[25000];
int glbl,cnt;

void push(string X)
{
	int sz,i,now;

	sz=X.size();
	for(i=0;i<sz;i++)
		if(X[i]=='/')
			X[i]=' ';

	istringstream iS(X);
	string A;
	now = 0;

	while(iS>>A)
	{
		if(mnode[now].find(A)==mnode[now].end())
		{
			cnt++;
			glbl++;
			mnode[now][A]=glbl;
			mnode[glbl].clear();
			now=glbl;
		}
		else
			now = mnode[now][A];
	}
}			

int main()
{
//	freopen("A-small-attempt0.in","r",stdin);
//	freopen("A-small-attempt20.out","w",stdout);
//	freopen("A-small-attempt3.in","r",stdin);freopen("A-small-attempt3.out","w",stdout);
//	freopen("A-small-attempt2.in","r",stdin);freopen("A-small-attempt2.out","w",stdout);
	freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);
	
	int T,ks;
	int n,m,i,N;
	char word[1000];

	scanf("%d",&T);
	for(ks=1;ks<=T;ks++)
	{
		mnode[0].clear();
		glbl=0;

		scanf("%d%d",&n,&m);
		for(i=0;i<n;i++)
		{
			scanf("%s",word);
			push(word);
		}

		cnt=0;
		for(i=0;i<m;i++)
		{
			scanf("%s",word);
			push(word);
		}

		printf("Case #%d: %d\n",ks,cnt);
	}

	return 0;
}