#define _CRT_SECURE_NO_DEPRECATE
#include<iostream>
#include<numeric>
#include<sstream>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<memory>
#include<string>
#include<vector>
#include<cctype>
#include<list>
#include<queue>
#include<deque>
#include<stack>
#include<map>
#include<set>
#include<algorithm>
using namespace std;

typedef unsigned long long		ui64;
typedef long long				i64;
typedef	vector<int>				vi;
typedef	vector<string>			vs;
typedef	pair<int,int>			pii;
typedef	pair<double,double>		point;

#define pb						push_back
#define mp						make_pair
#define X						first
#define Y						second
#define all(a)					(a).begin(), (a).end()
#define INF						(2000000000)


int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int test;
	cin >> test;
	int K = test+1;
	for(;test;test--){
		int n; cin >> n;

		int sum = 0, mn = INF, s=0;
		for(;n;n--){
			int a;
			cin >> a;
			mn = min(a,mn);
			sum ^= a;
			s += a;
		}
		cout << "Case #" << K-test << ": ";
		if(sum)
			cout << "NO\n";
		else
			cout << s-mn << endl;
	}
	return 0;
}