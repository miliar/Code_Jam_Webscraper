#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>

#include <algorithm>
#include <set>
#include <map>
#include <queue>

using namespace std;

#include <iostream>
#define DB(x) cout << #x " == " << (x) << endl

int r,k,n, g[1050], s, to[1050], ve[1050];
bool mark[1050];

void process()
{
	int total = 0;
	int vez = 0;
	int ind = 0;
	
	if( s <= k ) { printf("%d\n", s*r); return; }
	
	int at;
	while( vez < r )
	{
		if( mark[ind] )
		{
			int ciclos = (r-vez)/(vez-ve[ind]);
			vez += ciclos*(vez-ve[ind]);
			total += ciclos*(total-to[ind]);
			
			if( vez == r ) break;
		}
		mark[ind] = true;
		to[ind] = total;
		ve[ind] = vez;
		at = g[ind];
		while( at <= k )
		{
			ind++;
			if( ind == n ) ind = 0;
			at += g[ind];
		}
		
		total += at - g[ind];
		vez++;
	}
	
	printf("%d\n", total);
}

bool read()
{
	scanf("%d %d %d", &r, &k, &n);
	
	s = 0;
	for( int i = 0 ; i < n ; ++i )
	{
		scanf("%d", g+i);
		s += g[i];
	}
	memset(mark,false,sizeof(mark));
	return true;
}


int main()
{
	int c; scanf("%d", &c);
	int t = 1;
	while( c-- )
	{
		printf("Case #%d: ", t++);
		read();
		process();
	}	
	return 0;
}
