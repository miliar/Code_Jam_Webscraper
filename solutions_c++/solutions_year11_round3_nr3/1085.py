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
typedef long long ll;

int N, L, H;
int f[10005];

void main2()
{
	scanf("%d %d %d", &N, &L, &H);
	int i,j;
	for(i = 0; i < N; i++)
	{
		scanf("%d", &f[i]);
	}

	for(i = L; i <= H; i++)
	{
		for(j = 0; j < N; j++)
		{
			if(f[j] % i == 0 || i % f[j] == 0)
				continue;
			break;
		}

		if(j >= N)
			break;
	}

	if(i <= H)
		printf(" %d\n", i);
	else
		printf(" NO\n");
}

int main() {

#define GETANS

#ifdef GETANS
	 freopen("C-small-attempt2.in","rt",stdin);
	freopen("ans.out","wt",stdout);
#endif

	int c,t;
	c = 0;
	scanf("%d", &t);
	while(t--)
	{
		c++;
		printf("Case #%d:", c);
		main2();
	}

	return 0;
}