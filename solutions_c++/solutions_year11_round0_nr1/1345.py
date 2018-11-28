#include <cstdio>
#include <vector>
#include <cstdlib>
#include <iostream>
using namespace std;

int N,n;
int a[10000],z[10000];

int abs(int k) {
	return (k>0)?(k):(-k);
}

int get_next(int p,int x) {
	while (p<=n && a[p]!=x) p++;
//	printf("p %d\n",p); 
	return (p>n)?(-1):(p);
}

int main() {
	cin>>N;
	for (int I=1;I<=N;I++) {
		cin>>n;
		int b=1,o=1;
		int p;
		char c;
		for (int i=1;i<=n;i++) {
			cin>>c>>p;
			if (c=='B') a[i]=0; else a[i]=1;
			z[i]=p;
		}	
		int t,ans=0;
		for (int i=1;i<=n;i++) {
			if (a[i]==0) {
				t=abs(b-z[i])+1;
				int k=get_next(i,1);
				if (k!=-1) {
					if (o<z[k]) o=min(o+t,z[k]); else o=max(o-t,z[k]);
				}
				b=z[i];
			} else {
				t=abs(o-z[i])+1;
				int k=get_next(i,0);
//				printf("k %d\n",k);
				if (k!=-1) {
					if (b<z[k]) b=min(b+t,z[k]); else b=max(b-t,z[k]);
				}
				o=z[i];
			}
			ans+=t;
//			printf("%d %d %d %d\n",b,o,a[i],z[i]);
		}
		printf("Case #%d: %d\n",I,ans);
	}
}