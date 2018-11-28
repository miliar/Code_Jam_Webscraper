#define _CRT_SECURE_NO_DEPRECATE

#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <algorithm>
#include <ctime>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int)(n); ++i)
#define fore(i, a, b) for(int i = a; i < (int)(b); ++i)
#define pii pair<int,int>
#define pb push_back
#define mp make_pair
#define all(a) a.begin,a.end()
#define ll long long

string s[12345];
int n;
bool bad[123456], usedLetter[34];

bool match(string t, char c){
	forn(i, n){
		if(t.length() != s[i].length() || bad[i])
			continue;
		bool okc = 0;
		forn(j, s[i].length()){
			if (s[i][j] == c)
			{
				okc = 1;
				break;
			}
		}
		if(!okc){
			continue;
		}
		forn(j, t.length())
			if((s[i][j] != t[j] && t[j] != '_') || (t[j] == '_' && usedLetter[s[i][j] - 'a'])){
				okc = 0;
				break;
			}
		if(okc)
			return 1;
	}
	return false;
}
bool del(string t, char c){
	forn(i, n){
		if(t.length() != s[i].length() || bad[i])
			continue;
		bool okc = 0;
		forn(j, s[i].length()){
			if (s[i][j] == c)
			{
				okc = 1;
				break;
			}
		}
		if(!okc){
			continue;
		}
		bad[i] = 1;
	}
	return false;
}
bool del2(string t, char c){
	
	return false;
}

int main(){
#ifndef ONLINE_JUDGE
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif

	int t;
	cin >> t;
	forn(tt, t){
		int m;
		cin >> n >> m;
		getline(cin, s[0]);



		forn(i, n){
			getline(cin, s[i]);
		}

		printf("Case #%d:", tt + 1);
		forn(i, m){
			string L;
			getline(cin, L);
			int mx = -1;
			string ans = "";


			forn(j, n){
				memset(bad, 0, sizeof bad);
				int used[26];
				memset(used, 0, sizeof used);
				memset(usedLetter, 0, sizeof usedLetter);
				int k = (int)s[j].size();
				forn(kk, s[j].length())
					used[s[j][kk] - 'a']++;
				string a (s[j].length(), '_');
				int res = 0;
				forn(kk, 26){
					if(!k)
						break;
					if (match(a, L[kk])){
						if(used[L[kk] - 'a'] == 0){
							del(a, L[kk]);
							++res;
						}else
							del2(a, L[kk]);
						k -= used[L[kk] - 'a'];
						forn(ii, a.length())
							if (s[j][ii] == L[kk])
								a[ii] = L[kk];
					}
					usedLetter[L[kk] - 'a'] = 1;
				}
				if (res > mx){
					mx = res;
					ans = s[j];
				}
			}

			printf(" %s", ans.c_str());
		}
		puts("");

		/*
		long long n;
		int pd, pg;
		cin >>n >>pd >> pg;
		bool ok = 0;

		printf("Case #%d: ", tt + 1);

		if(n > 100)n = 100;

		if(n > 100){

		}else{
			fore(j, 1, n + 1){
				if(!ok)
					forn(k, j + 1){
						if(ok)continue;
						if (k * 100 == pd * j){
							if (k > 0 && pg == 0)
								continue;
							if (k < j && pg == 100)
								continue;
							ok = 1;
							puts("Possible");
						}
					}
			}
		}
		if (!ok)
			puts("Broken");
			*/
	}
	
	return 0;
}