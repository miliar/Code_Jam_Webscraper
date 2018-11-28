#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <utility>
#include <algorithm>
#include <vector>

#define MAXN 10005

using namespace std;

pair<int,int> r[MAXN];
int tx[100], ty[100], n, cases, W, L;
double x[MAXN], y[MAXN];
bool mark[MAXN];
vector<int> nowmark;

inline double dist(int x1,int y1,int x2,int y2){
	return sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2));
}

int check(int rr,int xx,int yy){
	for(int i = 0; i < n; ++i)
		if(mark[i] && (dist(x[i],y[i],xx,yy)<(rr+r[i].first)))return false;
	return true;
}

long long getrandom(long long n){
	long long x = RAND_MAX;
	long long now = x;
	int cnt = 1;
	while(now < n){
		cnt ++;
		now = now * x;
	}
	long long res = 1;
	for(int i = 1; i <= cnt; ++i)
		res = res * rand();
	res = res % n;
	return res;
}

int main(){
	//freopen("test.txt","r",stdin);
	srand(time(0));
	scanf("%d",&cases);
	for(int xx = 1; xx <= cases; ++xx){
		memset(x,0,sizeof(x));
		memset(y,0,sizeof(y));
		memset(mark,0,sizeof(mark));
		scanf("%d%d%d",&n,&W,&L);
		for(int i = 0; i < n; ++i){
			scanf("%d",&r[i].first);
			r[i].first = -r[i].first;
			r[i].second = i;
		}
		//greedy to put some points
		sort(r, r + n);
		for(int i = 0; i < n; ++i)
			r[i].first = -r[i].first;

		tx[0] = 0;
		ty[0] = 0;
		tx[1] = 0;
		ty[1] = L;
		tx[2] = W;
		ty[2] = 0;
		tx[3] = W;
		ty[3] = L;

		for(int i = 0; i < n; ++i){
			for(int j = 0; j < 4; ++j)
				if(check(r[i].first,tx[j],ty[j])){
					mark[r[i].second] = true;
					x[r[i].second] = tx[j];
					y[r[i].second] = ty[j];
					break;
				}
		}
		int times = 0;
		int limited = 100;
		int cleared = n / 2;
		int findPt = 1000;
		while(times <= limited){
			// try to put
			times ++;
			for(int i = 0; i < n; ++i)
				if(!mark[r[i].second]){
					for(int kk = 0; kk <= findPt; ++kk){
					double nowx = getrandom(W*1LL*100+1LL) / 100;
					double nowy = getrandom(L*1LL*100+1LL) / 100;
					if(check(r[i].first,nowx,nowy)){
						mark[r[i].second] = true;
						x[r[i].second] = nowx;
						y[r[i].second] = nowy;
						break;
					}
					}
				}

			// check all
			bool ok = true;
			for(int i = 0; i < n; ++i)
				if(!mark[i]){
					ok = false;
					break;
				}

			if (ok) break;
			// clear some to reput
			nowmark.clear();
			for(int i = 0; i < n; ++i)
				if(mark[i])nowmark.push_back(i);
			random_shuffle(nowmark.begin(),nowmark.end());
			for(int i = 0; i < min((int)nowmark.size(),cleared); ++i)
				mark[nowmark[i]] = false;
		}

		//check all again
		for(int i = 0; i < n; ++i){
			mark[i] = false;
			if(check(
		}

		printf("Case #%d: ", xx);
		for(int i = 0; i < n - 1; ++i)
			printf("%.2lf %.2lf ", x[i], y[i]);
		printf("%.2lf %.2lf\n",x[n - 1], y[n - 1]);
	}
}
