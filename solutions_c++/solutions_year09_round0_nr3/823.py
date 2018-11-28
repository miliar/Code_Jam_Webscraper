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
using namespace std;

#define Eo(x) { std::cerr << #x << " = " << x << std::endl; }

char buf[1000000];

const int maxl = 509;
const int maxt = 20;
int num[maxl][maxt];

string RRR("welcome to code jam");

const int MOD = 10000;

int main(){
	int T; cin >> T;
	gets(buf);
	for (int _ = 0; _ < T; _++){
		gets(buf);
		string all(buf);

		memset(num,0,sizeof(num));
		int p = 0;
		for (int j = all.size()-1; j >= 0; j--){
			if (all[j] == 'm') p++;
			num[j][RRR.size()-1] = p;
		}
		for (int i = RRR.size()-2; i >= 0; i--){
			p = 0;
			for (int j = all.size()-1; j >= 0; j--){
				if (j+1 >= all.size()) continue;
				if (all[j] != RRR[i]){
					num[j][i] = p;
					continue;
				}
				p += (num[j+1][i+1]);
				p %= MOD;
				num[j][i] = p;
			}
		}

		int res = num[0][0];

		printf("Case #%d: %04d\n",_+1,res);
	}
	return 0;
}

