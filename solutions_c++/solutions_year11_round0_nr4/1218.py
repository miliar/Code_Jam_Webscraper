#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string.h>
#include <iso646.h>
using namespace std; 

void Quicksort(int b, int t);
int colocar(int b, int t);
void EliminaElementosEnOrden();
void verElementos();

vector<int> elementos;
vector<int> orden;
int iteraciones;
	
int main(){

	freopen("Q4.in", "rt", stdin);
	freopen("Q4.out", "wt", stdout);
	 	
	int r,T;
	int C,N,i,j,k;
	  
   cin >> T;  
   for(r=0;r<T;r++){
		cout << "Case #" << r+1 << ": ";
		cerr << "Case #" << r+1 << ": ";
	
		elementos.clear();
		orden.clear();
		iteraciones = 0;
		cin >> N;
		for(i=0;i<N;i++){
			cin >> C;
			elementos.push_back(C);
			//cerr << C << ",";				
		}
		
		//ordenamos
		for(i=0;i<elementos.size();i++){
		  orden.push_back(elementos[i]);
		}
		sort(orden.begin(),orden.end());

	   //Iteramos
		for(i=0;i<elementos.size();i++){
			if(elementos[i] != orden[i]) iteraciones++;
		}
     	
		float x = iteraciones;
		printf("%.6f\n",x);
		cerr << x << endl;
	}
}
