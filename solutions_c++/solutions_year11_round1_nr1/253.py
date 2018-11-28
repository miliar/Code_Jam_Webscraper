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

i64 gcd (i64 a, i64 b) {
	return b ? gcd (b, a % b) : a;
}

int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int tests1; cin >> tests1;
	for(int tests=0;tests<tests1;tests++){
		i64 pg,pd,n; cin >> n >> pd >> pg;
		i64 mntd = 100/gcd(pd,100);
		i64 mnall = 100/gcd(pg,100);
	//	cout << n << " " << pd << " " << pg << " ->" << mntd << endl;
		if( n<mntd || (pg==100 && pd!=100) || (pd!=0 && pg==0) )
			cout << "Case #"<<tests+1 << ": Broken\n";
		else
			cout << "Case #"<<tests+1 << ": Possible\n";
			

	}

	return 0;
}