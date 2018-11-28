#include <cstdio>
#include <algorithm>

using namespace std;
int main(){
	int t = 0, c = 0;
	scanf("%d", &t);
	FILE *f = fopen("c_out.txt", "w");
	while(c++ < t){
		int n = 0;
		scanf("%d", &n);
		int numbs[n];
		for(int i = 0; i < n; i++) scanf("%d", &numbs[i]);
		sort(numbs, numbs + n);
		int xp_sum = 0, xs_sum = 0, p_cand = 0, s_cand = 0, lim = 1;
		bool can = true, cry = true;
		while(can && cry){
			for(int i = 0; i < n; i++){
				if(i < lim){
					p_cand += numbs[i];
					xp_sum = xp_sum ^ numbs[i];
				}else{
					s_cand += numbs[i];
					xs_sum = xs_sum ^ numbs[i];
				}
			}
			can = (s_cand > p_cand)? true : false;
			cry = (xp_sum == xs_sum)? false : true;
			p_cand = 0; s_cand = (!cry)? s_cand : 0; xp_sum = 0; xs_sum = 0;
			lim++;
		}
		if(!cry){
			printf("Case #%d: %d\n", c, s_cand);
			fprintf(f, "Case #%d: %d\n", c, s_cand);
		}else{
			printf("Case #%d: NO\n", c);
			fprintf(f, "Case #%d: NO\n", c);
		}
	}
	return 0;
}