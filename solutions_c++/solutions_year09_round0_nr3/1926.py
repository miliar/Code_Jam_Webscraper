#include <stdio.h>
#include <string.h>
#include <memory.h>
char data[505];
const char msg[]="welcome to code jam";
int dt[505][20];
int main(){
	int i,j,k,l;
	int test;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d%*c",&test);
	
	for(i=0;i<test;i++){
		int ans = 0;
		gets(data);
		memset(dt,0,sizeof(dt));
		dt[0][0] = (data[0] == msg[0])?1:0;
		for(j=1;data[j];j++){
			dt[j][0] = ((data[j] == msg[0])?1:0) + dt[j-1][0];
			dt[j][0] %= 10000;
			for(k=1;msg[k];k++){
				dt[j][k] = dt[j-1][k];
				if(data[j] == msg[k]){
					dt[j][k] += dt[j-1][k-1];
				}
				dt[j][k] %= 10000;
			}
		}
		ans = dt[strlen(data)-1][18] % 10000;
		printf("Case #%d: %04d\n",i+1,ans);
	}
	return 0;
}
