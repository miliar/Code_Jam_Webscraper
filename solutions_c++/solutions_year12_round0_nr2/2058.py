#include <cstdio>
#include <cstring>

int cases,n,m,p,a[105];

int main(){
	scanf("%d",&cases);
	for(int xx = 1; xx <= cases; ++xx){
		scanf("%d%d%d",&n,&m,&p);
		for(int i = 0; i < n; ++i)
			scanf("%d",&a[i]);
		//sort(a, a + n);
		int ans = 0;
		for(int i = 0; i < n; ++i){
			int avg = a[i] / 3;
			if (avg >= p) ans++;
			else{
				int ys = a[i] - avg * 3;
				if (ys == 0){
					if (avg + 1 >= p && avg > 0 && m > 0){
						m--;
						ans++;
					}
				}else if (ys ==1){
					if (avg + 1 >= p)
						ans++;
				}else{
					if(avg + 1 >= p){
						ans++;
					}else if (avg + 2 >= p && m > 0){
						m--;
						ans++;
					}
				}

			}
		}
		printf("Case #%d: %d\n",xx,ans);
	}
}
