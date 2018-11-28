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

int timetoint(string s) {
	int rr(0);
	rr += (s[0]-'0') * 600;
	rr += (s[1]-'0') * 60;
	rr += (s[3]-'0') * 10;
	rr += (s[4]-'0') * 1;
	return rr;
}

void train() {
	int size(0);
	cin >> size;
	for(int z=0; z<size; ++z) {
		int t, na, nb;
		string dep_time, arr_time;
		cin >> t >> na >> nb;
		vector<pair<int, int> > atA, atB;
		for(int j=0; j<na; ++j) {
			cin >> dep_time >> arr_time;
			atA.push_back(make_pair(timetoint(dep_time), 1));
			atB.push_back(make_pair(timetoint(arr_time)+t, 0));
		}
		for(int j=0; j<nb; ++j) {
			cin >> dep_time >> arr_time;
			atB.push_back(make_pair(timetoint(dep_time), 1));
			atA.push_back(make_pair(timetoint(arr_time)+t, 0));
		}
		sort(all(atA));
		sort(all(atB));
		int stack(0), countA(0), countB(0);
		for(int j=0; j<atA.size(); ++j) {
			if(atA[j].second == 1) {
				if(stack>0) --stack;
				else ++countA;
			} else if(atA[j].second == 0) {
				stack++;
			}
		}
		stack = 0;
		for(int j=0; j<atB.size(); ++j) {
			if(atB[j].second == 1) {
				if(stack>0) --stack;
				else ++countB;
			} else if(atB[j].second == 0) {
				stack++;
			}
		}
		cout << "Case #" << z+1 << ": " << countA << " " << countB << endl;
	}
}

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
//	saveUniverse();
	train();
	return 0;
}

