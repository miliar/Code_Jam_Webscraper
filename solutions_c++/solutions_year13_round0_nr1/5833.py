#include<cstdio>
#include<string>
#include<iostream>

using namespace std;
bool flg;

char f()
{
	string s[4];
	for(int i=0;i<4;i++)cin >> s[i];
	
	for(int i=0;i<4;i++){
		if((s[0][i]=='X'||s[0][i]=='T')&&(s[1][i]=='X'||s[1][i]=='T')&&(s[2][i]=='X'||s[2][i]=='T')&&(s[3][i]=='X'||s[3][i]=='T')){
			return 'X';
		}
		if((s[0][i]=='O'||s[0][i]=='T')&&(s[1][i]=='O'||s[1][i]=='T')&&(s[2][i]=='O'||s[2][i]=='T')&&(s[3][i]=='O'||s[3][i]=='T')){
			return 'O';
		}
		if((s[i][0]=='X'||s[i][0]=='T')&&(s[i][1]=='X'||s[i][1]=='T')&&(s[i][2]=='X'||s[i][2]=='T')&&(s[i][3]=='X'||s[i][3]=='T')){
			return 'X';
		}
		if((s[i][0]=='O'||s[i][0]=='T')&&(s[i][1]=='O'||s[i][1]=='T')&&(s[i][2]=='O'||s[i][2]=='T')&&(s[i][3]=='O'||s[i][3]=='T')){
			return 'O';
		}
		if(s[i][0]=='.'||s[i][1]=='.'||s[i][2]=='.'||s[i][3]=='.'){
			flg=true;
		}
	}
	if((s[0][0]=='X'||s[0][0]=='T')&&(s[1][1]=='X'||s[1][1]=='T')&&(s[2][2]=='X'||s[2][2]=='T')&&(s[3][3]=='X'||s[3][3]=='T')){
		return 'X';
	}
	if((s[0][0]=='O'||s[0][0]=='T')&&(s[1][1]=='O'||s[1][1]=='T')&&(s[2][2]=='O'||s[2][2]=='T')&&(s[3][3]=='O'||s[3][3]=='T')){
		return 'O';
	}
	if((s[0][3]=='X'||s[0][3]=='T')&&(s[1][2]=='X'||s[1][2]=='T')&&(s[2][1]=='X'||s[2][1]=='T')&&(s[3][0]=='X'||s[3][0]=='T')){
		return 'X';
	}
	if((s[0][3]=='O'||s[0][3]=='T')&&(s[1][2]=='O'||s[1][2]=='T')&&(s[2][1]=='O'||s[2][1]=='T')&&(s[3][0]=='O'||s[3][0]=='T')){
		return 'O';
	}
	return 'D';
}

int main()
{
	int n;
	scanf("%d",&n);

	for(int i=0;i<n;i++){
		flg=false;
		char c=f();
		printf("Case #%d: ",i+1);
		if(c=='D'){
			if(flg==true){
				printf("Game has not completed\n");
			}else{
				printf("Draw\n");
			}
			continue;
		}
		printf("%c won\n",c);
	}
	return 0;
}