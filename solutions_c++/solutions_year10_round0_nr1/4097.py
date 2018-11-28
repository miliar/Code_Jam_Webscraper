
#include <cstring>
#include <string>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>

using namespace std;

int main()
{
//	freopen("A-small-attempt0.in","rt",stdin);
//	freopen("A-small.out","wt",stdout);

	freopen("A-large.in","rt",stdin);
	freopen("A-large.out","wt",stdout);

	int t;
	cin >> t;

	for(int tt=0; tt<t; tt++)
	{
		long long n;
		long long k;
		cin >> n >> k;

		if((k+1)%(long long)pow((double)2,(double)n)==0)
			printf("Case #%d: ON\n",tt+1);
		else
			printf("Case #%d: OFF\n",tt+1);		
	}
	return 0;
}
