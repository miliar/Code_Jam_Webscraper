#include <iostream>
#include <cstdio>

using namespace std;

int main(){
	int t, k=1;
	cin>>t;
	while(t--){
		char a[4][4];
		
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)	cin>>a[i][j];
		scanf("\n");
			
		printf("Case #%d: ",k++);		
		int cx=0,cy=0;
		bool vacio=0;
		bool saltar=0;
		for(int i=0;i<4;i++){
			cx=0;cy=0;
			for(int j=0;j<4;j++){
				if(a[i][j]=='X' or a[i][j]=='T')	cx++;
				if(a[i][j]=='O' or a[i][j]=='T')	cy++;
				if(a[i][j]=='.'){
					vacio=1;
					continue;
				}
				if(cx==4){
					printf("X won\n");
					saltar=1;					
					break;
					break;
				}
				if(cy==4){
					printf("O won\n");
					saltar=1;
					break;
					break;
				}				
			}
		}
		if(saltar)	continue;
		for(int i=0;i<4;i++){
			cx=0;cy=0;
			for(int j=0;j<4;j++){
				if(a[j][i]=='X' or a[j][i]=='T')	cx++;
				if(a[j][i]=='O' or a[j][i]=='T')	cy++;
				if(a[j][i]=='.'){
					vacio=1;
					continue;
				}
				if(cx==4){
					printf("X won\n");
					saltar=1;
					break;
					break;
				}
				if(cy==4){
					printf("O won\n");
					saltar=1;
					break;
					break;
				}				
			}
		}
		if(saltar)	continue;
		cx=0;cy=0;
		for(int i=0;i<4;i++){
			if(a[i][i]=='X' or a[i][i]=='T')	cx++;
			if(a[i][i]=='O' or a[i][i]=='T')	cy++;
			if(a[i][i]=='.'){
				vacio=1;
				break;
			}
			if(cx==4){
				printf("X won\n");
				saltar=1;
				break;
			}
			if(cy==4){
				printf("O won\n");
				saltar=1;
				break;
			}		
		}
		if(saltar)	continue;

		cx=0;cy=0;
		for(int i=0;i<4;i++){
			if(a[3-i][i]=='X' or a[3-i][i]=='T')	cx++;
			if(a[3-i][i]=='O' or a[3-i][i]=='T')	cy++;
			if(a[3-i][i]=='.'){
				vacio=1;
				break;
			}
			if(cx==4){
				printf("X won\n");
				saltar=1;
				break;
			}
			if(cy==4){
				printf("O won\n");
				saltar=1;
				break;
			}		
		}
		if(saltar)	continue;		
		
		if(cx!=4 and cy!=4){
			if(vacio)	printf("Game has not completed\n");
			else		printf("Draw\n");
		}		
	}
	return 0;
}
