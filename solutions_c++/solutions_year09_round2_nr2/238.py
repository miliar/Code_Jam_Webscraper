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


void test() {
	int N;
	cin >> N;
	string welcome = "welcome to code jam";
	string str;
	getline(std::cin, str);
	for(int t=0; t<N; ++t) {
		getline(std::cin, str);
//		cout << "Case #" << (t+1) << ": " << rr << endl;
	}
}

bool s_sort(string& s, int pos) {
	int p = -1;
	char v = s[pos], nv = '9';
	for(int i=pos+1; i<s.size(); ++i) {
		if(v < s[i] && s[i] <= nv) {
			p = i;
			nv = s[i];
		}
	}
	if(p == -1) return false;
	swap(s[pos], s[p]);
	sort(s.begin()+pos+1, s.end());
	return true;
}

string next(string num) {
	for(int i=num.size()-1; i>=0; --i) {
		bool b = s_sort(num, i);
		if(b) return num;
	}
	num.push_back('0');
	sort(all(num));
	int p=0;
	FSZ(i,0,num) if(num[i]!='0') {
		p = i;
		break;
	}
	swap(num[0], num[p]);
	return num;
}

void A2() {

}

void B2() {
	int T;
	cin >> T;
	for(int t=0; t<T; ++t) {
		string num;
		cin >> num;

		string rr = next(num);
		cout << "Case #" << (t+1) << ": " << rr << endl;
	}
}

void C2() {

}

int main(int argc, char* argv[])
{
//	A2();
	B2();
//	C2();
	return 0;
}

