
// (c) Alvaro Salmador 2011

#pragma warning(disable : 4996)
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <algorithm>
/*#include <string>
#include <list>
#include <vector>
#include <map>*/

using namespace std;


#undef M_PI
#define M_PI 3.14159265358979323846  
const double SQRT2 = sqrt(2.0);
const double Pi = M_PI;
//typedef long long ll;
//typedef unsigned long long ull;


int N=0, C[1000];



bool get_input()
{
	static int T = -1;
	
	if (T<0)
		scanf("%d", &T);
	
	if (T>0)
	{
		--T;

		if (scanf("%d", &N)!=1)
			return false;

		while(fgetc(stdin)!='\n') ;

		int i, c;
		for(i=0; i<N; ++i)
		{
			c = fgetc(stdin);
			char s[16], *p=s;
			while(c!=' ' && c!='\n' && c!=EOF) {
				*(p++)=(char)c;
				c = fgetc(stdin);
			}
			*p = 0;

			C[i] = atoi(s);
		}

		return true;
	}
	else
		return false;
}

int cmp(const void * a, const void * b)
{
  return ( *(int*)a - *(int*)b );
}


int solve(int xor1=0, int xor2=0, int sum1=0, int sum2=0, int n=0, int n1=0)
{
	if (n==N) {
		if (xor1==xor2)
			return (sum1>sum2) ? sum1 : sum2;
		else
			return -1;
	}
	else if (n==N-1) //check for empty pile
	{
		if (n1==n)
			return solve(xor1, xor2^C[n], sum1, sum2+C[n], n+1, n1);
		else if (n1==0)
			return solve(xor1^C[n], xor2, sum1+C[n], sum2, n+1, n1+1);
	}

	int r1=solve(xor1^C[n], xor2, sum1+C[n], sum2, n+1, n1+1);
	int r2=solve(xor1, xor2^C[n], sum1, sum2+C[n], n+1, n1);

	return (r1>r2) ? r1 : r2;
}

int main()
{

	for(int ncase=1; get_input(); ++ncase)
	{
		//fprintf(stderr, "\nCase #%d\n", ncase); fflush(stderr);
		printf("Case #%d: ", ncase);

		//qsort(C, N, sizeof(int), cmp);

		/*int i;
		for(i=0; i<N; ++i)
			fprintf(stderr, "%d ", C[i]);*/

		int res = solve();

		if (res<0)
			printf("NO\n");
		else 
			printf("%d\n", res);
	}

	return 0;
}