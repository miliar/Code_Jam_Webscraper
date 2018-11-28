#include <iostream>
#include <string>
#define forn(i, n) for(int i = 0; i < int(n); i++)
using namespace std;
char b[300][300];
bool d[300][300];
char ans[300];
int szans = 0;
int main(){
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt",stdout);
	int tests;
	string s;
	cin >> tests;
	forn(test, tests){
		int n;
		cin >> n;
		memset(b, 0, sizeof b);
		memset(d, 0, sizeof d);
		forn(i, n){
			char c1, c2, c3;
			scanf(" %c%c%c", &c1, &c2, &c3);
			b[c1][c2] = b[c2][c1] = c3;
		}
		cin >> n;
		forn(i, n){
			char c1, c2;
			scanf(" %c%c", &c1, &c2);
			d[c1][c2] = d[c2][c1] = true;
		}
		scanf("%d\n", &n);
		getline(cin, s);
		szans = 0;
		forn(i, n){
			
			if(i == 0){
				ans[szans++] = s[i];
				continue;
			}
			bool good = true;
			if(b[s[i]][ans[szans - 1]] != 0){
				ans[szans - 1] = b[s[i]][ans[szans - 1]];
				good = false;
			}
			else{
				forn(j, szans)
					if(d[ans[j]][s[i]]){
						szans = 0;
						good = false;
						break;
					}
			}
			if(good){
				ans[szans++] = s[i];
			}
		}
		ans[szans] = 0;
		printf("Case #%d: [", test + 1);
		forn(i, szans){
			printf("%c", ans[i]);
			if(i != szans - 1)
				printf(", ");
		}
		printf("]\n");
	}
	return 0;
}