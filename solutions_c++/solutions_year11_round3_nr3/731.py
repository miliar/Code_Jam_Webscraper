#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <queue>
#include <map>
#include <algorithm>
#include <utility>
#include <cmath>

using namespace std;

int l, h, in[200];

int main(){
	int casos; scanf("%d", &casos);
	int caso = 1;
	int n;
	while(casos--){
		printf("Case #%d: ", caso++);
		scanf("%d%d%d", &n, &l, &h);
		for(int i = 0; i <n ;++i){
			scanf("%d", &in[i]);
		}
		for(int i = l; i <= h; ++i){
			
			for(int j = 0; j < n; ++j){
				if((in[j]%i ==0 ) || (i%in[j] == 0) ){
					
				}else{
					goto cont;
				}
			}
			printf("%d\n", i);
			goto cont2;
			cont:;
		}
		printf("NO\n");
		cont2:;
	}
	
	return 0;
}