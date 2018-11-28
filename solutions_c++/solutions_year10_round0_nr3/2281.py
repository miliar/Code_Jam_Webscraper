#include<cstdio>

int data[1005][3];

int main(){
	
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	
	int t;
	scanf("%d",&t);
	for(int ca = 0; ca < t; ++ca){
		int r,k,n;
		scanf("%d%d%d",&r,&k,&n);
		for(int i = 0 ; i < n; ++i){
			scanf("%d",&data[i][0]);
		}
		int sum = 0;
		for(int i = 0 ; i < n; ++i){
			sum = 0;
			for(int j = 0,pos = i+j; j < n ; ++j,++pos){
				if(pos == n){
					pos = 0;
				}
				sum += data[pos][0];
				if(sum <= k){
					data[i][1] = pos+1;
					if(data[i][1] == n){
						data[i][1] = 0;
					}
					data[i][2] = sum;
				}
			}
		}
		/*for(int i = 0; i < n; ++i){
			printf("%d %d %d\n",data[i][0],data[i][1],data[i][2]);
		}*/
		__int64 count = 0;
		for(int i = 0,pos = 0 ;i < r ;++i){
			count += data[pos][2];
			pos = data[pos][1];
		}
		printf("Case #%d: ",ca+1);
		printf("%I64d\n",count);
	}
	return 0;
}
