#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <deque>
#include <map>
#include <queue>
#include <stack>
#include <vector>
#include <set>
#include <list>
#include <bitset>
#include <complex>
#include <list>
#include <sstream>
#include <iomanip>
#include <algorithm>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <functional>
#include <numeric>
#include <utility>
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

#define all(v) v.begin(),v.end()
#define rall(v) v.rbegin(),v.rend()
#define pb push_back
#define SIZE(x) ((int)(x.size()))
#define LENGTH(x) ((int)(x.length()))
#define PI 3.14159265358979323846264338327950288

typedef long long ll;
typedef unsigned long long ull;

/*
 The first line of the input gives the number of test cases, T. T test cases follow. 
 Each test case consists of a single line, containing the following space-separated 
 elements in order:
 
 First an integer C, followed by C strings, each containing three characters:
 two base elements followed by a non-base element. This indicates that the two base 
 elements combine to form the non-base element. Next will come an integer D, followed by D 
 strings, each containing two characters: two base elements that are opposed to each other. 
 Finally there will be an integer N, followed by a single string containing N characters: 
 the series of base elements you are to invoke. You will invoke them in the order they appear 
 in the string (leftmost character first, and so on). 
 */

vector<string> change;
vector<string> opposed;
int T;
int C,D,N;
string s;

bool canChange(char x,char y){
	for (int i=0; i<change.size(); ++i) {
		if  ((x==change[i][0] && y==change[i][1]) || (y==change[i][0] && x==change[i][1]) ) {
			return true;
		}
	}
	return false;
}

bool canErase(char x,char y){
	for (int i=0; i<opposed.size(); ++i) {
		if ((x==opposed[i][0] && y==opposed[i][1]) || (y==opposed[i][0] && x==opposed[i][1]) ) {
			return true;
		}
	}
	return false;
}

char doChange(char x,char y){
	for (int i=0; i<change.size(); ++i) {
		if  ((x==change[i][0] && y==change[i][1]) || (y==change[i][0] && x==change[i][1]) ) {
			return change[i][2];
		}
	}
}

bool check(vector<char> v){
	if ( v.size()>=2 ) {
		for (int i=v.size()-2; i>=0; --i ) {
			if ( canErase(v[i],v[v.size()-1])) {
				return true;
			}
		}
		char a,b;
		a=v.back();
		v.pop_back();
		b=v.back();
		v.pop_back();
		
		v.push_back(a);
		v.push_back(b);
		return canChange(b,a);
	}else 
		return false;
}

int main(){
	cin>>T;
	for (int testcase=1; testcase<=T; ++testcase) {
		change.clear();
		opposed.clear();
		cin>>C;
		for (int i=0; i<C; ++i) {
			string tmp;
			cin>>tmp;
			change.push_back(tmp);
		}
		cin>>D;
		for (int i=0; i<D; ++i) {
			string tmp;
			cin>>tmp;
			opposed.push_back(tmp);
		}
		
		cin>>N>>s;
		vector<char> res;
		for (int i=0; i<s.size(); ++i) {
			res.push_back(s[i]);
			while ( check(res) ) {
				char a,b;
				a=res.back();
				res.pop_back();
				b=res.back();
				res.pop_back();
				if ( canChange(b,a) ) {
					res.push_back( doChange(b,a) );
				}else{
					/*res.push_back(b);
					res.push_back(a);
					
					a=res.back();
					res.pop_back();
					char c;
					
					do {
						c=res.back();
						res.pop_back();
					} while ( !canErase(c,a) );*/
					res.clear();
				}
			}
		}
		cout << "Case #" << testcase << ": [";
		for (int idx=0; idx<res.size(); ++idx) {
			cout << res[idx];
			if (idx!=res.size()-1) cout<<", ";
		}
		cout << "]"<<endl;
	}
	return 0;
}
