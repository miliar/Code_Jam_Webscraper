#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>

using namespace std;

#define Eo(x) { cerr << #x << " = " << (x) << endl; }

typedef long long int64;

const int maxn = 1024;
char was[maxn];
int a[maxn];

int64 stupid(int r,int k, int n){
	int64 profit = 0;
	int x = 0;
	for (int i = 0; i < r; i++){
		int64 has = 0;
		for (int j = 0; j < n; j++){
			if (has + a[x] > k) break;
			has += a[x];
			x = (x+1)%n;
		}
		profit += has;
	}
	return profit;
}

int64 smart(int r, int k, int n){
		vector<int64> part;
		int x = 0;
		memset(was,0,sizeof(was));
		int cnt = 0;
		int64 bablo = 0;
		part.push_back(bablo);
		for (;;cnt++){
			if (was[x]) break;
			was[x] = cnt+1;
			int64 has = 0;
			for (int j = 0; j < n; j++, x = (x+1)%n){
				if (has+a[x] > k) break;
				has += a[x];
			}
			bablo += has;
			part.push_back(bablo);
		}
		int64 predperiod = was[x]-1;
		int64 period = cnt-predperiod;
		int64 profit = 0;
//		Eo(predperiod);Eo(period);
		if (r >= predperiod){
			profit += part[predperiod];
			r -= predperiod;
			int64 pers = r/period;
//			Eo(pers);
			int64 babloperiod = part[period + predperiod] - part[predperiod];
//			Eo(part[predperiod]);Eo(babloperiod);
			profit += babloperiod * pers;
			r %= period;
			profit += part[predperiod+r]-part[predperiod];
		} else {
			profit += part[r];
		}
		return profit;
}

int main(){
	int T; cin >> T;
	for (int _ = 0; _ < T; _++){
		Eo(_);
		int r,k,n;
		cin >> r >> k >> n;
		for (int i = 0; i < n; i++)
			scanf("%d",&a[i]);
//		int64 ss = stupid(r,k,n);
//		Eo(ss);
		int64 tt = smart(r,k,n);
		Eo(tt);
		
//		assert(ss==tt);
		printf("Case #%d: ",_+1);
		cout << tt << endl;
	}
	return 0;
}
