/*
ID: ahaigh1
PROG: 
LANG: C++
*/
#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>
#include <algorithm>
#include <queue>
#include <utility>
#include <memory>
#include <set>
#include <stack>
#include <string>
#include <cstdlib>
#include <cstring>
#include <sstream>
#include <limits>
#include <map>
#include <bitset>
using namespace std;

#define REP(i, n) for(int i = 0; i < n; i++)
#define CL(x) memset(x, 0, sizeof(x))
#define eps (1e-10)
#define inf (1<<30)
#define ll long long
#define MP make_pair

char can_combine[26][26];
bool can_oppose[26][26];

char st[105]; int l;
int in_list[26];

int t, c, d, n;
char x, y, z;
char s[5000];

int main() { 
	cin >> t;
	REP(i, t) { 
		CL(in_list); CL(can_combine); CL(can_oppose); l = 0;
		
		cin >> c;
		REP(j, c) { 
			cin >> s;
			x = s[0]; y = s[1]; z = s[2];
			can_combine[ x-'A' ][ y-'A' ] = z;
			can_combine[ y-'A' ][ x-'A' ] = z;
		}
		cin >> d;
		REP(j, d) { 
			cin >> s;
			x = s[0]; y = s[1];
			can_oppose[ x-'A' ][ y-'A' ] = true;
			can_oppose[ y-'A' ][ x-'A' ] = true;
		}
		
		//cout << "!" << endl;
		
		cin >> n; if (n) cin >> s;
		REP(j, n) { 
			x = s[j];
			char to_add = can_combine[ st[l-1]-'A' ][ x-'A' ];
			//cout << to_add << endl;
			if (l && to_add) { 
				in_list[ st[l-1]-'A' ]--;
				st[l-1] = to_add;
				in_list[ to_add-'A' ]++;
			} else { 
				bool flag = false;
				//cout << in_list['F'-'A'] << endl;
				for (int k = 0; k < 26; k++) if (can_oppose[ x-'A' ][k] && in_list[k]) { 
					l = 0; CL(in_list); flag = true;
				}
				if (!flag) { 
					st[l++] = x;
					in_list[ x-'A' ]++;
				}
			}
			
			if (j == n-1) { 
				printf("Case #%d: \[",i+1);
				REP(j, l) { 
					printf("%c",st[j]);
					if (j < l-1) printf(", ");
				}
				printf("]\n");
			}
		}		
	}
	
}