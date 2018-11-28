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

int main() {
	//ifstream cin("A-small.in");
	ifstream cin("A-large.in");
	ofstream cout("out");

	int L, D, N, Case;
	int i, j, k;
	string s;
	cin>>L>>D>>N;
	vector<string> v(D);
	int ch[15][26];
	for (i=0; i<D; i++) cin>>v[i];
	for (Case=1; N; N--,Case++) {
		cin>>s;
		memset(ch, 0, sizeof(ch));
		for (i=j=0; i<s.length();i++,j++) {
			if (s[i] == '(') {
				while(1) {
					i++;
					if (i>=s.length() || s[i]==')') break;
					ch[j][s[i]-'a'] = 1;
				}
			}
			else ch[j][s[i]-'a'] = 1;
		}
		int res = 0;
		for (i=0; i<D; i++) {
			for (j=0; j<L; j++) {
				if (ch[j][v[i][j]-'a'] == 0) break;
			}
			if (j == L) res++;
		}
		cout<<"Case #"<<Case<<": "<<res<<endl;
	}

}