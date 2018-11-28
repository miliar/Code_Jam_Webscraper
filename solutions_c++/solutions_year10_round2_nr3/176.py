#include<iostream>
#define MOD 100003
using namespace std;
long long c[1000][1000];
int m[1000][1000];

int f(int n, int p) {
	if(p==1) return 1;
	if(p>=n) return 0;
	if(m[n][p]) return m[n][p];
	int nn = p, pp;
	int ans = 0;
	for(pp=1;pp<p;pp++) {
		ans = ( ans + (c[n-nn-1][p-pp-1] * f(nn,pp))%MOD ) % MOD;
	}
	return m[n][p] = ans;
}

int main() {
    int t,Ts,N,K,B,T,i,j,cnt,tot;
    
    c[0][0] = 1;
    for(i=1;i<1000;i++) {
		c[i][0] = c[i][i] = 1;
		for(j=1;j<i;j++) c[i][j] = (c[i-1][j-1] + c[i-1][j])%MOD;
	}
    
    cin>>Ts;
    for(t=1;t<=Ts;t++) {
		cin>>N;
		tot = 0;
		for(i=1;i<N;i++) tot = ( tot + f(N,i) ) % MOD;
		cout<<"Case #"<<t<<": "<<tot<<endl;
    }
    return 0;
}
