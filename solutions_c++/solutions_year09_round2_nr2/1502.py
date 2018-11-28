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

#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;i++)
#define REP(i,n) FOR(i,0,(n)-1)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define FOREACH(i,t) for (typeof(t.begin()) i=t.begin(); i!=t.end(); i++)

#define ALL(x) (x).begin(),(x).end()
#define SORT(x) sort(ALL(x))
#define REVERSE(x) reverse(all(x))
#define CLEAR(x,c) memset(x,c,sizeof(x)) 



int main() {

	int T;
	int64 N, res;
	cin>> T;
	FOR(c,1,T){
		cin>>N;

		vi v;
		while (N){
			v.push_back(N%10);
			N = N/10;
		}
		v.push_back(0);

		vector<int>::iterator it, it_right;
		it = it_right = v.begin();
		it ++;
		while (it <v.end() && (*it >=*it_right)){
			it++;
			it_right++;
		}
		int key = *it;

			
		vector<int>::iterator index;
		for (index =v.begin(); *index<=key || !(*index); index++);
		*it = *index;
		*index = key;

		sort(v.begin(), it,std::greater<int>());

		res = 0; int64 ten = 1;
		for (it = v.begin(); it<v.end();it ++) {
			res += (*it)*ten;
			ten *= 10;
		}
		
		cout <<"Case #"<<c<<": " << res<<endl;
	}
		
	return 0;
}
