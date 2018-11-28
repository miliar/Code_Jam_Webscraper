/*
Yet another code by amrSamir
*/
#include <vector>
#include <valarray>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <sstream>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstring>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <complex>
using namespace std;
typedef long long ll;
typedef long double ld;

string in = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv yeq";
string out= "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up aoz";

int main()
{

	freopen("A-small-attempt0.in","rt",stdin);
	freopen("A-small.out","wt",stdout);
	char m[128];
	for(int i = 0;  i < in.size(); ++i) {
		m[in[i]]=out[i];
	}
	m['z'] = 'q';
//	for (int i = 0; i < 26; ++i) {
//		cout << (char)(i+'a') << " " << m[i+'a'] << endl;
//	}
	int n;
	cin >> n;
	string s;
	getline(cin,s);
	for (int i = 0; i < n; ++i) {
		getline(cin,s);
		cout << "Case #" << i+1 << ": ";
		for (int i = 0; i < s.size(); ++i) {
			cout << m[s[i]];
		}
		cout << endl;
	}
	return 0;
}
