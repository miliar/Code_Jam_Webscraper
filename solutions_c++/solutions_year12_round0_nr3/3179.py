#include <cstdio>
int a,b,t;
int main(){
	freopen("c.in", "r", stdin);
    freopen("c.out", "w", stdout);
	scanf("%d",&t);
	for(int i =1;i <=t;i ++){
		scanf("%d%d",&a,&b);
		int count = 0;
		for(int k = a; k <=b;k ++){
			if(k>100){
				int r = k % 10;
				int q = k / 10;
				if(r * 100 + q <=b && r * 100 + q > k)
					count ++;
				r = k % 100;
				q = k / 100;
				if(r * 10 + q <=b && r * 10 + q > k)
					count ++;
			}
			else if(k < 100){
				int r = k % 10;
				int q = k / 10;
				if(r * 10 + q <=b&& r * 10 + q > k)
					count ++;
			}
		}
		printf("Case #%d: %d\n",i,count);
	}
	return 0;
}