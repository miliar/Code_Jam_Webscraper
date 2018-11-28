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
#include <iostream>
#include <climits>
#include <cstring>
#include <fstream>
using namespace std;

#define forn(a, n) for(int a = 0; a<(n); ++a)
#define forsn(a,s,n) for(int a = (s); a<(n); ++a)
#define forall(a, all) for(typeof((all).begin()) a = (all).begin(); a != (all).end(); ++a)

#define dforn(a, n) for(int a = (n)-1; a>=0; --a)
#define dforsn(a,s,n) for(int a = (n)-1; a>=(s); --a)
#define dforall(a, all) for(typeof((all).rbegin()) a = (all).rbegin(); a != (all).rend(); ++a)

#define contains(mask, bit) ((mask & (1LL<<bit)) != 0LL)

typedef long long tint;

int T, a, b, vist[2000004];

vector<int> intToVi(int ka){
	vector<int> ret;
	while(ka > 9){
		ret.push_back(ka%10);
		ka/=10;
	}
	ret.push_back(ka);
	reverse(ret.begin(), ret.end());
	return ret;
}

int viToInt(const vector<int> &vi){
	int num = 0;
	
	forn(i, vi.size())
		num = num*10 + vi[i];
	return num;
}

int calc2(int n){
	memset(vist, 0, sizeof(vist));
	vector<int> v = intToVi(n);
	int ret = 0;
	
	dforn(i, v.size()){
		vector<int> c;
		c.insert(c.begin(), v.begin()+i, v.end());
		c.insert(c.end(), v.begin(), v.begin()+i);
		int m = viToInt(c);
		
		if(n < m && m <= b && !vist[m]){
			ret++;
			vist[m] = 1;
		}
	}
	return ret;
}

int calc(int n){
	vector<int> v = intToVi(n);
	int ret = -1;
	dforn(i, v.size()){
		vector<int> c;
		c.insert(c.begin(), v.begin()+i, v.end());
		c.insert(c.end(), v.begin(), v.begin()+i);
		int m = viToInt(c);
		if(n <= m && m <= b && !vist[m]){
			ret++;
			vist[m] = 1;
		}
	}
	return ret*(ret+1)/2;
}

int main()
{
#ifdef __YO__
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
#endif
	
	scanf("%i", &T);
	
	forn(t, T){
		scanf("%i%i", &a, &b);
		int ret = 0;
		cerr << t << endl;
		memset(vist, 0, sizeof(vist));
		forsn(i, a, b+1) if(!vist[i])
			ret += calc(i);
		
		printf("Case #%i: %i\n", t+1, ret);
	}

	return 0;
}
