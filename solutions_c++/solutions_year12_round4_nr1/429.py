#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <string>

using namespace std;

#define MAXN  11000

int dis[MAXN], len[MAXN], far[MAXN];
int N, D;

struct NODE
{
    int index, len;
};

queue<NODE> que;

void init()
{
    while( !que.empty() )   que.pop();
    memset(far, 0, sizeof(far));
}

int main() 
{
	int datacase, t = 0, tmpfar;
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf( "%d", &datacase );
	while( datacase-- ) 
	{
		init();
		scanf( "%d", &N );
		for( int i = 0; i < N; i++ )
			scanf( "%d%d", &dis[i], &len[i] );
		scanf("%d", &D );
		
	    bool flag = true;

	    NODE start;
	    start.index = 0;
	    start.len = dis[0];
	    que.push(start);
	
	    while( !que.empty() )
		{
	    	NODE now = que.front();
	        que.pop();
	        if( D - dis[ now.index ] <= now.len )
			{
	            flag = false;  
				break;
	        }
	
	        for(int i=now.index+1; i<N; ++i)
			{
	        	if( dis[i] > dis[now.index] + now.len ) 
					break;
	        	NODE next;
	        	next.index = i;
	        	next.len = min( dis[i] - dis[now.index], len[i] );
	            tmpfar = dis[i] + next.len;
	            if( far[i] < tmpfar )
				{
	            	far[i] = tmpfar;
	            	que.push(next);
	            }
	        }
	    }
		printf("Case #%d: ", ++t );	    
		if( !flag )
			printf("YES\n");
		else
			printf("NO\n");
	}
	return 0;
}
