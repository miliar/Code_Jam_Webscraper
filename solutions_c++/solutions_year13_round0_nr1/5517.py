#include<iostream>
#include<stdlib.h>
#include<stdio.h>
#include<math.h>
#include<string>
using namespace std;


int main()
{
	int T;
	int k=0;
	int i,j;
	char bo[4][4];
	cin>>T;
	int cou=0;
	char win;
	while(k++<T){
		for(i=0;i<4;++i)
			for(j=0;j<4;++j)
				cin>>bo[i][j];
		cou=0;
		win='N';
		for(i=0;i<4;++i){
			if( (bo[i][0]=='X' || bo[i][0]=='T') &&(bo[i][1]=='X' || bo[i][1]=='T') 
				&& (bo[i][2]=='X' || bo[i][2]=='T' ) && ( bo[i][3]=='X' || bo[i][3]=='T' ) ){
					win='X';
					break;
			}
			if( (bo[i][0]=='O' || bo[i][0]=='T') && (bo[i][1]=='O' || bo[i][1]=='T') 
				&& (bo[i][2]=='O' || bo[i][2]=='T' ) && ( bo[i][3]=='O' || bo[i][3]=='T' ) ){
					win='O';
					break;
			}
		}
		if(win!='X' || 'O'){
			for(i=0;i<4;++i){
				if( ( bo[0][i]=='X' || bo[0][i]=='T' ) && (bo[1][i]=='X' || bo[1][i]=='T') 
					&&(bo[2][i]=='X' || bo[2][i]=='T') && (bo[3][i]=='X' || bo[3][i]=='T' )  ){
						win='X';
						break;
				}
				if( ( bo[0][i]=='O' || bo[0][i]=='T' ) && (bo[1][i]=='O' || bo[1][i]=='T') 
					&&(bo[2][i]=='O' || bo[2][i]=='T') && (bo[3][i]=='O' || bo[3][i]=='T' )  ){
						win='O';
						break;
				}
			}//for
		}//if
		if(win!='X' || 'O'){
			if( (bo[0][0]=='X' || bo[0][0]=='T') &&(bo[1][1]=='X' || bo[1][1]=='T') 
				&& (bo[2][2]=='X' || bo[2][2]=='T' ) && ( bo[3][3]=='X' || bo[3][3]=='T' ) ||
				((bo[0][3]=='X' || bo[0][3]=='T') &&(bo[1][2]=='X' || bo[1][2]=='T') 
				&& (bo[2][1]=='X' || bo[2][1]=='T' ) && ( bo[3][0]=='X' || bo[3][0]=='T' )) ){
					win='X';
			}
			else if( ((bo[0][0]=='O' || bo[0][0]=='T') &&(bo[1][1]=='O' || bo[1][1]=='T') 
				&& (bo[2][2]=='O' || bo[2][2]=='T' ) && ( bo[3][3]=='O' || bo[3][3]=='T' ) ) 
				||
				((bo[0][3]=='O' || bo[0][3]=='T') &&(bo[1][2]=='O' || bo[1][2]=='T') 
				&& (bo[2][1]=='O' || bo[2][1]=='T' ) && ( bo[3][0]=='O' || bo[3][0]=='T' )) ){
					win='O';
			}//if
		}//if
		cout<<"Case #"<<k<<": ";
		if(win=='N'){
			for(i=0;i<15;++i){
				if(*((char*)bo+i)=='.'){
					win='D';
					break;
				}
			}
			if(win=='D')
				cout<<"Game has not completed"<<endl;
			else
				cout<<"Draw"<<endl;
		}
		else
			cout<<win<<" won"<<endl;
	}//while
	return 0;
}