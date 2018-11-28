#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <cmath>
#include <cctype>
#include <cstdio>
#include <cstdlib>

#define REP(i, T) for(int (i)=0; (i) < T; (i) ++)
#define FOR(i, L, R) for(int (i)=L; (i) < R; (i) ++)
#define PB push_back
#define ALL(v) v.begin(), v.end()
#define SZ(v) (int)v.size()

#define vi vector<int>
#define vs vector<string>
#define ui unsigned int
#define ll long long

using namespace std;

int l, d, n, i, j, k;
string dic[5100];
int mark[5100];
int tot;
string s;

int main()
{
	cin >> l >> d >> n;
	for(i=0; i<d; i++) cin >> dic[i];
	
	for(int caso=1; caso<=n; caso++) {
		cin >> s;
		for(i=0; i<d; i++) mark[i]=1;
		
		int si=0;
		for(i=0; i<l; i++) {
			int a, b;
			if(s[si]=='(') {
				a=si+1;
				while(s[si]!=')') si++;
				b=si-1;
			} else a = b = si;
			si++;
			
			for(j=0; j<d; j++) {
				if(!mark[j]) continue;
				int found=0;
				for(k=a; !found && k<=b; k++) {
					if(dic[j][i] == s[k]) found=1;
				}
				if(!found) mark[j]=0;
			}
		}
		
		int tot=0;
		for(i=0; i<d; i++) if(mark[i]) tot++;
		
		cout << "Case #" << caso << ": " << tot << endl;
	}
	return 0;
}
