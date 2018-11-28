#include<iostream>
using namespace std;

const int PNUM=78498;
typedef long long i64;

bool table[1000001];
int plst[PNUM],ps;

int solve(i64 n) {
	int i,p,ret=1;
	if(n==1)return 0;
	for(i=0;i<ps;i++) {
		p=plst[i];
		i64 now=p;
		while(true) {
			if(now>n/p)break;
			now*=p;
			ret++;
		}
	}
	return ret;
}

void build() {
	int i,j;
	for(i=2;i<=1000000;i++)table[i]=true;
	for(i=2;i<=1000000;i++) {
		if(!table[i])continue;
		plst[ps++]=i;
		j=2*i;
		while(j<=1000000) {
			table[j]=false;
			j+=i;
		}
	}
}

int main() {
	int T,S; i64 n;
	build();
	cin>>T;
	for(S=1;S<=T;S++) {
		cin>>n;
		cout<<"Case #"<<S<<": "<<solve(n)<<endl;
	}
	return 0;
}
