#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <cmath>
#include <cstring>
#include <queue>
#include <stack>
#include <algorithm>
#include <sstream>
#include <cassert>
using namespace std; 

#define f first
#define s second
#define mp make_pair
#define sz(a) int((a).size()) 
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define forit(it,S) for(typeof(S.begin()) it = S.begin(); it != S.end(); ++it)

char to[300];
string ss;
string s = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
string t = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";

int main() {
	for (char ch = 'a'; ch <= 'z'; ++ch)
		to[ch] = '-';
	for (int i = 0; i < s.size(); ++i) if (isalpha(s[i])) {
		to[s[i]] = t[i];
	}
			
	to['z'] = 'q';
	to['q'] = 'z';
		
	int tests;
	scanf("%d\n", &tests);		
	for (int casenum = 1; casenum <= tests; ++casenum) {		
		getline(cin, ss);
		int n = ss.size();
		for (int i = 0; i < n; ++i) {
			assert((ss[i] >= 'a' && ss[i] <= 'z') || ss[i] == ' ');
			if (isalpha(ss[i]))
				ss[i] = to[ss[i]];
		}				
		printf("Case #%d: ", casenum);
		cout << ss << endl;
	}
	return 0;		
}

