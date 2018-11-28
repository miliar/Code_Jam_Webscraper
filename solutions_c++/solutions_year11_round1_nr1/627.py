#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <deque>

using namespace std;

int MDC(int a, int b){
  int resto;

  while(b != 0){
    resto = a % b;
    a = b;
    b = resto;
  }

  return a;
}

int main(int argc, char** argv)
{
	int T, pd, pg, m;
	long long n;
	bool p;
	
	scanf("%d", &T);
	
	for(int i = 1; i <= T; i++)
	{
		scanf("%lld %d %d", &n, &pd, &pg);
		
		if(pg == 100)
		{
			if(pd == 100) p = true;
			else p = false;
		}
		
		else if(pg == 0)
		{
			if(pd == 0) p = true;
			else p = false;
		}
		
		else if(n >= 100)
		{
			p = true;
		}
		else
		{
			m = MDC(pd, 100);
			if(n >= (100/m))
				p = true;
			else
				p = false;
		}
		
		printf("Case #%d: ", i);
		if(p) printf("Possible");
		else printf("Broken");
		
		if(i != T) putchar('\n');
	}
	
	return 0;
}
