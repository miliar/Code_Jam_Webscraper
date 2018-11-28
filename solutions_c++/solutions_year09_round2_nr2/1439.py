#pragma warning(disable:4786)
#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<set>
using namespace std;
set<int>Set;
char Temp[25];
int Count[10],Len,Check[10];
void Rec(int Index, int Value){
	if(Index==Len){
		Set.insert(Value);
		return;
	}
	int i;
	for(i = 0 ; i <= 9 ; i++){
		if(Index==0 && i==0) continue;
		if(Count[i]-Check[i]>0){
			Check[i]++;
			Rec(Index+1,Value*10+i);
			Check[i]--;
		}
	}
}
int main(){
	int Case,Input;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&Case);
	for(int I = 1 ; I <= Case ; I++){
		memset(Temp,0,sizeof(Temp));
		memset(Count,0,sizeof(Count));
		memset(Check,0,sizeof(Check));
		Set.clear();
		scanf("%s",Temp);
		sscanf(Temp,"%d",&Input);
		Len = strlen(Temp);
		for(int i = 0 ; i < Len ; i++) Count[ Temp[i]-'0' ]++;
		for(i = 0 ; i < Len-1 ; i++)  if(Temp[i]<Temp[i+1]) break;
		printf("Case #%d: ",I);
		if(i==Len-1){
			Count[0]++;
			Len++;
			Rec(0,0);
			std::set<int>::iterator it=Set.begin();
			printf("%d\n",*it);
		}
		else{
			Rec(0,0);
			std::set<int>::iterator it=Set.find(Input);
			it++;
			printf("%d\n",*it);
//			while(Temp_Res!=Input){
//				Temp_Res=Set.
//			}
//			printf("%d",);
		}		
	}
	return 0;
}