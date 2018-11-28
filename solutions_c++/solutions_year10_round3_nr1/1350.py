#include<cstdio>
#include<cstdlib>

int data[1005][2];

int cmp(const void *a,const void *b);

int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t;
	scanf("%d",&t);
	for(int ca = 0; ca < t ; ++ca){
		int n;
		scanf("%d",&n);
		for(int i = 0; i < n; ++i){
			scanf("%d%d",&data[i][0],&data[i][1]);
		}
		int temp[2];
		int count = 0;
		qsort(data,n,sizeof(int)*2,cmp);
		for(int i = 0; i < n; ++i){
			for(int j = i+1; j < n; ++j){
				//printf("%d %d\n",data[i][1],data[j][1]);
				if(data[i][1] > data[j][1]){
					temp[0] = data[i][0];
					temp[1] = data[i][1];
					data[i][0] = data[j][0];
					data[i][1] = data[j][1];
					data[j][0] = temp[0];
					data[j][1] = temp[1];
					count ++;
				}
			}
		}
		printf("Case #%d: %d\n",ca+1,count);
	}
	return 0;
}

int cmp(const void *a,const void *b){
	return ((int *)a)[0] - ((int *)b)[0];
}
