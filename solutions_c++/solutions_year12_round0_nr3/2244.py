//============================================================================
// Name        : gcj2012qualC.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================


#include <iostream>
#include <algorithm>
#include <sstream>
#include <string>
#include <queue>
#include <vector>
#include <set>
#include <map>
#include <cstring>
#include <cstdio>
using namespace std;

#define For(i,a,b) for(int i = a; i < b; i++)
#define rep(i,x) For(i,0,x)
#define Foreach(i,c) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define sz(x) (int((x).size()))
#define F first
#define S second
#define mp make_pair

using namespace std;

deque<int> convert(int n){
	deque<int> res;
	while(n){
		res.push_front(n % 10);
		n /= 10;
	}
	return res;
}

int deconvert(deque<int> d){
	int res = 0;
	for(int i = 0; i < sz(d); i++)
		res = res * 10  + d[i];
	return res;
}

void rotate(deque<int>& d){
	d.push_front(d.back());
	d.pop_back();
}

typedef long long ll;
int main() {

	int np; cin>>np;
	rep(tp,np){
		set<pair<int,int> > got;
		ll res = 0;
		int a,b; cin>>a>>b;
		For(i,a,b+1){
			deque<int> d = convert(i);
			int n = sz(d);
			int key = i;

			ll legal = 0;
			set<int> unique;
			rep(j, n){
				rotate(d);
				int v = deconvert(d);
				key = min(key, v);
				if(d[0] != 0 && v >= a && v <= b && unique.insert(v).S)
					legal++;
			}
			if(got.insert(mp(key, n)).second){
				//cout << i << " " << key << " " << legal << endl;
				res += (legal)*(legal-1)/2;
			}
		}
		cerr << (tp+1) << endl;
		printf("Case #%d: %lld\n",tp + 1, res);
	}
}
