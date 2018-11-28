#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std; 

int main(){

	freopen("Q1.in", "rt", stdin);
	freopen("Q1.out", "wt", stdout);
	
	int r,T;
	int N;
	int i;
	char Robot;
	int Boton;
	int salida;
	int posO,posB;
	
	vector<int> B;
	vector<int> O;
	vector<char> orden;
	
   cin >> T;  
   for(r=0;r<T;r++){
		cout << "Case #" << r+1 << ": ";
		cerr << "Case #" << r+1 << ": ";
			
		orden.clear();
		O.clear();
		B.clear();
		
		cin >> N;
		for(i=0;i<N;i++){
		   cin >> Robot >> Boton;
		   orden.push_back(Robot);
			if(Robot=='O'){
				O.push_back(Boton);
			}else{
				B.push_back(Boton); 
			}	
		}

		int posO = 1;
		int posB = 1;
		int index = 1;
		int indexO = 1;
		int indexB = 1;
		int destinoO = 1;
		int destinoB = 1;
		char proximoboton = orden[0];
		char turno = orden[0];
		bool finalO = false;
		bool finalB = false;
		int tiempo = 0;
		int evento = 0;
		bool press = false;
		
		if(O.size() == 0) finalO = true; else destinoO = O[0];
		if(B.size() == 0) finalB = true; else destinoB = B[0];
		
		while(!(finalO && finalB)){
		   evento++;
			switch(turno){
		   	case 'O':
			   	if(!finalO){
			   	   if(posO == destinoO && proximoboton == 'O' && !press){
			   	   	press=true;
			   	   	proximoboton = orden[index];
			   	   	index++;
			   	   	if(indexO == O.size()){ 
			   	   		finalO = true;
							}else{
				   	   	destinoO = O[indexO];
				   	   	indexO++;
				   	   }
						}else if(posO > destinoO){
							posO--;							
						}else if(posO < destinoO){
							posO++;
						}
					}
					turno = 'B';
					break;
		   	default:
		   		if(!finalB){
			   	   if(posB == destinoB && proximoboton == 'B' && !press){
			   	   	press=true;
			   	   	proximoboton = orden[index];
			   	   	index++;
			   	   	if(indexB == B.size()){
			   	   		finalB = true;
							}else{
				   	   	destinoB = B[indexB];
				   	   	indexB++;
				   	   }
						}else if(posB > destinoB){
							posB--;							
						}else if(posB < destinoB){
							posB++;
						}
					}
					turno = 'O';
		   		break;
			}
			if(evento%2==1) tiempo++; else press=false;			
		}
		
	   cout << tiempo << endl;
		cerr << tiempo << endl;
	}
}

