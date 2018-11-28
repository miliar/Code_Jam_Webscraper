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

	
	int64 C;
	cin >> C;
	cin.ignore();

	int map[256];

	FOR(c,1,C){
		string str;
		uint64 res;
		getline (cin,str);

		CLEAR(map,-1);
		int base = 1, index =0;
		map[str[0]] = 1;
		for(int i=1;i<str.length();i++){
			if(map[str[i]]==-1){
				base ++;
				map[str[i]] = index;
				if(!index) index = 2; else index ++;
			}
		}
		if (base==1) base++;
		res = 0;
		for(int i = 0; i < str.length(); i++){
			res  = res*base + map[str[i]];
		}

		cout <<"Case #"<<c<<": "<< res <<endl;
	}
		
	return 0;
}
