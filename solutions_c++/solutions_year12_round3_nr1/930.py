#include <stdio.h>
#include <queue>
#include <map>
#include <set>
#include <vector>
#include <algorithm>
using namespace std;

typedef map<long long, int>  MAP;
map<long long, int> M;

long long X[500];

bool multiple( int head, vector<int> v[1002] )
{
	int from[1002];
	queue<int> q;
	int i;
	for(i=0; i<1002; ++i)
	{
		from[i]=-1;
	}
	for(i=0; i<v[head].size(); ++i)
	{
		q.push((1024*v[head][i])+head);
	}
	while( !q.empty() )
	{
		int fn = q.front();
		int fr = fn%1024;
		int nd = fn/1024;
		q.pop();
		if( from[nd] != -1 && from[nd]!=fr )
			return true;
		if( from[nd] != -1 )
			continue;
		from[nd] = fr;
		for(i=0; i<v[nd].size(); ++i)
		{
			q.push(1024*v[nd][i]+nd);
		}
	}
	return false;
}

int main(int argc, char* argv[])
{

	int N;
	scanf("%d",&N);
	char ch[1025];
	gets(ch);
	for(int I=0; I<N; ++I)
	{
		vector<int> V[1002];
		int n,i,j;
		scanf("%d",&n);
		for(i=0; i<n; ++i)
		{
			int m,x;
			scanf("%d",&m);
			for(j=0; j<m; ++j)
			{
				scanf("%d",&x);
				V[i+1].push_back(x);
			}
		}

		printf("Case #%d: ", I+1);
		for(i=0; i<n; ++i)
		{
			if( multiple(i+1,V) )
			{
				break;
			}
		}
		if(i==n)
		{
			printf("No\n");
		}
		else
			printf("Yes\n");
	}
	return 0;
}


