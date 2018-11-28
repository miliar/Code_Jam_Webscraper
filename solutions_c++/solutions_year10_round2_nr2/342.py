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

int v[55],x[55];

bool ok[55];

int main() {
	int testow;
	scanf("%d",&testow);
	for(int z=1;z<=testow;++z) {
		int wynik=0;
		int n,k,b,czas;
		scanf("%d%d%d%d",&n,&k,&b,&czas);
		for(int i=0;i<n;++i)
			scanf("%d",x+i);
		for(int i=0;i<n;++i) {
			scanf("%d",v+i);
			ok[i]=false;
		}
		for(int i=n-1;i>=0 && k>0;--i) {
			//printf("i=%d\n",i);
			if((b-x[i])<=czas*v[i]) {
				ok[i]=true;
				//printf(" ok\n");
				--k;
			}
			if(ok[i]) {
				for(int j=i+1;j<n;++j) {
					if(!ok[j]) {
						//printf("  j=%d ++wynik\n",j);
						++wynik;
					}
				}
			}
		}
		
		if(k>0)
			printf("Case #%d: IMPOSSIBLE\n",z);
		else
			printf("Case #%d: %d\n",z,wynik);
	}
}
