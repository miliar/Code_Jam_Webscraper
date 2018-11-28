#include<cstdio>
#include<algorithm>
#include<iostream>
#include<sstream>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<numeric>
#include<cmath>
#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include <ctype.h>

using namespace std;

typedef vector<int> vi;
typedef unsigned long long uint64;
typedef long long int64;

#define FOR(i,a,b) for(int64 i=(a),_b=(b);i<=_b;i++)
#define REP(i,n) FOR(i,0,(n)-1)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define FOREACH(i,t) for (typeof(t.begin()) i=t.begin(); i!=t.end(); i++)

#define ALL(x) (x).begin(),(x).end()
#define SORT(x) sort(ALL(x))
#define REVERSE(x) reverse(all(x))
#define CLEAR(x,c) memset(x,c,sizeof(x)) 



int main() {

	
	int64 T;
	cin >> T;

	FOR(t,1,T){
		int64 N, K;
		cin >> N;
		cin >> K;

		int64 r;
		r = 1;
		r = (1<<N) -1;
		bool res = (r&K)==r;

		cout <<"Case #"<<t<<": "<< (res?"ON":"OFF") <<endl;
	}
		
	return 0;
}
