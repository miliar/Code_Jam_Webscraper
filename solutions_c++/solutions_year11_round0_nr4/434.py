#include <stdio.h>
#include <algorithm>
using namespace std;

int dat[1000];
int main(){
	freopen("D-large.in","r",stdin);
	freopen("D-large.out","w",stdout);
	int T, n, i, j, k;
	scanf("%d",&T);
	while(T>0){T--;
		scanf("%d",&n);
		for(i=0;i<n;i++) scanf("%d",&dat[i]);
		double sol = 0.0;
		for(i=0;i<n;i++){
			if(dat[i] != -1){
				j = i;
				int cnt = 0;
				do{
					k = dat[j] - 1;
					dat[j] = -1;
					cnt ++;
					j = k;
				}while(j != i);
				if(cnt > 1){
					sol += (double)cnt;
				}
			}
		}
		static int cs = 1;
		printf("Case #%d: %.6lf\n", cs++, sol);
	}
	return 0;
}