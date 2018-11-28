#include <cstdio>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <string>
#include <cassert>

typedef long long int64;
typedef double real;

const int inf = 0x3f3f3f3f;

#define Eo(x) { std::cerr << #x << " = " << x << std::endl; }
#define tname "counterexample"

using namespace std;

const int maxn = 5002;
string a[maxn];

const int maxl = 30;
char can[maxl][maxl];

int main(){
	int l,d,n;
	cin >> l >> d >> n;
	for (int i = 0; i < d; i++){
		cin >> a[i];
	}
	for (int i = 0 ; i < n; i++){
		string p; cin >> p;
		memset(can,0,sizeof(can));
		int k = 0;
		for (int l = 0; l < p.length();){
			if (p[l] == '('){
				l++;
				while (p[l] != ')'){
					can[k][p[l]-'a'] = 1;
					l++;
				}
				l++;
			} else {
				can[k][p[l]-'a'] = 1;
				l++;
			}
			k++;
		}

		int res = 0;
		for (int j = 0; j < d; j++){
			bool good = true;
			for (int l = 0; l < a[j].length(); l++){
				if (!can[l][a[j][l]-'a']){
					good = false;
					break;
				}
			}
			if (good) res++;
		}
		printf("Case #%d: %d\n",i+1,res);
	}
	return 0;
}

