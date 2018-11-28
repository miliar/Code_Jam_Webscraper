#include <cstdio>
int t,n,s,p;
int main(){
	freopen("BL.in","r",stdin);
	freopen("BL.out","w",stdout);
	scanf("%d",&t);
	for(int i =1 ;i <=t;i ++){
		scanf("%d%d%d",&n,&s,&p);
		int sum;
		int count = 0;
		for(int k = 0;k < n;k ++){
			scanf("%d",&sum);
			int base = sum / 3;
			int r = sum % 3;
			switch(r){
				case 0:
				{
					//base,base,base
					//base-1,base,base+1
					if(p <= base)
						count ++;
					else if(s > 0 && base > 0 && base + 1 >= p){
						count ++;
						s --;
					}
					break;
				}
				case 1:
				{
					// base ,base ,base+ 1
					// base-1,base + 1,base +1
					if(base + 1 >= p)
						count ++;
					else if(s > 0 && base >0 && base + 1>=p){
						count ++;
						s --;
					}
					break;
				}
				case 2:
				{
					//base ,base,base +2;
					//base,base +1,base+1;
					if(base + 1 >= p)
						count ++;
					else if(s>0 && base + 2 >= p){
						count ++;
						s --;
					}
					break;
				}
			}
		}
		printf("Case #%d: %d\n",i,count);
	}
	return 0;
}