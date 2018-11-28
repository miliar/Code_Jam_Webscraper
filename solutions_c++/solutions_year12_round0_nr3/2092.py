#include <cstdio>
#include <cstring>
#include <map>

using namespace std;

int cases, A, B, gg[1005];
map<int,int> gao;

int main(){
	scanf("%d",&cases);
	for(int xx = 1; xx <= cases; ++xx){
		scanf("%d%d",&A,&B);
		int ans = 0;
		for(int i = A; i <= B; ++i){
			gao.clear();
			int x = i;
			memset(gg,0,sizeof(gg));
			int zz = 0;
			while(x != 0){
				gg[zz] = x % 10;
				zz++;
				x = x / 10;
			}
			for(int j = 0; j < zz; ++j)
				if(gg[j] != 0){
					int zz2 = j - 1;
					zz2 = (zz2 + zz) % zz;
					int tot = gg[j];
					while(zz2 != j){
						tot = tot * 10 + gg[zz2];
						--zz2;
						zz2 = (zz2 + zz) % zz;
					}
					
					if(tot > i && tot <= B && (gao.count(tot)==0)){
						gao[tot] = 1;
						++ans;
					}
				}
		}
		printf("Case #%d: %d\n",xx,ans);
	}
}
