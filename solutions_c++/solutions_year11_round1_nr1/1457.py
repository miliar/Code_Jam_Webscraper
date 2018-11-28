#include <cstdio>

using namespace std;

int main()
{
	int t;
	int q=1;
	int n, pd, pg;
	scanf("%d", &t);
	while(t){
		bool f=0;
		printf("Case #%d: ", q);
		
		scanf("%d %d %d", &n, &pd, &pg);
		if(pg>0)
			if(pd > 0 && pd<=100 && pg<100)
		for(int i=1; i<=100 && i<=n; i++){
			double tmp;
			tmp = i*pd/100;
			if((i*pd)%100==0){
				printf("Possible\n");
				f=1;
				break;
			}
			
		}
		if(pd==100 && pg==100){
			printf("Possible\n");
			f=1;
		}
		if(pd==0 && pg<100){
			printf("Possible\n");
			f=1;
		}
			
		if(f==0)
			printf("Broken\n");
		
		t--;
		q++;
	}
}