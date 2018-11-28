#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#define N 50
using namespace std;

char table[N][N];

int main(){
	int cases;
	cin >> cases;
	for(int i=0;i<cases;i++){
		//..............
		for(int j=0;j<N;j++){for(int k=0;k<N;k++){table[j][k]=' ';}}
		int rows, cols;
		cin >> rows;
		cin >> cols;
		for(int j=0;j<rows;j++){
			for(int k=0;k<cols;k++){
				cin >> table[j][k];
			}
		}
		
		// sorokon vegig
		int bluesInRow=0;
		bool impossible=false;
		for(int j=0;j<rows && !impossible;j++){
			for(int k=0;k<cols && !impossible;k++){
				if(table[j][k]=='.'){		// white coming
					if(bluesInRow%2==0){	//good
						bluesInRow=0;
					}
					else{
						impossible=true;
						bluesInRow=0;
					}
				}else{					// blue coming
					bluesInRow++;
					if(bluesInRow%2==1){
						table[j][k]='/';
					}
					else{
						table[j][k]='\\';
					}
					if(k==cols-1 && bluesInRow%2==1)impossible=true;
				}
			}
		}
		if(impossible){
			cout << "Case #" << i+1 << ":"<< endl;
			cout << "Impossible" << endl;
			continue;
		}
		
		// oszlopokon vegig
		bluesInRow=0;
		impossible=false;
		for(int k=0;k<cols && !impossible;k++){
			for(int j=0;j<rows && !impossible;j++){
				if(table[j][k]=='.'){		// white coming
					if(bluesInRow%2==0){	//good
						bluesInRow=0;
					}
					else{
						impossible=true;
						bluesInRow=0;
					}
				}else{					// blue coming
					bluesInRow++;
					if(bluesInRow%2==1){
						table[j][k]=='\\';
						
					}else{ 
						table[j][k]=='/';
					}
					
					if(j==rows-1 && bluesInRow%2==1)impossible=true;
				}
			}
		}
		if(impossible){
			cout << "Case #" << i+1 << ":"<<endl;
			cout << "Impossible" << endl;
			continue;
		}
		bluesInRow =0;
		for(int j=0;j<cols;j++){
			for(int k=0;k<rows;k++){
				if(table[k][j]=='.'){
					bluesInRow=0;
				}else{
					bluesInRow++;
					if(bluesInRow%2==0){
						if(table[k][j]=='\\') table[k][j]='/';
						else table[k][j]='\\';
					}
				}
			}
		}
		
		
		cout << "Case #" << i+1 << ":" << endl;
		for(int j=0;j<rows;j++){
			for(int k=0;k<cols;k++){
				cout << table[j][k];
			}
			cout  << endl;
		}
	}
	return 0;
}