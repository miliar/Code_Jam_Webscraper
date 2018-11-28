#include <cstdio>
using namespace std;
#include <algorithm>
#include <iostream>
#include <string>

#define MAXD 5000
int l, d, n;
string s[MAXD];

int main(){
	freopen("input.txt", "rt", stdin);
	scanf("%d%d%d", &l, &d, &n);
	for (int i = 0; i < d; i++)
		cin>>s[i];
	for (int i = 0; i < n; i++){
		string a;
		cin>>a;
		int res = 0;
		for (int j = 0; j < d; j++){
			bool can = true;
			int pos = 0;
			for (int q = 0; q < l; q++){
				char ch = s[j][q];
				if (a[pos] == '('){
					pos++;
					bool y = false;
					while (a[pos] != ')'){
						if (a[pos] == ch) y = true;
						pos++;
					}
					pos++;
					if (!y) can = false;
				}
				else{
					if (ch != a[pos]) can = false;
					pos++;
				}	
			}
			if (can) res++;
		}
		printf("Case #%d: %d\n", i + 1, res);
	}
	return 0;
}
