#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>

#include <algorithm>
#include <set>
#include <map>
#include <queue>

using namespace std;

void process()
{
	int n,k;
	
	scanf("%d %d", &n, &k);
	
	for(int i = 0 ; i < n ; ++i )
	{
		if( !(k&(1<<i)) )
		{
			printf("OFF\n");
			return;
		}
	}
	printf("ON\n");
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
