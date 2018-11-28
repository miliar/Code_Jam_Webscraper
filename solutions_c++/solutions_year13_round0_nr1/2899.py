#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int main()
{
  int T;
  long A,B,number;
  long temp,i,j,k;
  char c;
  int tic[4][4];
  int row[4];
  int column[4];
  int diag[2];
  int dotexists;
  int texists;
  int owins; 
  int xwins;
  cin >> T;
  for(i=0;i<T;i++){
	dotexists =0;
	texists =0;
	owins =0;
	xwins=0;
	for(j=0;j<4;j++){
		 for(k=0;k<4;k++){
			tic[j][k]=0;
		}
	}
 	for(j=0;j<4;j++){
		 for(k=0;k<4;k++){
			cin >> c;
			if(c == 'X'){
			    tic[j][k]=1;
			}
			if(c == 'O'){
			    tic[j][k]=5;
			}  				
			if(c == '.'){
			    tic[j][k]=25;
			    dotexists =1;
			}
			if(c == 'T'){
			    tic[j][k]=125;
		            texists =1;
			}
		}
	}
	for(j=0;j<4;j++){
		row[j]=0;
		column[j]=0;
	}
	for(j=0;j<2;j++){
		diag[j]=0;
	}
	for(j=0;j<4;j++){
		 for(k=0;k<4;k++){
			row[j] = row[j]+tic[j][k];
			column[j] = column[j]+tic[k][j];
		}
	}
	diag[1] = tic[1][1]+tic[2][2]+tic[3][3]+tic[0][0];	
	diag[0] = tic[1][2]+tic[2][1]+tic[3][0]+tic[0][3];
	for(j=0;j<4;j++){
		if(row[j] == 20 || row[j] == 140 || column[j] == 20 || column[j] ==140){
			owins =1;
		}
		if(row[j] == 4 || row[j] == 128 || column[j] == 4 || column[j] ==128){
			xwins =1;
		}
	}
	for(j=0;j<2;j++){
		if(diag[j] == 20 || diag[j] == 140 ){
			owins =1;
		}
		if(diag[j] == 4 || diag[j] == 128 ){
			xwins =1;
		}
	}
	if(owins ==1){
	    cout << "Case #" << i+1 << ": O won" << endl;
	}
	if(xwins ==1){
	    cout << "Case #" << i+1 << ": X won" << endl;
	}
	if(owins == 0 && xwins ==0 && dotexists ==0){
		    cout << "Case #" << i+1 << ": Draw" << endl;
	}
	if(dotexists ==1 && owins == 0 && xwins ==0){
	    cout << "Case #" << i+1 << ": Game has not completed" << endl;
	}
  }
  return 0;
}
