//#include<iostream>
#include<stdio.h>
#include<string>
#include<vector>
#include <fstream>
using namespace std;


string arr[4];
int main(){


	
	int numOfTest;

	ofstream cout ("test1.out");
    ifstream cin ("A-small-attempt0.in");

	cin>>numOfTest;

	string read;

	for(int counter=0;counter<numOfTest;++counter){
		getline(cin,read);


		getline(cin,arr[0]);
		getline(cin,arr[1]);
		getline(cin,arr[2]);
		getline(cin,arr[3]);

		char Winter='N';


	for(int i=0;i<4;++i){
		if((arr[i][0]=='X' ||arr[i][0]=='T') &&
			(arr[i][1]=='X' ||arr[i][1]=='T') &&
			(arr[i][2]=='X' ||arr[i][2]=='T') &&
			(arr[i][3]=='X' ||arr[i][3]=='T') 
			&&(arr[i][0]=='X' || arr[i][1]=='X' || arr[i][2]=='X' || arr[i][3]=='X')){
				Winter='X';
		}else
			if((arr[i][0]=='O' ||arr[i][0]=='T') &&
			(arr[i][1]=='O' ||arr[i][1]=='T') &&
			(arr[i][2]=='O' ||arr[i][2]=='T') &&
			(arr[i][3]=='O' ||arr[i][3]=='T') 
			&&(arr[i][0]=='O' || arr[i][1]=='O' || arr[i][2]=='O' || arr[i][3]=='O')){
				Winter='O';
			}

			if(Winter!='N')break;
		}


	for(int i=0;i<4;++i){

		if(Winter!='N')break;

		if((arr[0][i]=='X' ||arr[0][i]=='T') &&
			(arr[1][i]=='X' ||arr[1][i]=='T') &&
			(arr[2][i]=='X' ||arr[2][i]=='T') &&
			(arr[3][i]=='X' ||arr[3][i]=='T') 
			&&(arr[0][i]=='X' || arr[1][i]=='X' || arr[2][i]=='X' || arr[3][i]=='X')){
				Winter='X';
		}else
			if((arr[0][i]=='O' ||arr[0][i]=='T') &&
			(arr[1][i]=='O' ||arr[1][i]=='T') &&
			(arr[2][i]=='O' ||arr[2][i]=='T') &&
			(arr[3][i]=='O' ||arr[3][i]=='T') 
			&&(arr[0][i]=='O' || arr[1][i]=='O' || arr[2][i]=='O' || arr[3][i]=='O')){
				Winter='O';
			}

			
		}


	if((arr[0][0]=='X' ||arr[0][0]=='T') &&
			(arr[1][1]=='X' ||arr[1][1]=='T') &&
			(arr[2][2]=='X' ||arr[2][2]=='T') &&
			(arr[3][3]=='X' ||arr[3][3]=='T') 
			&&(arr[0][0]=='X' || arr[1][1]=='X' || arr[2][2]=='X' || arr[3][3]=='X')){
				Winter='X';
		}else
		if((arr[0][0]=='O' ||arr[0][0]=='T') &&
			(arr[1][1]=='O' ||arr[1][1]=='T') &&
			(arr[2][2]=='O' ||arr[2][2]=='T') &&
			(arr[3][3]=='O' ||arr[3][3]=='T') 
			&&(arr[0][0]=='O' || arr[1][1]=='O' || arr[2][2]=='O' || arr[3][3]=='O')){
				Winter='O';
		}


	if(  (arr[0][3]=='X' ||arr[0][3]=='T') &&
			(arr[1][2]=='X' ||arr[1][2]=='T') &&
			(arr[2][1]=='X' ||arr[2][1]=='T') &&
			(arr[3][0]=='X' ||arr[3][0]=='T') 
			&&(arr[0][3]=='X' || arr[1][2]=='X' || arr[2][1]=='X' || arr[3][0]=='X')){
				Winter='X';
		}else
		if((arr[0][3]=='O' ||arr[0][3]=='T') &&
			(arr[1][2]=='O' ||arr[1][2]=='T') &&
			(arr[2][1]=='O' ||arr[2][1]=='T') &&
			(arr[3][0]=='O' ||arr[3][0]=='T') 
			&&(arr[0][3]=='O' || arr[1][2]=='O' || arr[2][1]=='O' || arr[3][0]=='O')){
				Winter='O';
		}

		bool f=false;
		for(int i=0;i<4;++i)
			for(int j=0;j<4;++j){
				if(arr[i][j]=='.')
					f=true;
			}

			cout<<"Case #"<<counter+1<<": ";
			if(Winter=='X'){
				cout<<"X won"<<endl;;
			}
			else if(Winter=='O'){
				cout<<"O won"<<endl;;
			}
			else{

				if(f)
					cout<<"Game has not completed"<<endl;
				else
					cout<<"Draw"<<endl;
			}

	 }

	
	return 0;
}
