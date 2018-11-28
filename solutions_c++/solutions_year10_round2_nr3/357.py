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

int wyniki[33]={},t[33];

int main() {
	int testow;
	scanf("%d",&testow);
	for(int z=1;z<=testow;++z) {
		int wynik=0;
		int x,n,nn;
		scanf("%d",&x);
		if(wyniki[x]!=0) {
			wynik=wyniki[x];
			goto koniec;
		}
		n=x-2;
		nn=1<<n;
		for(int i=0;i<nn;++i) {
			int poz=1;
			for(int j=0;j<n;++j) {
				if((1<<j)&i) {
					t[j+2]=poz++;
				} else {
					t[j+2]=-1;
				}
			}
			t[x]=poz;
			int y=x;
			for(;y>1;) {
				y=t[y];
			}
			if(y==1)
				++wynik;
		}
		wyniki[x]=wynik;
		koniec:;
		printf("Case #%d: %d\n",z,wynik%100003);
	}
}
