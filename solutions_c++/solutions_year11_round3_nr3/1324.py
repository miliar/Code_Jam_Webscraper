#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <memory.h>
#include <string.h>
#include <time.h>

#define N	10000
__int64 a[N];

__int64  gcd(__int64  a, __int64  b)
{
    __int64  c; 

	if(a < b) return gcd(b, a);

    while (b) 
    {
        c  =  b;
        b  =  a % b;
        a  =  c;
    }    
    return a;
}   

void main2()
{
	__int64 i, j, k;
	__int64 n, l, h;
	__int64 f;
	__int64 g;

	scanf("%I64d %I64d %I64d", &n, &l, &h);
	
	f = 1;
	for(i = 0; i < n; i++)
	{
		scanf("%I64d", a + i);
	}
	for(i = l; i <= h; i++)
	{
		for(j = 0; j < n; j++)
		{
			if((i % a[j] != 0) && (a[j] % i != 0)) break;
		}
		if(j >= n) break;
	}
	if(i <= h) {
		printf("%I64d\n", i);
	} else {
		printf("NO\n");
	}
/*
	g = a[0];
	for(i = 1; i < n; i++) g = gcd(g, a[i]);
	if(g >= l && g <= h) { printf("I64d\n", f); return; }

	if(f >= l && f <= h) {
		printf("I64d\n", f);
	} else {
		printf("NO\n");
	}
	*/
}

//======================================================
int main()
{
	int t, T;

	//freopen("C.txt", "r", stdin);

	freopen("C-small.in", "r", stdin);
	freopen("C-small.out.txt", "w", stdout);
	//freopen("C-large.in", "r", stdin);
	//freopen("C-large.out.txt", "w", stdout);

	scanf("%d", &T);
	for(t = 0; t < T; t++)
	{
		printf("Case #%d: ", t+1);
		main2();
	}
	return 0;
}