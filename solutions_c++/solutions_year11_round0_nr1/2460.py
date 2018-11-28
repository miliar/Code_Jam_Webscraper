#include <iostream>
#define X first
#define Y second
#define forn(i, n) for(int i = 0; i < int(n); i++)

using namespace std;
typedef pair<int, int> pt;
int n;

pt b[200];

int main(){
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int tests;
	cin >> tests;
	forn(test, tests){
		cin >> n;
		
		forn(i, n){
			char c;
			int x;
			scanf(" %c %d", &c, &x);
			if(c == 'O'){
				
				b[i].X = 0;
			}
			else{
				
				b[i].X = 1;
			}
			b[i].Y = x;
		}
		int ans = 0;
		int st[2], tm[2];
		st[0] = 1, st[1] = 1;
		tm[0] = tm[1] = 0;
		forn(i, n){
			int cur = abs(b[i].Y - st[b[i].X]);
			cur = max(0, cur - ans + tm[b[i].X]);
			cur++;
			st[b[i].X] = b[i].Y;
			ans += cur;
			tm[b[i].X] = ans;
			
		}
		printf("Case #%d: %d\n", test + 1, ans);
	}
}