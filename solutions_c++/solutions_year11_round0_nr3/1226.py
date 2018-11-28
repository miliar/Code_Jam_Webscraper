#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string.h>
#include <iso646.h>
using namespace std; 

int main(){

	freopen("Q3.in", "rt", stdin);
	freopen("Q3.out", "wt", stdout);
	 	
	int r,T;
	int C,N,i,j,k;
	int diff;
	int salida;
	
	vector<int> valor;
	  
   cin >> T;  
   for(r=0;r<T;r++){
		cout << "Case #" << r+1 << ": ";
		cerr << "Case #" << r+1 << ": ";
	
		valor.clear();
		cin >> N;
		for(i=0;i<N;i++){
			cin >> C;
			valor.push_back(C);				
		}
		
		salida = 0;
		for(i=1;i<((2<<(N-1))-1);i++){
			int suma1 = 0;
			int suma2 = 0;
			int timo1 = 0;
			int timo2 = 0;
			for(j=0;j<N;j++){
				if((i&(1<<j))==0){
					suma1 += valor[j];
					timo1 ^= valor[j];
				}else{
				   suma2 += valor[j];
					timo2 ^= valor[j];
				}
			}
			if(timo1 == timo2){
				diff= max(suma1,suma2);
				if(diff>salida) salida = diff;
			}
		}
		if(salida==0){
			cout << "NO" << endl;
			cerr << "NO" << endl;
		}else{
			cout << salida << endl;
			cerr << salida << endl;
		}
	}
}

