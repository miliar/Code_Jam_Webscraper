// gcj2008.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <vector>
#include <list>
#include <map>
#include <set>
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

// 현재의 template
#define sz(v) ((int)(v).size())
#define F(i,a,b) for(int i=(a);i<(b);++i)
#define FSZ(i,a,v) F(i,a,sz(v))
#define all(v) v.begin(),v.end()
string itoa(int i) { stringstream ss; ss<<i; return ss.str(); }
#define same(a,b) (fabs((a)-(b))<0.0000001)
inline int loop(int size, int now, int add) { return (now+add)%size; }
#define two(N) (1<<(N))
#define contain(S,N) (((S)&two(N))!=0)
#define subset(S,X) (((S)&(X))==(X))
// 해당 위치에 비트의 값 체크 (0인지, 1인지)
#define bitpos(X,P) ((X&(1<<(P)))&&(1<<(P)))
template<class T> inline int countbit(T n){return (n==0)?0:(1+countbit(n&(n-1)));}
#define bound(i,j,isize,jsize) (0<=(i)&&(i)<(isize)&&0<=(j)&&(j)<(jsize))

void saveUniverse() {
	int size(0);
	char sz[1024];
	cin >> size;
	for(int z=0; z<size; ++z) {
		int S, Q;
		vector<string> engine;
		vector<string> query;
		set<string> check;
		cin >> S;
		cin.getline(sz, 1024);
		for(int i=0; i<S; ++i) {
			cin.getline(sz, 1024);
			string s(sz);
			engine.push_back(s);
		}
		cin >> Q;
		cin.getline(sz, 1024);
		for(int i=0; i<Q; ++i) {
			cin.getline(sz, 1024);
			string s(sz);
			query.push_back(s);
		}
		int count(0);
		for(int i=0; i<query.size(); ++i) {
			check.insert(query[i]);
			if(check.size() == S) {
				++count;
				check.clear();
				check.insert(query[i]);
			}
		}
		cout << "Case #" << z+1 << ": " << count << endl;
	}
}

int main(int argc, char* argv[])
{
	saveUniverse();
	return 0;
}

