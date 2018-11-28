#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

const int maxn=1000100;

long long A,B,P;
long long ans;
long long a[maxn];

void gen(){
	ans=0;
	memset(a,0,sizeof(a));
	for (int i=A;i<B+1;++i) a[i-A]=i;
}

int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	int Q,Num=0;
	cin >> Q;
	while (Q--){
		cin >> A >> B >> P;
		gen();
		Num++;
		cout << "Case #" << Num << ": " << ans << endl;
	}

	return 0;
}