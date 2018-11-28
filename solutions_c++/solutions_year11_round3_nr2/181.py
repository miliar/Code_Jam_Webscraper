#include <stdio.h>
#include <functional>
#include <bitset>
#include <math.h>
#include <time.h>
#include <stdlib.h>
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <sstream>
#include <queue>
#include <bitset>
#include <string.h>
using namespace std;

long long N, L, t, C;
vector<int> space;

void readCase()
{
	scanf("%lld %lld %lld %lld", &L, &t, &N, &C);
	space.resize( N );
	for(int i = 0; i < C; i++) 
	{
		int a;
		scanf("%d", &a);
		space[i] = a;
	}
	for(int i = C; i < N; i++) 
	{
		space[i] = space[i%C];
	}
}

void solve()
{
	long long time = 0;
	int s = 0;

	do
	{
		long long tot = (t - time) / 2;
		if( tot < space[s] )
		{
			time += tot * 2;
			space[s] = space[s] - tot;
		} else {
			time += space[s] * 2;
			s++;
		}
	}
	while( s < N && time < t );

	sort( space.begin() + s, space.end(), greater<int>() );

	for(int b = 0; s < N && b < L; s++, b++)
	{
		time += space[s];
	}

	for(; s < N; s++)
	{
		time += space[s] * 2;
	}

	printf("%lld", time);
}

int main()
{
	//string fname = "./test/B-example.in";
	//string fname = "./test/B-small-attempt0.in";
	string fname = "./test/B-large.in";
	
	freopen(fname.c_str(),"r",stdin);freopen((fname+".out").c_str(),"w",stdout);

	int analizeCase = -1;
	
	int T;
	scanf("%d", &T);
	for(int tCase = 1; tCase <= T; tCase++) {
		printf("Case #%d: ", tCase);
		readCase();
		if(analizeCase < 0 || analizeCase == tCase) solve();
		printf("\n");
		fflush(stdout);
		fprintf(stderr, "Done %d %%     \r", 100 * tCase / T );
	}
	return 0;
}

