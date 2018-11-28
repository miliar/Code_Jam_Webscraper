#include <stdio.h>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <memory.h>
#include <queue>
#include <string>
#include <string.h>
#include <cmath>
#include <utility>
#include <time.h>


typedef long long LL;
typedef unsigned long long ULL;

#define PI 3.1415926535897932384626433832795
#define sqr(x) ((x)*(x))
#define OUT_RT cerr << (float(clock()) / CLOCKS_PER_SEC) << endl

using namespace std;

int T;
int n,ma,mi;

/*void Rec(int sum,vector<int>& v,int col){
	bool good = true;
	for(int i=0;i<v.size();i++) if(sum % v[i]){
		Rec(sum + v[i] - (sum % v[i]), v, col + 1);
		good = false;
	}
	if(good){
		if(v.size() == n){
			if(col < mi) mi = col;
			if(col > ma) ma = col;
			return;
		}
		for(int i=1;i<=n;i++){
			int is = -1;
			for(int j=0;j<v.size();j++) if(v[j] == i){
				is = j;
				break;
			}
			if(is == -1){
				v.push_back(i);
				Rec(sum, v, col);
				v.pop_back();
			}
		}
			
	}
}            */

int D[1111],d[1111],pn,pr[1111];

int main(void){
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	scanf("%d\n",&T);
	for(int _=1;_<=T;_++){
		cin >> n;

		pn = 0;
		for(int i=2;i<=n;i++){
			bool bad = false;
			for(int j=0;j<pn;j++) if( (i % pr[j]) == 0){
				bad = true;
				break;
			}
			if(!bad) pr[pn++] = i;
		}

		int ma = 1, mi = 0;

		memset(D,0,sizeof(D));
		for(int i=2;i<=n;i++){
			memset(d,0,sizeof(d));
			int x = i;
			for(int j=0;j<pn;j++) while( (x % pr[j]) == 0){
				d[j]++;
				x/=pr[j];
			}
			bool ch = false;
			for(int j=0;j<pn;j++) if(d[j] > D[j]){
				D[j] = d[j];
				ch  = true;
			}
			if(ch) ma++;
		}

		if(n == 1) mi = 1;else{
			for(int j=0;j<pn;j++)
				if(D[j]>0)
					mi++;
		}/*
		for(int i=n;i>0;i--){
			memset(d,0,sizeof(d));
			int x = i;
			for(int j=0;j<pn;j++) while( (x % pr[j]) == 0){
				d[j]++;
				x/=pr[j];
			}
			bool ch = false;
			for(int j=0;j<pn;j++) if(d[j] > D[j]){
				D[j] = d[j];
				ch  = true;
			}
			if(ch) mi++;
		}      */
					
		printf("Case #%d: ",_);
		cout << ma - mi<< endl;
	}
	return 0;
}
