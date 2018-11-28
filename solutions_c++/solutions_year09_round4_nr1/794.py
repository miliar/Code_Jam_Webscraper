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

char stemp[88];
int t[88];

int main() {
	int testow;
	scanf("%d",&testow);
	for(int z=1;z<=testow;++z) {
		int wynik=0;
		int n;
		scanf("%d",&n);
		for(int i=0;i<n;++i) {
			scanf("%s",stemp);
			t[i]=-1;
			for(int j=0;j<n;++j)
				if(stemp[j]=='1')
					t[i]=j;
			//printf("i=%d t[i]=%d\n",i,t[i]);
		}
		for(int i=0;i<n;++i) {
			if(t[i]<=i)
				continue;
			for(int j=i+1;;++j) {
				if(t[j]<=i) {
					for(int k=j;k>i;--k) {
						++wynik;
						swap(t[k],t[k-1]);
					}
					break;
				}
			}
		}
		printf("Case #%d: %d\n",z,wynik);
	}
}
