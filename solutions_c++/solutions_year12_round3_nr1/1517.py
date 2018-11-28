# include <stdio.h>
# include <string.h>
# include <string>
# include <iostream>
# include <algorithm>
# include <vector>
# include <set>
# include <cmath>
# include <queue>
using namespace std;

vector < int > v [ 1001 ];
int s,d,vis[55][55], last[55];

bool bfs (int a)
{
	queue< int > q ;
	q.push(s);
	bool f=0 ;
	while(!q.empty())
	{
		int cur = q.front() ;
		q.pop() ;
		if ( cur == d )
		{
			f=1;
			break;
		}
		for ( int i=0 ; i<v[cur].size() ; i++ )
		{
			if ( vis[cur] [ v[cur][i] ]==0 )
			{
				last[v[cur][i]]=cur ;
				vis[ cur ][ v[cur][i] ] = 1 ;
				q.push( v[cur][i] ) ;
			}
		}
	}
	if ( f )
	{
		if ( a == 1 )
		{
			memset(vis,0,sizeof vis);
			int k = last[d] , kk = d ;
			while( k != -1 )
			{
				vis[k][kk]=1 ;
				kk=k ;
				k = last[k] ;
			}
		}
		return true ;
	}
	return false ;
}

int main(void) 
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int tc ;
	cin >> tc ;
	for ( int t=1 ; t<=tc ; t++ )
	{
		cout << "Case #" << t << ": ";
		int n , m , tmp ;
		cin >> n ;
		for ( int i=0 ; i<n ; i++ )
			v[i].clear() ;
		for ( int i=0 ; i<n ; i++ )
		{
			cin >> m ;
			for ( int j=0 ; j<m ; j++ )
			{
				cin >> tmp ;
				tmp-- ;
				v[i].push_back(tmp);
			}
		}
		bool z=0 ;
		for ( int i=0 ; i<n && !z ; i++ )
		{
			for ( int j=0 ; j<n && !z ; j++ )
			{
				if ( i==j )	continue ;
				s = i ;
				d = j ;
				memset(vis,0,sizeof vis);
				memset(last,-1,sizeof last);
				if ( bfs(1) )
				{
					if ( bfs(2) )
					{
						z=1 ;
						printf("Yes\n");
					}
				}
			}
		}
		if ( !z )	printf("No\n");
	}
	//while(1);
	return 0;
}