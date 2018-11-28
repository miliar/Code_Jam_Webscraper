#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <fstream>

using namespace std;

int main() {
	freopen("A-large.in","r",stdin);
	int N,S,Q;
	cin>>N;
	string engine[100];
	ofstream fp("A-large.out");
	for(int i = 1; i <= N; i++) {
		cin>>S;
		getline(cin,engine[0]);
		for(int j = 0; j < S; j++) {
			getline(cin,engine[j]);
		}
		cin>>Q;
		string query;
		getline(cin,query);
		set<string> memo;
		int res = 0;
		for(int j = 0; j < Q; j++) {
			getline(cin,query);
			memo.insert(query);
			if((int)memo.size() == S) {
				res ++;
				memo.clear();
				memo.insert(query);
			}
		}
		fp<<"Case #"<<i<<": "<<res<<endl;
	}
	fp.close();
	return 0;
}