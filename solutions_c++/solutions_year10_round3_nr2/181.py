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

void process()
{
	long long l,p,c;
	int res = 0;
	scanf("%lld%lld%lld", &l, &p, &c);
	
	int k = 0;
	while( l < p )
	{
		l = l*c;
		k++;
	}
	k--;
	while( k )
	{
		res++;
		k /= 2;
	}
	
	printf("%d\n", res);
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
