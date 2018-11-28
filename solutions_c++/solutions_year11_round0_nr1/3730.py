#include <vector>
#include <valarray>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <sstream>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstring>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <complex>
using namespace std;

#define GETANS

char ri[105];
int pi[105];
int n;
int ans;

void Solve(){
	int posO, posB;
	int timeO, timeB;
	posO = posB = 1;
	timeO = timeB = 0;
	int i;
	for(i = 0; i < n; i++)
	{
		if(ri[i] == 'O')
		{
			timeO += abs(pi[i] - posO)+1;
			if(timeO <= timeB)
				timeO = timeB + 1;
			posO = pi[i];
		}
		else
		{
			timeB += abs(pi[i] - posB) + 1;
			if(timeB <= timeO)
				timeB = timeO + 1;
			posB = pi[i];
		}
	}

	ans = timeO > timeB?timeO:timeB;
}

int main() {

#ifdef GETANS
	freopen("A-large.in","rt",stdin);
	freopen("ans.out","wt",stdout);
#endif

	int c,t,i,j;
	c = 0;
	scanf("%d", &t);
	while(t--)
	{
		c++;
		scanf("%d ", &n);
		for(i = 0; i < n; i++)
			scanf(" %c %d", ri+i, pi+i);

		Solve();
		printf("Case #%d: %d\n", c, ans);
/*
		for(i = 0; i < n; i++)
			printf("%c %d\n",ri[i], pi[i]); 
			*/
	}

	return 0;
}