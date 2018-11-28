#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <map>
#include <algorithm>
#include <cstring>
#include <string>
#include <list>

using namespace std;

typedef long long int LL;
typedef pair<int,int> pii;

#define F first
#define S second
#define pb push_back
#define mp make_pair

double dist(double xa, double ya, double xb, double yb) {
	return sqrt( (xa -xb) * (xa - xb) + (ya - yb) * (ya - yb));
}

int main (void)
{
	int T;

	scanf("%d", &T);

	LL r[10000];

	srand( 45655 );

	for(int t = 0; t < T; t++) {

		printf("Case #%d: ", t+1);

		LL N, W, H;

		scanf("%lld %lld %lld", &N, &W, &H);

		for(int i = 0; i < N; i++) {
			scanf("%lld", &r[i]);
		}

		double posx[N+1], posy[N+1];

		int done = 0;

		while(!done) {

			for(int i = 0; i < N; i++) {
				posx[i] = (double) rand()/RAND_MAX * W;
				posy[i] = (double) rand()/RAND_MAX * H;
			}

			int collide = 0;
			for(int i = 0; i < N; i++)
				for(int j = i+1; j < N; j++) {
					if(dist(posx[i], posy[i], posx[j], posy[j]) < r[i] + r[j]) collide = 1;	
				}

			if(!collide) done = 1;
		}

		for(int i = 0; i < N; i++)
			printf("%lf %lf ", posx[i], posy[i]);
		printf("\n");
	}

	return 0;
}
