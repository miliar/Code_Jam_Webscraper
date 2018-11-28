#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <map>
#include <algorithm>

using namespace std;

const int nmax = 5005;

string words[nmax];
int pat[20][500];

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int l,d,n;
	cin >> l >> d >> n;
	for (int i = 0;i < d; ++i) cin >> words[i];

	for (int test = 1;test <= n; ++test){
		string s;
		cin >> s;	
		memset(pat,0,sizeof(pat));

		int pos = 0;

		for (int i = 0;i < l; ++i){
			if (s[pos] == '('){
				++pos;
				while (s[pos] != ')'){
					pat[i][s[pos]] = 1;
					++pos;
				}
				++pos;
			}
			else {
				pat[i][s[pos]] = 1;
				++pos;
			}
		}		
		int ans = 0;
		for (int i = 0;i < d; ++i){
			bool ok = true;
			for (int j = 0;j < l; ++j)
				if (pat[j][words[i][j]] == 0){
					ok = false;
					break;
				}
			if (ok) ++ans;
		}
		printf("Case #%i: %i\n",test,ans);

	}
	
	return 0;
}