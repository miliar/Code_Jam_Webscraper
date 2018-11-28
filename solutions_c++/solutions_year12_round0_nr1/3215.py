#define _USE_MATH_DEFINES
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <deque>
#include <algorithm>
#include <typeinfo>
#include <set>
#include <cctype>
#include <locale>
#include <utility>
#include <map>
#include <iterator>
#include <cstring>
using namespace std;

const double eps = 1e-6; 

int in() {
	int a;
	scanf("%d", &a);
	return a;
}

double din() {
	double a;
	scanf("%lf", &a);
	return a;
}

int gcd(int a, int b) {
	while(b){
		a%=b;
		swap(a,b);
	}
	return a;
}

int lcm(int a, int b) {
	return a / gcd(a, b) * b;
}


int main(){
	freopen ("1.in", "r", stdin);
	freopen ("out.txt", "w", stdout);
	int n = in();
	map <char, char> keys;
	scanf("\n");	
	keys[' ']=' ';
	keys['a']='y';
	keys['b']='h';
	keys['c']='e';
	keys['d']='s';
	keys['e']='o';
	keys['f']='c';
	keys['g']='v';
	keys['h']='x';
	keys['i']='d';
	keys['j']='u';
	keys['k']='i';
	keys['l']='g';
	keys['m']='l';
	keys['n']='b';
	keys['o']='k';
	keys['p']='r';
	keys['q']='z';
	keys['r']='t';
	keys['s']='n';
	keys['t']='w';
	keys['u']='j';
	keys['v']='p';
	keys['w']='f';
	keys['x']='m';
	keys['y']='a';
	keys['z']='q';
	vector <string> ss;
	for(int i=0; i<n; ++i){
		string s;
		getline(cin,s);
		ss.push_back(s);
	}
	for(int i=0; i<n; ++i){
		for(int j=0; j<ss[i].size(); ++j){
			ss[i][j] = keys[ss[i][j]];
		}
	}
	for(int i=0; i<n; ++i){
		cout<<"Case #"<<i+1<<": "<<ss[i]<<endl;
	}
	return 0;
}
