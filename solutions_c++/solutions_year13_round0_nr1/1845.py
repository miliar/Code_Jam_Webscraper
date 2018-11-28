#include<iostream>
#include<string>
#include<stdio.h>


using namespace std;

string s[5];
char sts[50];


bool win(char c){

	if( (s[0][0]==c || s[0][0]=='T') && (s[0][1]==c || s[0][1]=='T') && (s[0][2]==c || s[0][2]=='T') && (s[0][3]==c || s[0][3]=='T') )return true;
	if( (s[1][0]==c || s[1][0]=='T') && (s[1][1]==c || s[1][1]=='T') && (s[1][2]==c || s[1][2]=='T') && (s[1][3]==c || s[1][3]=='T') )return true;
	if( (s[2][0]==c || s[2][0]=='T') && (s[2][1]==c || s[2][1]=='T') && (s[2][2]==c || s[2][2]=='T') && (s[2][3]==c || s[2][3]=='T') )return true;
	if( (s[3][0]==c || s[3][0]=='T') && (s[3][1]==c || s[3][1]=='T') && (s[3][2]==c || s[3][2]=='T') && (s[3][3]==c || s[3][3]=='T') )return true;

	if( (s[0][0]==c || s[0][0]=='T') && (s[1][0]==c || s[1][0]=='T') && (s[2][0]==c || s[2][0]=='T') && (s[3][0]==c || s[3][0]=='T'))return true;
	if( (s[0][1]==c || s[0][1]=='T') && (s[1][1]==c || s[1][1]=='T') && (s[2][1]==c || s[2][1]=='T') && (s[3][1]==c || s[3][1]=='T'))return true;
	if( (s[0][2]==c || s[0][2]=='T') && (s[1][2]==c || s[1][2]=='T') && (s[2][2]==c || s[2][2]=='T') && (s[3][2]==c || s[3][2]=='T'))return true;
	if( (s[0][3]==c || s[0][3]=='T') && (s[1][3]==c || s[1][3]=='T') && (s[2][3]==c || s[2][3]=='T') && (s[3][3]==c || s[3][3]=='T'))return true;
	
	if((s[0][0]==c || s[0][0]=='T') && (s[1][1]==c || s[1][1]=='T') && (s[2][2]==c || s[2][2]=='T') && (s[3][3]==c || s[3][3]=='T'))return true;
	if((s[0][3]==c || s[0][3]=='T') && (s[1][2]==c || s[1][2]=='T') && (s[2][1]==c || s[2][1]=='T') && (s[3][0]==c || s[3][0]=='T'))return true;
	return false;
}

bool filled(){
	int i,j;
	for(i=0;i<4;i++){
		for(j=0;j<4;j++){
			if(s[i][j]=='.')return false;
		}
	}
	return true;
}

int main()
{
	freopen("sam.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int i=0,t;
	cin>>t;
	while(t--){
		cin>>s[0]>>s[1]>>s[2]>>s[3];
		if(filled()==true)strcpy(sts,"Draw");
		else strcpy(sts,"Game has not completed");
		if(win('X')==true)strcpy(sts,"X won");
		if(win('O')==true)strcpy(sts,"O won");
		printf("Case #%d: %s\n",++i,sts);
	}

	return 0;
}
