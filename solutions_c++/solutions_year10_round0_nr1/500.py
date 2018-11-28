//Jakub Sygnowski
#include <cstdio>
int t,n,k;
bool of;
int main(){
	scanf("%d",&t);
	for(int nr=0;nr<t;nr++){
		printf("Case #%d: ",nr+1);
		scanf("%d%d",&n,&k);
		of=false;
		while(n--){
			if (!(k%2)){
				printf("OFF\n");
				of=true;
				break;
			}
			k/=2;
		}
		if (!of)
			printf("ON\n");
	}
}
