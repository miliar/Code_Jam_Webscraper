#include<stdio.h>
#include<math.h>


int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("sample.out", "w", stdout);
	int T;
	int a,b,c,d[10];
	int bit,k,j;
	double e;
	int sum;
	scanf("%d",&T);

	for(int i=0;i<T;i++){
		scanf("%d%d",&a,&b);
		if(a<12)a=12;
		sum = 0;
		bit = 2;
		for(c=a;c<b;c++){
			while(c+0.5>pow(10,(double)bit))
				bit++;
			d[0]=c;
			
			for(j=1;j<bit;j++){
				d[j]= d[j-1]/10+(d[j-1]%10)*pow(10,(double)(bit-1));
				if(d[j]<=b&&d[j]>c){
					for(k=1;k<j;k++){
						if(d[j]==d[k]){
							sum--;
						}	
					}
					sum++;
				}
			}
		}

		printf("Case #%d: %d\n",i+1,sum);
	}
//	scanf("%d",&T);

	return 0;
}