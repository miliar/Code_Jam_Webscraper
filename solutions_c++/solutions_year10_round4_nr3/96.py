#include<stdio.h>
#include<set>
using namespace std;

typedef set<pair<int,int> > myset;
int answer;
myset bst,nbst;

bool check(int x,int y)
{
	return bst.find(make_pair(x,y))!=bst.end();
}

void solve()
{
	myset::iterator it; int x,y;
	for(answer=0;!bst.empty();answer++)
	{
		for(it=bst.begin();it!=bst.end();it++)
		{
			x=it->first;
			y=it->second;
			if(check(x,y-1)||check(x-1,y))
				nbst.insert(make_pair(x,y));
			if(check(x+1,y-1))
				nbst.insert(make_pair(x+1,y));
			if(check(x-1,y+1))
				nbst.insert(make_pair(x,y+1));
		}
		bst.clear();
		bst=nbst;
		nbst.clear();
	}
}

void input()
{
	int n,x1,y1,x2,y2,i,j;
	scanf("%d",&n);
	while(n--)
	{
		scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
		for(i=x1;i<=x2;i++)
		{
			for(j=y1;j<=y2;j++)
			{
				bst.insert(make_pair(i,j));
			}
		}
	}
}

int main()
{
	int T,S;
	scanf("%d",&S);
	for(T=1;T<=S;T++)
	{
		input();
		solve();
		printf("Case #%d: %d\n",T,answer);
	}
	return 0;
}
