#include "assert.h"
#include "ctype.h"
#include "float.h"
#include "math.h"
#include "stdio.h"
#include "string.h"
#include "stdlib.h"
#include "stdarg.h"
#include "time.h"
#include "algorithm"
#include "numeric"
#include "functional"
#include "utility"
#include "bitset"
#include "vector"
#include "list"
#include "set"
#include "map"
#include "queue"
#include "stack"
#include "string"
#include "sstream"
#include "iostream"
using namespace std;

bool temp[10001];
int tam;
int resp=0;

void evaluar(){

	for (int j=tam-1 ; j>0 ; j-=2){
		if (temp[(j-1)/2]){
			temp[(j-1)/2]=temp[j]&&temp[j-1];
		}else{
			temp[(j-1)/2]=temp[j]||temp[j-1];
		}
		//cout << "Evaluando " << (j-1)/2 << endl;
	}

}

int main(){
	int casos;
	cin >> casos;
	for (int caso=0 ; caso<casos ; caso++){
		bool resul;
		cin >> tam >> resul;
		bool arbol[tam];
		bool change[tam];
		for (int i=0 ; i<tam/2 ; i++){
			cin >> arbol[i] >> change[i];
		}
		for (int i=tam/2 ; i<tam ; i++){
			cin >> arbol[i];
		}
		
		bool salir=false;
		if (!resul){
			for (int i=0 ; i<tam ; i++){
				arbol[i]=!arbol[i];
			}
		}
		int res=0;
		for (int k=0 ; k<tam && !salir ; k++){
			for (int i=0 ; i<tam/2 && !salir ; i++){
				/*cout <<"Operadores ";
				for(int ii=0 ; ii<tam/2 ; ii++)
					cout << arbol[ii] << " " ;*/
				for (int j=0 ; j<tam ; j++){
					temp[j]=arbol[j];
				}
				evaluar();
				if (temp[0]){
					salir=true;
					//res=i+1;
				}/*
					cout << "Evaluando ";
					for (int i=0 ; i<tam ; i++)
						cout << temp[i] << " ";
					cout << endl;*/
				
				if (!salir){
					bool changed=false;
					for (int j=0 ; j<tam/2 && !changed; j++){
						if (change[j] && arbol[j]){
							
							if ((temp[2*j+1] && !temp[2*j+2])||(!temp[2*j+1] && temp[2*j+2])){
							
								//cout <<" Cambio el nodo " << j <<  " por" << temp[2*j+1] << " "  << temp[2*j+2] << " end " << 2*j+1 << endl;
								changed=true;
								arbol[j]=false;
								res++;
							}
							
						}
					}
				}
				
				
			}
		}
		cout << "Case #" << (caso+1) << ": ";
		if (salir){
			cout << res << endl;
		}else
			cout << "IMPOSSIBLE\n";
	}
	return 0;
}
