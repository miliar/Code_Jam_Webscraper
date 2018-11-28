#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

const int maxn=1000100;

long long A,B,P;
long long ans;
long long f[maxn];

void gen(){
	ans=0;
	memset(f,0,sizeof(f));
	for (int i=A;i<B+1;++i) f[i]=i;
}

bool prime(int k){
	for (int i=2;i<k;i++)
		if (k%i==0) return false;
	return true;
}

void work(){
	if (P==1) P=2;
	for (int i=P;i<B+1;++i)
		if (prime(i))
			for (int x=A;x<B+1;++x)
				if (x%i==0){
					int y=x-i;
					if (y>=A&&y<=B){
						int xx=f[x],yy=f[y];
						while (xx!=f[xx]) xx=f[xx];
						while (yy!=f[yy]) yy=f[yy];
						if (xx!=yy){
							if (xx>yy) swap(xx,yy);
							f[yy]=xx;
						}
					}
				}
	for (int i=A;i<B+1;++i){
		int x=f[i];
		while (x!=f[x]) x=f[x];
		f[i]=x;
	}
	for (int i=A;i<B+1;++i)
		if (f[i]==i)
			++ans;
}

int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	int Q,Num=0;
	cin >> Q;
	while (Q--){
		cin >> A >> B >> P;
		gen();
		work();
		Num++;
		cout << "Case #" << Num << ": " << ans << endl;
	}

	return 0;
}