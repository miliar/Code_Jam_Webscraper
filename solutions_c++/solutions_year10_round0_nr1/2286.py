#include<iostream>
#include<cstring>
#include<string>
#include<math.h>
#include<vector>
#include<map.h>
#include<algorithm>
bool power[32];
bool state[32];
int n,k;
int main(){
	freopen("A-small.in","r",stdin);freopen("A-small.out","w",stdout);
	//freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);
	int ncases=0;
	scanf("%d",&ncases);
	for(int cc=1;cc<=ncases;cc++){
		scanf("%d %d", &n,&k);
		for(int i=0;i<=n;i++){
			power[i]=false;state[i]=false;
		}
		power[0]=true;
		power[1]=true;
		state[0]=true;
		for(int i=0;i<k;i++){
			for(int j=1;j<=n;j++){
				if(power[j]==true){
					state[j]=!state[j];
				}
			}
			for(int j=1;j<=n;j++){
				power[j]=false;
			}
			for(int j=1;j<=n;j++){
				if(state[j-1]&&power[j-1]){
					power[j]=true;
				}else{
					break;
				}
			}
		}
		if(power[n]==true&&state[n]==true){
			printf("Case #%d: ON\n",cc);
		}else{
			printf("Case #%d: OFF\n",cc);
		}
	}
}