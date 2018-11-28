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
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

template <class A, class B> void convert(A& x, B& y) {stringstream s; s<<x; s>>y;}

int f[1000000][11];
bool v[1000000];

bool happy(int n, int base, int t) {
	if (n < 1000000) {
	if (f[n][base] == -1) {
		v[n] = 1;
		int i, j, k;
		k = n;
		i = 0;
		if (n != 1) {
			while (k) {
				j = k % base;
				i += j * j;
				k /= base;
			}
			if (!v[i]) f[n][base] = happy(i, base, t);
		}
		else f[n][base] = 1;  
	}
	v[n]  = 0;
	return f[n][base]==1; 
	}
	else {
		int i, j, k;
		k = n;
		i = 0;
		if (n != 1) {
			while (k) {
				j = k % base;
				i += j * j;
				k /= base;
			}
			if (t<100) return  happy(i, base, t+1);
		}
		else return 1;  
	}
}

int main() {
	//ifstream cin("in.txt");
	//ifstream cin("A-small.in");
	ifstream cin("A-large.in");
	ofstream cout("out");
	int T, Case;
	int i, j, k;
	string s;
	vector<int> base;
	for (cin>>T,getline(cin,s), Case=1; T; T--,Case++) {
		getline(cin,s);
		istringstream in(s);
		vector<int> base;
		while(in>>k) base.push_back(k);
		memset(f, -1, sizeof(f));
		memset(v, 0, sizeof(v));
		for (i=2; ; i++) {
			k=0;
			//cout<<i<<endl;
			for (j=0; j<base.size(); j++) {
				if (happy(i, base[j], 0)) k++;
			}
			if (k == base.size()) break;
		}
		cout<<"Case #"<<Case<<": "<<i<<endl;
	}
}