// SpaceEmergency.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <string>
using namespace std;

int readi() { int a; scanf( "%d", &a ); return a; }
double readf() { double a; scanf( "%lf", &a ); return a; }
char sbuf[100005]; string readstr() { scanf( "%s", sbuf ); return sbuf; }
long long readll() { long long a; scanf( "%lld", &a ); return a; }
#define fo(a,b,c) for( a = ( b ); a < ( c ); ++ a )

#define MAX 1000000
int dist[MAX];
int t;

int flytime(int N, int L){
	int time, buildtime, thistime1 = 2147483647, thistime2 = 2147483647;
	int prevtime; //time already spent

	//without speed
	time = dist[N] * 2;
	if(N == 0) thistime1 = time;
	else thistime1 = time + flytime(N-1, L);
	
	//with speed
	if(L >= 1) {
		if(N == 0) prevtime = 0;
		else prevtime = flytime(N-1, L - 1);

		if(prevtime >= t) { //Already built
			time = dist[N];
		} else {
			buildtime = t - prevtime; //additional time needed.
			if(buildtime >= time) {}//have no influency 
			else {
				if(buildtime % 2 != 0)  printf("\nerror\n");
				time = buildtime + (dist[N] - 0.5 * buildtime); 
			}
		}
		thistime2 = time + prevtime;
	}

	if (thistime1 <= thistime2) time = thistime1;
	else time = thistime2;
	return time;
}


int _tmain(int argc, _TCHAR* argv[])
{
	freopen("B-small-attempt0.in","rt",stdin);
	freopen("B-small-attempt0.out","wt",stdout);	

	int T, N, C, L;
	int i, j, k, r, time;


	T = readi();
	for(r = 1; r <= T; r++) {
		//Load data
		L = readi();  t = readi(); N = readi();	C = readi();
		memset(dist, 0, MAX * sizeof(int));
		for(i = 0; i < C; i++) dist[i] = readi();
		for(j = C; j < N; j++) dist[j] = dist[j % C];
		time = flytime(N - 1, L);

		printf("Case #%d: %d\n", r, time);

	}


	return 0;
}

