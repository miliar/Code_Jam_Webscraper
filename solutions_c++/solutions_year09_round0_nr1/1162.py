// codejam.cpp : Defines the entry point for the console application.
//
#include <vector>
#include <list>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <fstream>
#include <numeric>
#define _USE_MATH_DEFINES 
#include <cmath>
#include <math.h>
using namespace std;

#define sz(v) ((int)(v).size())
#define F(i,a,b) for(int i=(a);i<(b);++i)
#define FSZ(i,a,v) F(i,a,sz(v))
#define all(v) v.begin(),v.end()

// sort Dic
// 24^15 = 
// 5000*15*15*500 

// 24*15 = square by test word
// insert Dic


void A() {
	//	cout << 'z'-'a'+1 << endl;

	int L, D, N;
	cin >> L >> D >> N;

	vector<string> dic;
	for(int t=0; t<D; ++t) {
		string s;
		cin >> s;
		dic.push_back(s);
	}

	for(int t=0; t<N; ++t) {
		string s;
		cin >> s;
		bool flag = false;
		int pos = 0;
		vector<vector<int> > letter_map(26, vector<int>(L, 0));
		FSZ(i,0,s) {
			if(s[i] == '(') {
				flag = true;
			} else if(s[i] == ')') {
				flag = false;
				++pos;
			} else {
				if(flag) {
					letter_map[s[i]-'a'][pos] = 1;
				} else {
					letter_map[s[i]-'a'][pos] = 1;
					++pos;
				}
			}
		}

		int cnt(0);
		FSZ(i,0,dic) {
			bool b = true;
			FSZ(j,0,dic[i]) {
				char c = dic[i][j];
				if(letter_map[c-'a'][j] != 1) {
					b = false;
					break;
				}
			}
			if(b) ++cnt;
		}

		cout << "Case #" << (t+1) << ": " << cnt << endl;
	}
}

int main(int argc, char* argv[])
{
	A();
	return 0;
}

