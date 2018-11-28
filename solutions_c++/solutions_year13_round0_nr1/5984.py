#include <iostream>
#include<cmath>
#include<vector>
#include<string>
#include<cstring>
#include<algorithm>
#include<sstream>
#include<iterator>
#include<cstdlib>
#include<cctype>
#include<queue>
#include<map>
#include<ctime>
#include<utility>
#include<cstdio>
#include<set>

using namespace std;

#define FOR(i,a,b) for(int i=a;i!=b;i++)

char C[4][4];
char res[100];
bool st;
int a,b;

void check(){
	char ch = 'X';
	if(a>0 && b>0) C[a][b]='X';
	FOR(i,0,2){
		if(C[0][0]==ch && C[1][0]==ch && C[2][0]==ch && C[3][0]==ch){cout<<"enter"<<endl;sprintf(res,"%c won",ch);return;}
		else if(C[0][1]==ch && C[1][1]==ch && C[2][1]==ch && C[3][1]==ch){cout<<"enter"<<endl;sprintf(res,"%c won",ch);return;}
		else if(C[0][2]==ch && C[1][2]==ch && C[2][2]==ch && C[3][2]==ch){cout<<"enter"<<endl;sprintf(res,"%c won",ch);return;}
		else if(C[0][3]==ch && C[1][3]==ch && C[2][3]==ch && C[3][3]==ch){cout<<"enter"<<endl;sprintf(res,"%c won",ch);return;}
		else if(C[0][0]==ch && C[0][1]==ch && C[0][2]==ch && C[0][3]==ch){cout<<"enter"<<endl;sprintf(res,"%c won",ch);return;}
		else if(C[1][0]==ch && C[1][1]==ch && C[1][2]==ch && C[1][3]==ch){cout<<"enter"<<endl;sprintf(res,"%c won",ch);return;}
		else if(C[2][0]==ch && C[2][1]==ch && C[2][2]==ch && C[2][3]==ch){cout<<"enter"<<endl;sprintf(res,"%c won",ch);return;}
		else if(C[3][0]==ch && C[3][1]==ch && C[3][2]==ch && C[3][3]==ch){cout<<"enter"<<endl;sprintf(res,"%c won",ch);return;}
		else if(C[0][0]==ch && C[1][1]==ch && C[2][2]==ch && C[3][3]==ch){cout<<"enter"<<endl;sprintf(res,"%c won",ch);return;}
		else if(C[3][0]==ch && C[2][1]==ch && C[1][2]==ch && C[0][3]==ch){cout<<"enter"<<endl;sprintf(res,"%c won",ch);return;}
		ch='O';
		if(a>0 && b>0) C[a][b]='O';
	}
	
	if(st)sprintf(res,"Game has not completed");
	else sprintf(res,"Draw");
	
	return;
}


int main ()
{	
	int T;
	FILE* fi;
	FILE* fo;
	fi = fopen("input","r");
	fo = fopen("output","w");
	fscanf(fi,"%d",&T);
	FOR(i,1,T+1){
		st = false;
		a = -1;b = -1;
		FOR(j,0,4){
			fscanf(fi,"\n%c%c%c%c",&C[j][0],&C[j][1],&C[j][2],&C[j][3]);
			if(C[j][0]=='.' || C[j][1]=='.' || C[j][2]=='.' || C[j][3]=='.') {st = true;}
			
			if(C[j][0]=='T') {a = j;b = 0;}
			else if(C[j][1]=='T') {a = j;b = 1;}
			else if(C[j][2]=='T') {a = j;b = 2;}
			else if(C[j][3]=='T') {a = j;b = 3;}

		}
		check();
		cout << C[0][0] << C[1][0] << C[2][0] << C[3][0] << endl;
		if(C[0][0]==C[1][0]==C[2][0]==C[3][0]) cout << "YES!" <<endl;
		if(res[0]=='.') sprintf(res,"Game has not completed");
		fprintf(fo,"Case #%d: %s\n",i,res);
	}
	return 0;
}
