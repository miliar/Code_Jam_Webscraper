#include<iostream>
#include<string>
using namespace std;

string bd[4];
bool isSameR(int id,char c){

	for(int i=0;i<4;i++)
		if(bd[id][i]==c || bd[id][i]=='T')continue;
		else return false;
	return true;
}
bool isSameC(int id,char c){

	for(int i=0;i<4;i++)
		if(bd[i][id]==c || bd[i][id]=='T')continue;
		else return false;
	return true;
}
bool isD(char c){

	bool f=true;
	for(int i=0;i<4;i++)
		if(bd[i][i]==c||bd[i][i]=='T')continue;
		else f=false;
	
	if(f==true) return true;

	f=true;
	for(int i=0;i<4;i++)
		if(bd[i][3-i]==c||bd[i][3-i]=='T')continue;
		else return false;
	return true;
}
bool isXwon(){

	for(int i=0;i<4;i++){
		if(isSameR(i,'X')) return true;
		if(isSameC(i,'X')) return true;
	}
	if(isD('X')) return true;
	return false;
}
bool isOwon(){
	for(int i=0;i<4;i++){
		if(isSameR(i,'O')) return true;
		if(isSameC(i,'O')) return true;
	}
	if(isD('O')) return true;
	return false;

}
bool isFilled(){

		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				if(bd[i][j]=='.') return false;

		return true;
}
int main(){
	freopen("A-large.in","rt",stdin);
	freopen("A-large.out","wt",stdout);
	int T,cas=1;
	cin>>T;
	while(T--){
	
		for(int i=0;i<4;i++)
			cin>>bd[i];
		
		printf("Case #%d: ",cas++);
		if(isXwon())
			printf("X won\n");
		else if(isOwon())
			printf("O won\n");
		else if(isFilled())
			printf("Draw\n");
		else printf("Game has not completed\n");
	
	}
	return 0;
}