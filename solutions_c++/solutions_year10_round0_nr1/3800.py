#define forn(i, n) for(int i = 0; i<(int) n; i++)
#define ford(i, n) for(int i = (int)n -1; i>=0 ; i--)
#define pb push_back 
#define mp make_pair
#define se second
#define fi first
#define ll long long

#include <vector>
#include <list>
#include <map>
#include <set>
//#include <multiset>
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

using namespace std;
 
int main(){
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int t, n, k;
	scanf("%d", &t);
	forn(i, t)
	{
		scanf("%d%d", &n, &k);
		int ans = 0;
		int tk = 1<<n;
		printf("Case #%d: ", i+1);
		if ((k+1)%tk==0)
			printf("ON\n");
		else
			printf("OFF\n");

	}
}
