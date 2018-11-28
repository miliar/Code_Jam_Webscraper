#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
typedef unsigned long long ll;
using namespace std;

int main()
{
	#ifndef ONLINE_JUDGE
	freopen("a.txt", "rt", stdin);
	freopen("b.txt", "wt", stdout);
	#endif

	int t;scanf("%d",&t);
	for (int ii = 0; ii < t; ++ii) {
		int n,k;scanf("%d%d",&n,&k);

		if(k>=n && (ll)(k - (1<<n) + 1) % (ll)(1<<n) == 0 )cout<<"Case #"<<ii+1<<": ON\n";
		else cout<<"Case #"<<ii+1<<": OFF\n";
	}
	return 0;
}

