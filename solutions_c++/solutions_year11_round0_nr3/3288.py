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

int N;
vector<int> numbers;

void readCase()
{
	scanf("%d", &N);
	numbers.clear();
	for(int i = 1; i <= N; i++) 
	{
		int A;
		scanf("%d", &A);
		numbers.push_back(A);
	}

}

void solve()
{
	long long sum = 0;
	int xor = 0;
	for(int i = 0; i < N; i++)
		xor ^= numbers[i], sum += numbers[i];

	sum -= *min_element(numbers.begin(), numbers.end());
	
	if(xor) printf("NO"); else printf("%lld", sum);
}

int main()
{
	//string fname = "./test/C-example.in";
	//string fname = "./test/C-small-attempt0.in";
	string fname = "./test/C-large.in";
	
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
	}
	return 0;
}

