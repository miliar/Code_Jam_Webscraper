//Karol Rozycki
#include<cstdio>
using namespace std;

int z;
char T[4][4];
char line[5];

int main(){
	scanf("%i",&z);
	for(int g=1;g<=z;g++){
		for(int i=0;i<4;i++){
			scanf("%s",line);
			for(int j=0;j<4;j++){
				T[i][j]=line[j];
			}
		}
		int flag=0;
		for(int i=0;i<4;i++){
			int counter=0;
			for(int j=0;j<4;j++){
				if(T[i][j]=='X' || T[i][j]=='T'){
					counter++;
				}else{
					break;
				}
			}
			if(counter==4){
				flag=1;
				break;
			}
		}
		for(int i=0;i<4;i++){
			int counter=0;
			for(int j=0;j<4;j++){
				if(T[j][i]=='X' || T[j][i]=='T'){
					counter++;
				}else{
					break;
				}
			}
			if(counter==4){
				flag=1;
				break;
			}
		}
		int counter=0;
		for(int i=0;i<4;i++){
			if(T[i][i]=='X' || T[i][i]=='T'){
				counter++;
			}else{
				break;
			}
		}
		if(counter==4){
			flag=1;
		}
		counter=0;
		for(int i=0;i<4;i++){
			if(T[i][3-i]=='X' || T[i][3-i]=='T'){
				counter++;
			}else{
				break;
			}
		}
		if(counter==4){
			flag=1;
		}
		for(int i=0;i<4;i++){
			int counter2=0;
			for(int j=0;j<4;j++){
				if(T[i][j]=='O' || T[i][j]=='T'){
					counter2++;
				}else{
					break;
				}
			}
			if(counter2==4){
				flag=2;
				break;
			}
		}
		for(int i=0;i<4;i++){
			int counter2=0;
			for(int j=0;j<4;j++){
				if(T[j][i]=='O' || T[j][i]=='T'){
					counter2++;
				}else{
					break;
				}
			}
			if(counter2==4){
				flag=2;
				break;
			}
		}
		int counter2=0;
		for(int i=0;i<4;i++){
			if(T[i][i]=='O' || T[i][i]=='T'){
				counter2++;
			}else{
				break;
			}
		}
		if(counter2==4){
			flag=2;
		}
		counter2=0;
		for(int i=0;i<4;i++){
			if(T[i][3-i]=='O' || T[i][3-i]=='T'){
				counter2++;
			}else{
				break;
			}
		}
		if(counter2==4){
			flag=2;
		}
		if(flag==0){
			for(int i=0;i<4;i++){
				for(int j=0;j<4;j++){
					if(T[i][j]=='.'){
						flag=-1;
						break;
					}
				}
			}		
		}
		printf("Case #%i: ",g);
		if(flag==0){
			printf("Draw\n");
		}else if(flag==1){
			printf("X won\n");
		}else if(flag==2){
			printf("O won\n");
		}else{
			printf("Game has not completed\n");
		}
	}
	return 0;
}

