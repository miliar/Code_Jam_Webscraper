#include<cstdio>
#include<iostream>
#include<string>
using namespace std;
int main(){	
	freopen("F:\\input2.in","r",stdin);
	freopen("F:\\output.txt","w",stdout);
	int t;
	scanf("%d",&t);
	for(int I=1;I<=t;I++){
		printf("Case #%d: ",I);
		bool anyBlank=false;
		string s[4];
		for(int i=0;i<4;i++){
			cin>>s[i];	
		}
		bool done=false;
		//row check
		for(int i=0;i<4 && !done;i++){
			int seen[3]={0,0,0};
			for(int j=0;j<4;j++){
				if(s[i][j]=='X') seen[0]++;
				else if(s[i][j]=='O') seen[1]++;
				else if(s[i][j]=='T') seen[2]++;
				else if(s[i][j]=='.') anyBlank=true;
			}
			if(seen[0]==0 && seen[1]+seen[2]==4){
				printf("O won\n");
				done=true;				
			}
			else if(seen[1]==0 && seen[0]+seen[2]==4){
				printf("X won\n");
				done=true;
			}
		}
		//col check
		for(int j=0;j<4 && !done;j++){
			int seen[3]={0,0,0};
			for(int i=0;i<4;i++){
				if(s[i][j]=='X') seen[0]++;
				else if(s[i][j]=='O') seen[1]++;
				else if(s[i][j]=='T') seen[2]++;
			}
			if(seen[0]==0 && seen[1]+seen[2]==4){
				printf("O won\n");
				done=true;				
			}
			else if(seen[1]==0 && seen[0]+seen[2]==4){
				printf("X won\n");
				done=true;
			}
		}
		// diagonal 1
		int seen[3]={0,0,0};
		for(int i=0;i<4 && !done;i++){
			if(s[i][i]=='X') seen[0]++;
			else if(s[i][i]=='O') seen[1]++;
			else if(s[i][i]=='T') seen[2]++;
		}
		if(seen[0]==0 && seen[1]+seen[2]==4){
			printf("O won\n");
			done=true;
		}
		if(seen[1]==0 && seen[0]+seen[2]==4){
			printf("X won\n");
			done=true;
		}
		for(int i=0;i<3;i++) seen[i]=0;
		//diagonal 2
		for(int i=0;i<4 && !done;i++){
			if(s[i][3-i]=='X') seen[0]++;
			else if(s[i][3-i]=='O') seen[1]++;
			else if(s[i][3-i]=='T') seen[2]++;	
		}
		if(seen[0]==0 && seen[1]+seen[2]==4){
			printf("O won\n");
			done=true;
		}
		if(seen[1]==0 && seen[0]+seen[2]==4){
			printf("X won\n");
			done=true;
		}
		if(!done && anyBlank) {
			printf("Game has not completed\n");
		}
		else if(!done && !anyBlank) {
			printf("Draw\n");
		}
		
	}
}
