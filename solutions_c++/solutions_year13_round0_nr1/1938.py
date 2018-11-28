#include <cstdio>
#include <iostream>

using namespace std;

int T;
char s[5][5];

int main(){
	
	scanf(" %d",&T);
	
	int cnt,w1,w2;
	
	for(int i=1,fl;i<=T;i++){
		
		fl=w1=w2=0;
		
		for(int j=1;j<=4;j++)
			for(int k=1;k<=4;k++){
				scanf(" %c",&s[j][k]);
				if(s[j][k]=='.')
					fl=1;
			}
		
		for(int j=1;j<=4;j++){
		
			cnt=0;
			for(int k=1;k<=4;k++)
				if(s[j][k]=='X' || s[j][k]=='T')
					cnt++;
				else break;
			if(cnt==4)	w1=1;
			
			cnt=0;
			for(int k=1;k<=4;k++)
				if(s[j][k]=='O' || s[j][k]=='T')
					cnt++;
				else break;
			if(cnt==4)	w2=1;
		}
		
		for(int j=1;j<=4;j++){
		
			cnt=0;
			for(int k=1;k<=4;k++)
				if(s[k][j]=='X' || s[k][j]=='T')
					cnt++;
				else break;
			if(cnt==4)	w1=1;
			
			cnt=0;
			for(int k=1;k<=4;k++)
				if(s[k][j]=='O' || s[k][j]=='T')
					cnt++;
				else break;
			if(cnt==4)	w2=1;
		}
		
		cnt=0;
		
		for(int j=1;j<=4;j++)
			if(s[j][j]=='X' || s[j][j]=='T')
				cnt++;
			else break;
		
		if(cnt==4)	w1=1;
		
		cnt=0;
		
		for(int j=1;j<=4;j++)
			if(s[j][4-j+1]=='X' || s[j][4-j+1]=='T')
				cnt++;
			else break;
		
		if(cnt==4)	w1=1;
		
		cnt=0;
		
		for(int j=1;j<=4;j++)
			if(s[j][j]=='O' || s[j][j]=='T')
				cnt++;
			else break;
		
		if(cnt==4)	w2=1;
		
		cnt=0;
		
		for(int j=1;j<=4;j++)
			if(s[j][4-j+1]=='O' || s[j][4-j+1]=='T')
				cnt++;
			else break;
		
		if(cnt==4)	w2=1;
		
		if(!fl){
			if(!w1 && !w2)	printf("Case #%d: Draw\n",i);
			else if(w1)	printf("Case #%d: X won\n",i);
			else if(w2)	printf("Case #%d: O won\n",i);
		}
		
		else {
			if(!w1 && !w2)	printf("Case #%d: Game has not completed\n",i);
			else if(w1)	printf("Case #%d: X won\n",i);
			else if(w2)	printf("Case #%d: O won\n",i);
		}
	}

	return 0;
}
