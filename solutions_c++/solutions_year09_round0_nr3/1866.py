//메모이제이션?!
#include<stdio.h>
#include<string.h>
char Sol[]="welcome to code jam";
char Temp[600];
int Len,T[600];
int Res,List[1000][1000];
void DFS(int Index,int w){
	int i;
	if(Index==19){
		Res++;
		Res%=10000;
		return;
	}
	int k;
	if(Sol[Index] == ' ') k=26;
	else k=Sol[Index] - 'a';
	for(i = 1 ; i <= List[ k ][ 0 ] ; i++){
		if(w<List[k][i]) DFS(Index+1,List[k][i]);
	}
}
int main(){
	int Case;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d\n",&Case);
	for(int I = 1 ; I <= Case ; I++){
		gets(Temp);
		Len=strlen(Temp);
		int i;
		memset(List,0,sizeof(List));
		for(i = 0 ; i < Len ; i++){
			if(Temp[i] == ' ') List[ 26 ][ ++List[26][0] ] = i;
			else List[ Temp[i]-'a' ][ ++List[ Temp[i]-'a' ][ 0 ] ] = i;
		}
		Res=0;
		for(i = 1 ; i <= List[ 'w' - 'a' ][ 0 ] ; i++){
			DFS(1,List['w'-'a'][i]);
		}
		printf("Case #%d: %04d\n",I,Res%10000);
	}
	return 0;
}