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

int n, a[2000], b[2000];

void process()
{
	scanf("%d",&n);
	for( int i = 0 ;  i < n ; ++i )
	{
		scanf("%d%d", a+i, b+i);
	}
	
	int count = 0;
	for( int i = 0 ; i < n ; ++i )
	{
		for( int j = i+1 ; j < n ; ++j )
		{
			if( (a[i]-a[j])*(b[i]-b[j]) < 0 )
			{
				count++;
			}
		}
	}
	
	printf("%d\n", count);
}

bool read()
{
}


int main()
{
	int c; scanf("%d", &c);
	int t = 1;
	while( c-- )
	{
		printf("Case #%d: ", t++);
		process();
	}	
	return 0;
}
