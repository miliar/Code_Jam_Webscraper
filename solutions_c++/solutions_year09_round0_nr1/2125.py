#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <ctime>
using namespace std;

typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;
typedef vector<char> vc;

#define ALL(t) 			t.begin(),t.end()
#define FOR(i,n) 		for(int i=0;i<(int)(n);i++)
#define FOREACH(i,t) 	for (typeof(t.begin())i=t.begin();i!=t.end();i++)

char buf[1024*1024];


int match(char c, vc &pc) {
	vc::iterator it;
	FOREACH(it, pc) {
		if(c == *it) {
			return 1;
		}
	}
	return 0;
}

int main () {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);	
	
	int l, d, n;
	
	gets(buf);
	sscanf(buf, "%d %d %d", &l, &d, &n);
	
	char words[d][l];
	
	FOR(i, d) {
		gets(buf);
		strncpy(words[i], buf, l);
	}
	
	FOR(i, n) {
		gets(buf);
		int buflen = strlen(buf);
		vc pattern[l];
		int p=0;
		FOR(j, buflen) {
			if(buf[j] == '(') {
				for(++j; buf[j]!=')'; ++j) {
					pattern[p].push_back(buf[j]);
				}
			} else {
				pattern[p].push_back(buf[j]);
			}
			
			p++;
		}
		
		int matchedw = 0;
		FOR(j, d) {
			int matchedc = 0;
			FOR(k, l) {
				if(match(words[j][k], pattern[k])) matchedc++;
			}
			if(matchedc==l) matchedw++;
		}
		
		printf("Case #%d: %d\n", i+1, matchedw);
	}

	return 0;
}
