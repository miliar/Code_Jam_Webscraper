#include <cstdio>
#include <iostream>
#include <string>
#include <cstring>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <cstring>
#include <queue>
#include <sstream>

using namespace std;

typedef long long ll;
typedef vector <int> vi;
typedef pair<int, int> pii;

int T;

int pd, pg;
ll n;

bool isPrime(int x)
{
	if (x == 1) return false;
	for (int i = 2; i*i <= x; ++i)
		if ( (x % i) == 0 )
			return false;
	return true;
}

int gcd (int a, int b) 
{
	return b ? gcd (b, a % b) : a;
}

int main()
{
  scanf("%d", &T);
  for (int t = 0; t < T; ++t)
  {
    cin >> n >> pd >> pg;
    if (pg == 100)
    {
    	if (pd != 100)
    		printf("Case #%d: Broken\n", t+1);
    	else
    	  printf("Case #%d: Possible\n", t+1);
    	continue;
    }
    if (pg == 0)
    {
    	if (pd != 0)
    		printf("Case #%d: Broken\n", t+1);
    	else
    	  printf("Case #%d: Possible\n", t+1);
    	continue;
    }
    int x = gcd( 100, pd );

    int y = 100 / x;
    bool b = false;
    if (pd == 0 || pd == 100 || y <= n ) b = true;
    if (!b)
	  	printf("Case #%d: Broken\n", t+1);
	  else
	  	printf("Case #%d: Possible\n", t+1);
  }
  return 0;
}