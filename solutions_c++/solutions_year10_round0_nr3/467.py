#include <iostream>
using namespace std;

long long R,K,N,T;
long long a[1001];
long long da[1001];
long long ans;
bool check();
long long single(long long  r);
int round,pre,roundidx;
long long roundw,prew;
void make_round();
long long workw(int start);
int main() {
	freopen("f:\\c-small.in","r",stdin);
	freopen("f:\\c-small.out","w",stdout);
	cin>>T;
	for(int t=1;t<=T;t++) {
		cin>>R>>K>>N;
		for(int i=0;i<N;i++){
			cin>>a[i];
		}
		if(check()){
			ans = single(0);
			printf("Case #%d: %lld\n",t,ans);
			continue;
		}
		
		make_round();
		ans = 0;
		if(R<=pre){
			ans=workw(0);
		} else {
			R-=pre;
			ans+=prew;
			long long r = R/round;
			ans += r*roundw;
			R = R%round;
			ans+=workw(roundidx);
		}
		printf("Case #%d: %lld\n",t,ans);
	}
	return 0;
}
void make_round() {
	memset(da,-1,sizeof(da));
	int idx = 0,preidx;
	long long sum;
	da[0]=0;
	int r =0;
	while(true) {
		r++;
		sum = K;
		preidx=idx;
		while(sum>=a[idx]){
			
			sum-=a[idx];
			idx+=1;
			idx%=N;
			if(idx==preidx) break;
		}
		if(da[idx]!=-1){
			pre = da[idx];
			round=r-da[idx];
			roundidx=idx;
			break;
			
		} else {
			da[idx]=r;
		}
	}
	idx=0;
	prew=0;
	roundw=0;
	for(int i=0;i<pre;i++){
		long long sum = K;
		int preidx = idx;
		while(sum>=a[idx]){
			sum-=a[idx];
			prew+=a[idx];
			idx+=1;
			idx%=N;
			if(idx==preidx) break;
		}
	}
	idx = roundidx;
	for(int i=0;i<round;i++){
		long long sum = K;
		int preidx = idx;
		while(sum>=a[idx]){
			sum-=a[idx];
			roundw+=a[idx];
			idx+=1;
			idx%=N;
			if(idx==preidx) break;
		}
	}
}
long long workw(int start) {
	long long res = 0;
	int idx = start;
	int n = N;
	while(R--){
		long long sum =K;
		int preidx = idx;
		while(sum>=a[idx]){
			res+=a[idx];
			sum-=a[idx];
			idx+=1;
			idx%=n;
			if(idx==preidx) break;
		}
	}
	return res;
}

bool check() {
	for(int i=0;i<N;i++){
		if(K<a[i]) return true;
	}
	return false;
}
long long single(long long r) {
	long long res = r;
	long long sum =K;
	int inx =0;
	while(R--){
		sum = K;
		while(sum>=a[inx]){
			res+=a[inx];
			sum-=a[inx];
			inx+=1;
		}
		if(K<a[inx]) return res;
	}
	return res;
}

