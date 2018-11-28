#include <stdio.h>
#include <algorithm>
#include <memory.h>
#include <queue>
#include <math.h>
#include <vector>
#include <map>
#include <stack>
#include <string.h>
#include <string>
#include <iostream>
#include <deque>
#include <stdlib.h>
#include <stack>
using namespace std;
int _T;
int n,m;
string d[1111],alf;
bool used[1111];

bool cmp(string a, string b) {
	if (a.length() != b.length()) return 0;
	for (int i=0;i<a.length();i++)
		if (!(a[i] == '!' || a[i] == b[i] || b[i] == '!')) return 0;
	return 1;
}

int main() {
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	
	scanf("%d",&_T);
	for (int _t=1;_t<=_T;_t++) {
		printf("Case #%d: ",_t);
		
		cin >> n >> m;
		for (int i=0;i<n;i++) cin >> d[i];
		
		while (m--) {
			cin >> alf;
			int best = -1; string ans;
			
			for (int i=0;i<n;i++) {
				memset(used,0,sizeof(used));
				string x = d[i];
				string cur = ""; int score = 0;
				for (int j=0;j<x.length();j++) cur += '!';
				
				
				for (int j=0;j<alf.length();j++) {
					//if (cur.length() != x.length()) cout << "AAAAAAAAAAAAAAAA";
					
					bool cool = 0;
					for (int k=0;k<n;k++)
						if (!used[k] && cmp(cur,d[k])) {
							for (int q=0;q<d[k].length();q++)
								if (d[k][q] == alf[j]) {
									cool = 1;
									break;
								}
							if (cool) break;
						}
					
					if (cool) {
						cool = 0;
						for (int k=0;k<x.length();k++)
							if (x[k] == alf[j]) {
								cur[k] = x[k];
								cool = 1;
							}
						if (!cool) score++;
						for (int k=0;k<n;k++)
								if (!used[k] && x.length() == d[k].length())
									for (int q=0;q<d[k].length();q++)
										if ((d[k][q] == alf[j] && x[q] != alf[j]) || (d[k][q] != alf[j] && x[q] == alf[j])) used[k] = 1;
					}
					if (cur == x) break;
				}
				
				//cout << cur << " " << score << endl;
				
				if (score > best) {
					ans = x;
					best = score;
				}
			}
			
			cout << ans;
			if (m) cout << ' ';
		}
		
		cout << endl;
	}
	
	return 0;
}
