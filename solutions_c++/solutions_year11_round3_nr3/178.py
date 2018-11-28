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
#include <list>
#include <set>
#include <map>
#include <sstream>
#include <queue>
#include <bitset>
#include <string.h>
using namespace std;

long long N, L, H;
list<int> notes;

void readCase()
{
	scanf("%lld %lld %lld", &N, &L, &H);
	notes.clear();
	for(int i = 0; i < N; i++) 
	{
		int f;
		scanf("%d", &f);
		notes.push_back(f);
	}
}

long long gcd(long long a, long long b)
{
	while(b != 0)
	{
		long long t = b;
		b = a % b;
		a = t;
	}
	return a;
}

long long lcm(long long a, long long b)
{
	return a * b / gcd(a, b);
}

void solve()
{
	long long cur;
	for(cur = L; cur <= H; cur++)
	{
		bool ok = true;
		for(list<int>::iterator note = notes.begin(); note != notes.end(); ++note)
		{
			if(*note % cur && cur % *note)
			{
				ok = false;
				break;
			}
		}
		if(!ok) continue;
		printf("%lld", cur);
		return;
	}
	printf("NO");
}

int main()
{
	//string fname = "./test/C-example.in";
	string fname = "./test/C-small-attempt0.in";
	//string fname = "./test/C-large.in";
	
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

