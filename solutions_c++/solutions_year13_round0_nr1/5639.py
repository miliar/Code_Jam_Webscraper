#include <iostream> 
#include <string> 
#include <algorithm> 
#include <map> 
#include <set> 
#include <vector> 
#include <string.h> 
#include <stdio.h> 
#include <math.h> 
#include <sstream> 

using namespace std; 
int t;
int main(){
	cin>>t;
	for(int i=0 ; i<t ; i++){
		string status = "ad";
		char a[4][4];
		for(int j=0 ; j<4 ; j++){
			for(int k=0 ; k<4 ; k++){
				cin>>a[j][k];
			}
		}
		for(int j=0 ; j<4 ; j++){
			if((a[j][1] == 'X' || a[j][1] == 'T') && (a[j][2] == 'X' || a[j][2] == 'T') && (a[j][0] == 'X' || a[j][0] == 'T') && (a[j][3] == 'X' || a[j][3] == 'T'))
				status = "X won";
			if((a[j][1] == 'O' || a[j][1] == 'T') && (a[j][2] == 'O' || a[j][2] == 'T') && (a[j][0] == 'O' || a[j][0] == 'T') && (a[j][3] == 'O' || a[j][3] == 'T'))
				status = "O won";
		}
		for(int k=0 ; k<4 ; k++){
			if((a[1][k] == 'X' || a[1][k] == 'T') && (a[2][k] == 'X' || a[2][k] == 'T') && (a[0][k] == 'X' || a[0][k] == 'T') && (a[3][k] == 'X' || a[3][k] == 'T'))
				status = "X won";
			if((a[1][k] == 'O' || a[1][k] == 'T') && (a[2][k] == 'O' || a[2][k] == 'T') && (a[0][k] == 'O' || a[0][k] == 'T') && (a[3][k] == 'O' || a[3][k] == 'T'))
				status = "O won";
		}
		if((a[1][1] == 'X' || a[1][1] == 'T') && (a[2][2] == 'X' || a[2][2] == 'T') && (a[0][0] == 'X' || a[0][0] == 'T') && (a[3][3] == 'X' || a[3][3] == 'T'))
			status = "X won";
		if((a[3][0] == 'X' || a[3][0] == 'T') && (a[2][1] == 'X' || a[2][1] == 'T') && (a[1][2] == 'X' || a[1][2] == 'T') && (a[0][3] == 'X' || a[0][3] == 'T'))
			status = "X won";
		if((a[1][1] == 'O' || a[3][3] == 'T') && (a[2][2] == 'O' || a[3][3] == 'T') && (a[0][0] == 'O' || a[3][3] == 'T') && (a[3][3] == 'O' || a[3][3] == 'T'))
				status = "O won";
		if((a[3][0] == 'O' || a[3][0] == 'T') && (a[2][1] == 'O' || a[2][1] == 'T') && (a[1][2] == 'O' || a[1][2] == 'T') && (a[0][3] == 'O' || a[0][3] == 'T'))
			status = "O won";
		if(status == "ad"){
			status = "Draw";
			for(int j=0 ; j<4 ; j++){
				for(int k=0 ; k<4 ; k++){
					if(a[j][k] == '.')
						status = "Game has not completed";
				}
			}
		}
		cout<<"Case #"<<i+1<<": "<<status<<endl;
	}

return 0; 
}