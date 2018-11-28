#include<stdio.h>
#include<string.h>
bool check[2000005];
int main(){
	int T;
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	scanf("%d",&T);
	for(int Case = 1 ; Case <= T ; ++Case){
		int n,m,result=0;
		scanf("%d%d",&n,&m);
		for(int i = n ; i <= m ; ++i){
			char temp[10]={0};
			memset(check, 0, sizeof(check));
			sprintf(temp,"%d",i);
			int len = strlen(temp);
			for(int j = 0 ; j < len ; ++j){
				char temp1=temp[0];
				for(int k = 0 ; k < len-1 ; ++k)
					temp[k]=temp[k+1];
				
				temp[len-1]=temp1;
				int tempResult;
				sscanf(temp,"%d",&tempResult);
				if(i<tempResult && n<=tempResult && tempResult<=m && temp[0]!='0' && !check[tempResult]){
						result++;
						check[tempResult]=true;
				}
			}
		}
		printf("Case #%d: %d\n",Case,result);
	}
	return 0;
}