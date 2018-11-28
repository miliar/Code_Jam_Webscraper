#include <vector>
#include <stack>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <map>
#include <bitset>
#include <cmath>
using namespace std;

#define GI ({int t ;scanf("%d",&t);t;})
#define FORZ(i,n) for(typeof(n)i=0;i<n;i++)
#define all(x) (x).begin(),(x).end()
#define PB push_back
#define sz size()
#define FF first
#define SS second
typedef vector<int> VI;
typedef pair<int,int> pII;
typedef vector<string> VS;
typedef long long LL;

int main ()
{
	int T = GI;
	FORZ (t	, T) {
		map <string, string> mpb;
		map <char, char> mpo;
		int C, D, N;

		cin >> C;	
		FORZ (i, C) {
			string s;	
			cin >> s;
			string a = s.substr(0, 2), b = s.substr(2, 1);
			mpb[a] = b;
			reverse(all(a));
			mpb[a] = b;
		}	
			
		cin >> D;
		FORZ (i, D) {
			string s;
			cin >> s;
			char a = s[0], b = s[1];
			mpo[a] = b; mpo[b] = a;
		}	
		
		cin >> N;
		
		string seq, ans;
		cin >> seq;
		
		for (int i = 0 ; i < N ; i ++) {
		
			if (ans.empty()) {
				ans += seq[i];
				continue;
			}			
		
			char cur = seq[i], last = ans[ans.sz - 1];
			string a = ans, b, c;
			b += last; b += cur;
			c += cur; c += last;
			bool changed = false;
						
			if (mpb[b] != "") {
				a = a.substr(0, a.sz - 1) + mpb[b];
				changed = true;
			}	
			if (mpb[c] != "") {
				a = a.substr(0, a.sz - 1) + mpb[c];
				changed = true;
			}
			
			if (!changed) {
				FORZ (j, a.sz) {
					if (mpo[a[j]] == cur || mpo[cur] == a[j]) {
						a = "";
						break;
					}	
				}
			}
			
			if (a == "")
			{
				ans = a;
				continue;	
			}	
			if (changed && a != "")
				ans = a;
			else
				ans += cur;			
		}
		
		
		cout << "Case #" << t + 1 << ": [";
		FORZ (i, ans.sz) {
			cout << ans[i];
			if (i < ans.sz - 1) cout << ", ";
		}
		cout << "]\n";
	}
	return 0;
}
