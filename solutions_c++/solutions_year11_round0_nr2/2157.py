#pragma comment(linker, "/STACK:64000000")
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <cassert>
#include <ctime>
#include <deque>

#define forn(i, n) for (int i = 0; i < n; i ++)
#define ford(i, n) for (int i = n - 1; i >= 0; i --)
#define mp make_pair
#define pb push_back
#define x first
#define y second
#define pi 3.1415926535897932
#define ll long long
#define ld long double

using namespace std;

string s1[110], s2[110];
stack<char> st;
int kol[26];
vector <char> ans;

int main(){
#ifndef ONLINE_JUDGE
	freopen ("input.txt","rt",stdin);
	freopen ("output.txt","wt",stdout);
#endif
	int t;
	cin >> t;
	forn(qqq, t){
		memset(kol, 0, sizeof(kol));
		ans.clear();
		int c, d, n;
		scanf("%d ", &c);
		forn(j, c){
			char c1;
			s1[j].clear();
			forn(k, 3){
				scanf("%c", &c1);
				s1[j] += c1;
			}
			if (s1[j][0] > s1[j][1]) swap(s1[j][0], s1[j][1]);
			scanf(" ");
		}
		scanf("%d ", &d);
		forn(j, d){
			char c1;
			s2[j].clear();
			forn(k, 2){
				scanf("%c", &c1);
				s2[j] += c1;
			}
			if (s2[j][0] > s2[j][1]) swap(s2[j][0], s2[j][1]);
			scanf(" ");
		}
		scanf("%d ", &n);
		forn(i, n){
			char c1;
			scanf("%c", &c1);
			st.push(c1);	
			kol[c1 - 'A'] ++;
			bool q = true;
			while (q){
				if (st.size() < 2) break;
				q = false;
				string s;
				s += st.top();
				st.pop();
				s += st.top();
				st.push(s[0]);
				if (s[0] > s[1]) swap(s[0], s[1]);
				forn(j, c)
					if (s[0] == s1[j][0] && s[1] == s1[j][1]){
						kol[st.top() - 'A'] --;
						st.pop();
						kol[st.top() - 'A'] --;
						st.pop();
						st.push(s1[j][2]);
						kol[s1[j][2] - 'A'] ++;
						q = true;
						break;
					}
			}
			forn(j, d)
				if (kol[s2[j][0] - 'A'] != 0 && kol[s2[j][1] - 'A'] != 0){
					while (!st.empty()) st.pop();
					memset(kol, 0, sizeof(kol));
					break;
				}
		}
		while (!st.empty()){
			ans.pb(st.top());
			st.pop();
		}
		reverse(ans.begin(), ans.end());
		printf ("Case #%d: ", qqq + 1);
		printf("[");
		forn(i, ans.size()){
			printf ("%c", ans[i]);
			if (i != ans.size() - 1) printf (", ");
		}
		printf ("]\n");
		scanf("\n");
	}
	return 0;
}