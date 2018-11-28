#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cassert>
#include<string>
#include<algorithm>
#include<fstream>
#include<sstream>
#include<set>
#include<map>
#include<vector>
#include<queue>
#include<deque>
#include<complex>
#include<numeric>
using namespace std;

#define LL long long

int a[10000];
int N;
int pr[2000], s[2000];

int add(int k) {
	bool flag=false;
	for(int i=2;i<=k;++i) {
		if(k%i!=0) continue;
		if(!pr[i]) continue;
		int m = 0;
		while(k%i==0) k/=i,++m;
		if(m > s[i]) {
			flag = true;
			s[i] = m;
		}
	}
	return flag;
}

int calc(int *a) {
	fill(s, s + N + 2, 0);
	int res=0;
	for(int i=0;i<N;++i)
		if(add(a[i])) {
			++res;
		} else
		if(!i) ++ res;
return res;
}

int run() {
	scanf("%d", &N);
	if(N == 1) return 0;
	LL cur=1;
	for(int i=0;i<N;++i) a[i]=i+1;
	int res = calc(a);
	
//	cout << "---> Increase = "<<res<<endl;
	
	int tmp = 0;
	for(int i=2;i<=N;++i)
		if(pr[i]) ++ tmp;
	
//	cout << "     dec = "<<tmp<<endl;
	
	res -= tmp;
	return res;
}

int main() {
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	fill(pr+2,pr+2000,1);
	for(int i=2;i<2000;++i)
		if(pr[i]) {
			for(int j=i+i;j<2000;j+=i)
				pr[j] = false;
		}
	int test; scanf("%d", &test);
	for(int no=1;no<=test;++no){
		printf("Case #%d: %d\n", no, run());
	}
}
