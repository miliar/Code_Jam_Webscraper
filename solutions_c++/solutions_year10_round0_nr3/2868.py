#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

long long R,k,N;
const int maxn = 10000005;
int g[maxn];
long long money[maxn];
int next[maxn];

void init(){
	memset(money,0,sizeof(money));
	memset(next,0,sizeof(next));
	for(int i =0;i<N;i++){
		long long now = 0,j;
		for(j = i;now+g[j%N]<=k;){
			now += g[j%N];
			j++;
			if(j>=N){
				if(i+N<=j) break;
			}
		}
		money[i] = now;
		next[i] = j%N;
	}
}

long long solve(){
	cin >> R >> k >> N;
	for(int i = 0;i<N;i++){
		cin >> g[i];
	}

	init();

	long long ret = 0;

	int now = 0;
	for(int i = 0;i<R;i++){
		ret += money[now];
		now = next[now];
	}

	return ret;
}

int main(){
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);

	int n;
	cin >> n;
	for(int i = 1;i<=n;i++){
		cout << "Case #" << i << ": " << solve() << endl;
	}
	return 0;
}
