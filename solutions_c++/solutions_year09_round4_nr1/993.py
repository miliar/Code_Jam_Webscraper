#include <cstdio>
#include <algorithm>
#include <vector>
#include <stack>
#include <set>
#include <map>
using namespace std;


int ntc,n;
int wyn=0;
char tab[50][50];
int r[50];

int main() {
	scanf("%d", &ntc);
	for(int cas=1; cas<=ntc; ++cas) {
		scanf("%d", &n);
		wyn=0;
		for(int i=1;i<=n; ++i) {
			scanf("%s", tab[i]+1);
			r[i]=0;
			for(int j=1; j<=n; ++j) { tab[i][j]-='0'; if(tab[i][j]) r[i]=j;}
		}
		for(int i=1; i<=n; ++i) {
			if(r[i]<=i) continue;
			else {
				int best = 0; 
				for(int j=i+1; j<=n; ++j) if(r[j]<=i) { best = j; break; }
				wyn+=best-i;
				int temp=r[best];
				for(int j=best-1; j>=i; --j) r[j+1]=r[j];
				r[i]=temp;
			}
		}
		printf("Case #%d: %d\n", cas, wyn);
	}
		
		 

}
