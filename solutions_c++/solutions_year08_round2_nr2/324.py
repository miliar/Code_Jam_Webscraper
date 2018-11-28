#include <stdio.h>
#include <math.h>
#include <algorithm>
#include <vector>
#include <string>
#include <map>

using namespace std;

#define nul(a) memset(a,0,sizeof(a))
int s[2000];
bool use[2000];
int gcd(int a,int b){
	while (a && b){
		if (a > b)
			a %= b;
		else
			b %= a;
	}
	return a + b;
}
int maxPrime(int a){
	if (a==1)
		return 0;
	for (int i = 2; i < a; i++){
		while (i < a && a % i == 0)
			a /= i;
	}
	return a;
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	scanf("%d", &t);
	for (int ti = 1; ti <= t; ti++){
		int a, b, p;
		scanf("%d%d%d", &a, &b, &p);
		nul(use);
		int res=0;
		for (int i = a; i <= b; i++)
			if (!use[i]){
				res++;
				int u = 1;
				s[0]=i;
				for (int d = 0; d < u; d++){
					int v = s[d];
					for (int j = a; j <= b; j++)
						if (!use[j] && maxPrime(gcd(v, j)) >= p){
							s[u++] = j;
							use[j] = true;
						}
				}
			}
		printf("Case #%d: %d\n", ti, res);
	}
	return 0;
}