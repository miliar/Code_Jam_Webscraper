#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <vector>
#include <map>
#include <string>
#include <cstring>

using namespace std;

int t,n;
int num[22];

int main(){
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	int caso = 0;
	
	scanf("%d", &t);
	
	while(t--){
		printf("Case #%d:\n", ++caso);
		scanf("%d", &n);
		for(int i = 0; i < n; ++i){
			scanf("%d", num+i);
		}
		int lim = 1<<n;
		for(int i = 1; i < lim; ++i){
			for(int mask = (i-1)&i; mask; mask = (mask-1)&i){
				int soma = 0;
				for(int j = 0; j < 20; ++j){
					if(i&(1<<j)){
						if((mask)&(1<<j)){
							soma += num[j];
						}
						else soma -= num[j];
					}
				}
				if(soma == 0){
					bool impri = false;
					for(int j = 0; j < 20; ++j){
						if(i&(1<<j)){
							if(mask&(1<<j)){
								if(impri) printf(" ");
								impri = true;
								printf("%d", num[j]);
							}
						}
					}
					impri = false;
					printf("\n");
					for(int j = 0; j < 20; ++j){
						if(i&(1<<j)){
							if(!(mask&(1<<j))){
								if(impri) printf(" ");
								impri = true;
								printf("%d", num[j]);
							}
						}
					}
					printf("\n");
					goto sai;
				}
			}
		}
		printf("Impossible\n");
		sai:;
	}
	return 0;
}
