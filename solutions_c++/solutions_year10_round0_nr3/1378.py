//#include <iostream>
#include <fstream>
#include <sstream>
#include <set>
#include <list>
#include <vector>
#include <map>
#include <queue>
#include <stack>
#include <string>
#include <cmath>
#include <algorithm>
using namespace std;

ifstream cin("C-small.in",ios::in);
ofstream cout("C-small.out",ios::out);

long long* G;
long long S;
int K, N, R, c;
map<pair<int,int>,long long> mem;

long long rec(int r) {
	if (mem.count(make_pair(c,r)))
		return mem[make_pair(c,r)];
	long long ans = 0;
	int ci = c;
	for (c=ci; c<N; c++) {
		if (r<G[c]) {
			mem[make_pair(c,r)] = ans;
			return ans;
		}
		r -= G[c];
		ans += G[c];
	}
	for (c=0; c<ci; c++) {
		if (r<G[c]) {
			mem[make_pair(c,r)] = ans;
			return ans;
		}
		r -= G[c];
		ans += G[c];
	}
	mem[make_pair(c,r)] = ans;
	return ans;
}

void go() {
	mem.clear();
	cin >> R >> K >> N;
	G = new long long [N];
	S = 0; c = 0;
	for (int i=0; i<N; i++) {
		cin >> G[i];
		S += G[i];
	}
	long long T = 0;
	for (long long i=0; i<R; i++)
		T += rec(K);
	cout << T;
	delete [] G;
}


int main() {
	int T;
	cin>>T;
	for (int i=1; i<=T; i++) {
		cout<<"Case #"<<i<<": ";
		go();
		cout<<endl;
	}
	return 0;
}
