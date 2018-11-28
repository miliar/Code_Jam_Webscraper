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

#define pb push_back
#define mp make_pair
#define sz size()
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<vector<pii> > adjL;
int oo = (int) 1e9;


int main()
{
#ifndef ONLINE_JUDGE
freopen("a.txt", "rt", stdin);
freopen("b.txt", "wt", stdout);
#endif

	ll low ,up ;
	double l , p , c;
	int t;
	cin>>t;
	for (int ii = 0; ii < t; ++ii) {
		cout<<"Case #"<<ii+1<<": ";
		cin>>l>>p>>c;
		int res = 0 ;
		while(p > l * c)
		{
			res++;
			p = ceil( p / c);
		}
		if(res == 0 )cout<<0<<endl;
		else
		cout<< ceil(log2(res+1))<<endl;
	}

	return 0;
}
/*
 *
 *
 *
4
50 700 2
19 57 3
1 1000 2
24 97 2

 */
