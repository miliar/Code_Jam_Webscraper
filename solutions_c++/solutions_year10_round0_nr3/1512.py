#include<cstdio>
#include<algorithm>
#include<vector>
#include<string>
#include<cmath>
using namespace std;

const int INF=1000111222;

typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vi;

int t[1003],p[1003];
ll w[1003];

int main() {
	int testow;
	scanf("%d",&testow);
	for(int z=1;z<=testow;++z) {
		ll wynik=0;
		int r,k,n;
		scanf("%d%d%d",&r,&k,&n);
		for(int i=0;i<n;++i) {
			scanf("%d",t+i);
		}
		for(int i=0;i<n;++i) {
			w[i]=0;
			p[i]=i;
			for(int j=0;j<n;++j) {
				int ij=(i+j)%n;
				if(w[i]+t[ij]<=(ll)k) {
					w[i]+=t[ij];
					p[i]=(i+j+1)%n;
				} else
					break;
			}
			//printf("i=%d w=%lld p=%d\n",i,w[i],p[i]);
		}
		for(int i=0,pos=0;i<r;++i) {
			wynik+=w[pos];
			pos=p[pos];
		}
		printf("Case #%d: %lld\n",z,wynik);
	}
}
