#include <stdio.h>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;

map<int, int> su, af;
vector<int> hav, haf;
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T, C, t;
	scanf("%d",&T);
	for(t=1;t<=T;t++){
		scanf("%d",&C);
		int i, x, v;
		hav.clear();su.clear();
		for(i=0;i<C;i++){
			scanf("%d %d",&x,&v);
			if(su[x] == 0 && v > 0){
				hav.push_back(x);
			}
			su[x] += v;
		}
		int sol = 0;
		while(1){
			af.clear();
			haf.clear();
			bool flag = false;
			for(i=0;i<hav.size();i++){
				if(su[hav[i]] >= 2){
					if(af[hav[i]-1] == 0){
						haf.push_back(hav[i]-1);
					}
					if(af[hav[i]+1] == 0){
						haf.push_back(hav[i]+1);
					}
					af[hav[i]-1] += su[hav[i]]/2;
					af[hav[i]+1] += su[hav[i]]/2;
					sol += su[hav[i]]/2;
					flag = true;
				}
				if(su[hav[i]] % 2 == 1){
					if(af[hav[i]] == 0){
						haf.push_back(hav[i]);
					}
					af[hav[i]] ++;
				}
			}
			if(!flag) break;
			hav = haf;
			su = af;
		}
		printf("Case #%d: %d\n", t, sol);
	}
	return 0;
}