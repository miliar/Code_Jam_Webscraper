#pragma warning(disable : 4786)
#include<stdio.h>
#include<map>
using namespace std;
map<char,int>Map;
int Count;
bool Check[100];
char Temp[66];
int Data[100];
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int Case,Len,i;
	char Input[66];
	scanf("%d",&Case);
	for(int I=1 ; I<=Case ; I++){
		Map.clear();
		Count=0;
		scanf("%s",Input);
		Len=strlen(Input);
		bool Sw=false;
		for(i = 0 ; i < Len ; i++){
			if(Map.count(Input[i])==0){
				if(Count==0 && Sw==false){
					Map[ Input[i] ]=1;
					Sw=true;
				}
				else if(Count==0 && Sw){
					Map[ Input[i] ]=0;
					Count=1;
				}
				else Map[ Input[i] ]=++Count;
			}
			Data[i] = Map[ Input[i] ];
		}
		__int64 k=1;
		__int64 Res=0;
		if(Count==0) Count++; 
		for(i = Len-1 ; i >= 0 ; i--){
			Res+=k*Data[i];
			k*=(Count+1);
		}
		printf("Case #%d: %I64d\n",I,Res);
	}
	return 0;
}