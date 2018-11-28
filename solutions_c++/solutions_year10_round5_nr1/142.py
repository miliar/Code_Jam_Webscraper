#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#include<list>
#include<queue>
#include<map>
#include<algorithm>
using namespace std;

#define MAX 1000000

int csK, csN;
int D, N, nP, V[16], P[131072], ans, ten;
int _ten[8] = {1, 10, 100, 1000, 10000, 100000, 1000000};
char isp[1048576];

inline void makePrime()
{
       int i, j, t;
       memset(isp, 1, sizeof(isp));
       nP = 1;
       P[0] = 2;
       for(i = 3; i <= MAX; i += 2)
       {
               if(!isp[i]) continue;
               t = i;
               P[nP++] = t;
	       if(t < 1000)
	               for(j = t*t; j < MAX; j += t) isp[j] = 0;
       }
       P[nP] = MAX + 1;
}

inline void extGCD(long long a, long long b, long long *x, long long *y)
{
	if(a%b == 0) *x = 0, *y = 1;
	else
	{
		long long nx, ny;
		extGCD(b, a%b, &nx, &ny);
		*x = ny;
		*y = nx - ny*(a/b);
	}
}

inline int xGCD(int n, int p)
{
	long long a, b;
	if(n == 0) return 0;
	extGCD(n, p, &a, &b);
	return (a%p+p) % p;
}

int main()
{
	int i, j, k, m, t, mx;
	long long a, b, p;
/*	while(scanf("%d %d", &i, &j) == 2)
	{
		k = xGCD(i, j);
		printf("\t%d\n", k);
	}*/
	makePrime();
	scanf("%d", &csN);
	for(csK = 1; csK <= csN; ++csK)
	{
		scanf("%d %d", &D, &N);
		ten = _ten[D];
		for(mx = i = 0; i < N; ++i)
		{
			scanf("%d", &V[i]);
			if(V[i] > mx) mx = V[i];
		}
/*		fprintf(stderr, "IN: %d %d\n\t", D, N);
		for(i = 0; i < N; ++i) fprintf(stderr, "%d ", V[i]);
		fprintf(stderr, "\n");*/
		if(N == 1)
		{
			printf("Case #%d: I don't know.\n", csK);
			fflush(stdout);
			continue;
		}
		else if(N == 2 && V[0] == V[1])
		{
			printf("Case #%d: %d\n", csK, V[0]);
			fflush(stdout);
			continue;
		}
		for(i = 0; P[i] <= mx; ++i) ;
		ans = -1;
		for(; P[i] <= ten && ans != -2; ++i)
		{
			p = P[i];
			if(N == 2)
			{
				for(a = 0; a < p; ++a)
				{
					b = (((V[1]-a*V[0])%p)+p) % p;
			//		fprintf(stderr, "p = %I64d, a = %I64d, b = %I64d, v = %d\n",
			//				p, a, b, (a*V[1]+b) % p);
					if(ans == -1) ans = (a*V[1]+b) % p;
					else if(ans != (a*V[1]+b)%p)
					{
						ans = -2;
						break;
					}
				}
			}
			else
			{
				a = ((((long long)V[2]-V[1])*xGCD((V[1]-V[0]+p)%p, p))%p + p) % p;
	//			fprintf(stderr, "p = %I64d, xGCD = %d, a = %I64d\n", p, xGCD((V[1]-V[0]+p)%p, p), a);
				b = ((V[1]-a*V[0])%p+p) % p;
				for(j = 2; j < N; ++j)
					if(V[j] != (a*V[j-1]+b)%p) break;
				if(j == N)
				{
					t = (a*V[N-1]+b) % p;
			//		fprintf(stderr, "p = %I64d, a = %I64d, b = %I64d, v = %d\n",
			//				p, a, b, t);
					if(ans == -1) ans = t;
					else if(ans != t) ans = -2;
				}
			}
		}
		if(ans < 0)
			printf("Case #%d: I don't know.\n", csK);
		else
			printf("Case #%d: %d\n", csK, ans);
		fflush(stdout);
	}
}




