#include <stdio.h>

int main(){	
	int t;
	char s[100][100];
	scanf("%d\n",&t);
	for(int bbb=0;bbb<t;bbb++){
		for(int i=0;i<4;i++){
			scanf("%s",s[i]);	
		}
		
		int at=-1;
		bool incompleto = false;
		for(int i=0;i<4;i++){
			int at=-1;
			for(int j=0;j<4;j++){
				if(s[i][j]=='O'){
					if((at==-1 || at==1))at=1;
					else at=3;
				}
				else if(s[i][j]=='X'){
					if((at==-1 || at==2))at=2;
					else at=3;
				}
				else if(s[i][j]=='.'){
					incompleto=true;
					at=3;
				}
			}
			if(at==1){
				goto bola;
			}
			else if(at==2){
				goto xix;
			}
		}


		for(int i=0;i<4;i++){
			int at=-1;
			for(int j=0;j<4;j++){
				if(s[j][i]=='O'){
					if((at==-1 || at==1))at=1;
					else at=3;
				}
				else if(s[j][i]=='X'){
					if((at==-1 || at==2))at=2;
					else at=3;
				}
				else if(s[j][i]=='.'){
					incompleto=true;
					at=3;
				}
			}
			if(at==1){
				goto bola;
			}
			else if(at==2){
				goto xix;
			}
		}

		at=-1;
		for(int i=0;i<4;i++){
			if(s[i][i]=='O'){
				if((at==-1 || at==1))at=1;
				else at=3;
			}
			else if(s[i][i]=='X'){
				if((at==-1 || at==2))at=2;
				else at=3;
			}
			else if(s[i][i]=='.'){
			
				incompleto=true;
				at=3;
			}
		}
		if(at==1)goto bola;
			else if(at==2){
				goto xix;
		}

		at=-1;
		for(int i=0;i<4;i++){
			
		
			if(s[i][3-i]=='O'){
				if((at==-1 || at==1))at=1;
				else at=3;
			}
			else if(s[i][3-i]=='X'){
				if((at==-1 || at==2))at=2;
				else at=3;
			}
			else if(s[i][3-i]=='.'){
				incompleto=true;
				at=3;
			}		
			
		}
		if(at==1)goto bola;
			else if(at==2){
				goto xix;
		}


		if(incompleto){
			printf("Case #%d: Game has not completed\n",bbb+1);
		}
		else{
			printf("Case #%d: Draw\n",bbb+1);
		}
		goto fim;

		bola:
			printf("Case #%d: O won\n",bbb+1);
		goto fim;
		xix:
			printf("Case #%d: X won\n",bbb+1);
		goto fim;

		fim:;



		



	}



}