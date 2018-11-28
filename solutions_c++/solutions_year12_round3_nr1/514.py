#include <cstdio>
#include <iostream>
#include <vector>
#define MAXN 1000
using namespace std;

vector<int> V[ MAXN + 10 ];
int In[ MAXN + 10 ];
int root, visited[ MAXN + 10 ];
bool ans;

void DFS( int m )
{
	visited[ m ] = root;
	for(int i=0; i<int(V[m].size())  &&  ! ans; i++)
		if( visited[ V[m][i] ] == root )
			ans = true;
		else
			DFS( V[m][i] );
}


int main()
{
	int ilz, n;
	scanf("%i", &ilz);
	for (int xz = 1; xz <= ilz; xz++)
	{
		scanf("%i", &n);
		
		for(int i=0; i<=n; i++)
		{
			V[i].clear();
			In[i] = 0;
			visited[i] = -1;
		}
		ans = false;
		
		for(int i=0, m; i<n; i++)
		{
			scanf("%i", &m);
			for(int j=0, a; j<m; j++)
			{
				scanf("%i", &a);
				a--;
				V[i].push_back(a);
				In[a]++;
			}
		}
		for(int i=0; i<n  &&  ! ans; i++)
			if( In[i] == 0 )
			{
				root = i;
				DFS( i );
			}
		printf("Case #%i: ", xz);
		if( ans )
			printf("Yes\n");
		else
			printf("No\n");
	}
	return 0;
}

