#include<stdio.h>
#include<algorithm>
char data[5005][30],Temp[1500];
int Res,List[30][30];
int l,d,n;
void DFS(int Index){
}
int main(){
	int i;
	freopen("input_la.txt","r",stdin);
	freopen("output_la.txt","w",stdout);
	scanf("%d%d%d",&l,&d,&n);
	for(i = 1 ; i <= d ; i++){
		scanf("%s",data[i]);
	}
	for(i = 1 ; i <= n ; i++){
		scanf("%s",Temp);
		int Len = strlen(Temp), j, Index=0;
		bool Check=false;
		memset(List,0,sizeof(List));
		for(j = 0; j < Len ; j++){
			if(Temp[j]=='(') Check=true;
			else if(Check==true && Temp[j]==')'){
				Check=false;
				Index++;
			}
			else if(Check==true) List[ Index ][ Temp[j]-'a' ] = 1;
			else{
				List[ Index ][ Temp[j]-'a' ] = 1;
				Index++;
			}
		}
		Res=0;
		for(int k = 1 ; k <= d ; k++){
			Len = strlen(data[k]);
			for(j = 0 ; j < Len ; j++){
				if(List[ j ][ data[k][j]-'a' ]==0) break;
			}
			if(j==Len) Res++;
		}
		printf("Case #%d: %d\n",i,Res);
	}
	return 0;
}