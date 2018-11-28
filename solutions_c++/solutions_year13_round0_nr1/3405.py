#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<cstring>
#include<math.h>
using namespace std;
char state[4][30]={"X won","O won","Draw","Game has not completed"};
int checkwon(char B[4][4], char player, int Tposi, int Tposj){
	int won=0;
//	cout<<B[Tposi][Tposj];
	if(Tposi!=-1 && Tposj!=-1)
		B[Tposi][Tposj]=player;
//	cout<<B[Tposi][Tposj];
	//Check Diagonal
	if( B[0][0]==player && B[0][0]==B[1][1] && B[1][1]==B[2][2] && B[2][2]==B[3][3])
		return 4;
	if( B[3][0]==player && B[0][3]==B[1][2] && B[1][2]==B[2][1] && B[2][1]==B[3][0])
		return 4;
	//Check Row
	for(int i=0;i<4;i++){
		won=0;
		for(int j=0;j<4;j++)
			if(B[i][j]==player)
				won++;
		if(won==4) return 4;
	}
	//Check Column
	for(int i=0;i<4;i++){
		won=0;
		for(int j=0;j<4;j++)
			if(B[j][i]==player)
				won++;
		if(won==4) return 4;
	}
	return 0;
}
const char* status(char B[4][4], int Tposi, int Tposj){
	int won=0,empty=0;
	for(int i=0;i<4;i++){
		for(int j=0;j<4;j++)
			if(B[i][j]=='.')
				empty++;
	}
	if(checkwon(B,'O',Tposi,Tposj))	return "O won";
	if(checkwon(B,'X',Tposi,Tposj))	return "X won";
	if(empty)      return "Game has not completed";
					 return "Draw";
}

void sort(int *gr, int size){
	int j;
	for(int i=1;i<size;i++){
		int key=gr[i];
		for(j=i-1;j>=0 && gr[j]>key;j--)
			gr[j+1]=gr[j];
		gr[j+1]=key;
	}
}
int main(){
	int T;
	char B[4][4];
	int Tposi,Tposj;
	cin>>T;
	for(int t=0;t<T;t++){
		Tposi=-1; Tposj=-1;
		for(int _i=0;_i<4;_i++)
			for(int _j=0;_j<4;_j++){
				cin>>B[_i][_j];
				if(B[_i][_j]=='T')
					{Tposi=_i;Tposj=_j;}
				}	
		cout<<"Case #"<<t+1<<": "<<status(B,Tposi, Tposj)<<endl;
	}
}
