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

// (count)*14 / 10000
// 앞 포지션으로 이어지는 애들은 모두 더해주기
// 다시 시작되는 걸 조심해야 함
void B() {
	int N;
	cin >> N;
	string welcome = "welcome to code jam";
	string str;
	getline(std::cin, str);
	for(int t=0; t<N; ++t) {
		getline(std::cin, str);
		vector<vector<int> > v(str.size(), vector<int>(welcome.size(), 0));
		FSZ(i,0,str) {
			if(str[i] == 'w') v[i][0] = 1;
		}
		FSZ(i, 1, welcome) {
			FSZ(j,0,str) {
				if(welcome[i] == str[j]) {
					int sum(0);
					for(int k=0; k<j; ++k) {
						sum = (sum + v[k][i-1]) % 10000;
					}
					v[j][i] = sum;
				}
			}
		}
		int cnt(0);
		FSZ(i,0,v) {
			cnt = (cnt + v[i][welcome.size()-1]) % 10000;
		}
		char buf[512];
		itoa(cnt, buf, 10);
		int padding = 4-strlen(buf);
		string rr;
		for(int i=0; i<padding; ++i) {
			rr += '0';
		}
		rr += buf;
		cout << "Case #" << (t+1) << ": " << rr << endl;
	}
}

int main(int argc, char* argv[])
{
//	A();
	B();
	return 0;
}

