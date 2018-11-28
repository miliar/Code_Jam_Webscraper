#include <stdio.h>
#include <algorithm>
using namespace std;
#define N 900

int n, a[N], b[N];

int main()
{
  	int t, index, s, sm, i;
	scanf("%d", &t);
	for(index = 1; index <= t; index++)
	{
		scanf("%d", &n);
		for(i = 0; i < n; i++)
			scanf("%d", &a[i]);
		for(i = 0; i < n; i++)
			scanf("%d", &b[i]);
  		sort(b, b+n);
   		for(i = 0, sm = 0; i < n; i++)
   			sm += a[i] * b[i];
    	while(next_permutation(b, b+n)) {
    		for(i = 0, s = 0; i < n; i++)
    			s += a[i] * b[i];
   			if(s < sm)
   				sm = s;
    	} 
  		printf("Case #%d: %d\n", index, sm);
	}
}

