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

#define sz size()
#define pb push_back
#define ppb pop_back
#define all(c) (c).begin(), (c).end()
#define sqr(a) (a)*(a)
#define mp(a,b) make_pair((a), (b))
#define x first
#define y second


typedef vector<int> vint;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;

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
	freopen ("output.txt", "w", stdout);
	int n = in();
	scanf("\n");
	map <char, char> key;
	key[' ']=' ';
	key['a']='y';
	key['b']='h';
	key['c']='e';
	key['d']='s';
	key['e']='o';
	key['f']='c';
	key['g']='v';
	key['h']='x';
	key['i']='d';
	key['j']='u';
	key['k']='i';
	key['l']='g';
	key['m']='l';
	key['n']='b';
	key['o']='k';
	key['p']='r';
	key['q']='z';
	key['r']='t';
	key['s']='n';
	key['t']='w';
	key['u']='j';
	key['v']='p';
	key['w']='f';
	key['x']='m';
	key['y']='a';
	key['z']='q';
	vector <string> in;
	for(int i=0; i<n; ++i){
		string s;
		getline(cin,s);
		in.push_back(s);
	}
	for(int i=0; i<n; ++i){
		for(int j=0; j<in[i].size(); ++j){
			in[i][j] = key[in[i][j]];
		}
	}
	for(int i=0; i<n; ++i){
		cout<<"Case #"<<i+1<<": "<<in[i]<<endl;
	}
	return 0;

}