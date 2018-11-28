#include <iostream>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

class Nodo {
	public:
		int pos;
		int Boton;
		Nodo *Prox;
		
		Nodo(){
			pos = 0;
			Boton = 0;
			Prox = NULL;
		}
};

class Lista {
	public:
		Nodo *Prim;
		int Tam;

		Lista(){
			Prim = NULL;
			Tam = 0;
		}

		void Insertar(int p, int b){
			Nodo *A = new Nodo();
			A -> Boton = b;
			A -> pos = p;
			if (Prim != NULL){
				Nodo *aux = Prim;
				while (aux -> Prox != NULL){
					aux = aux -> Prox;
				}
				aux -> Prox = A;
			} else {
				Prim = A;
			}
			Tam++;
		}
		
		void Eliminar(){
			if (Prim != NULL){
				Nodo *aux = Prim;
				Prim = Prim -> Prox;
				delete(aux);
				Tam--;
			}
		}
};


int main () {
	int T, N, posB;
	string R;
	Lista O, B;
	cin >> T;
	for (int i = 0; i < T; i ++){
		cin >> N;
		for (int j = 0; j < N; j++){
			cin >> R;
			cin >> posB;
			if (R == "O"){
				O.Insertar(j, posB);
				
			} else {
				B.Insertar(j, posB);
			}
		}
		
		int cont = 0, posO=1;
		posB = 1;
		while (O.Prim != NULL && B.Prim != NULL){
			//cout << "Entro a " << cont+1 << endl;
			if (O.Prim -> pos < B.Prim -> pos){
				if (O.Prim -> Boton == posO){
					O.Eliminar();
				}else {
					if (O.Prim -> Boton < posO){
						posO--;
					}else{
						posO++;
					}
				}
				if (B.Prim -> Boton > posB){
					posB++;
				} else {
					if (B.Prim -> Boton < posB){
						posB--;
					}
				}
			} else {
				if (B.Prim -> pos < O.Prim -> pos){
					if (B.Prim -> Boton == posB){
						B.Eliminar();
					} else {
						if (B.Prim -> Boton < posB){
							posB--;
						} else {
							posB++;
						}
					}
					if (O.Prim -> Boton > posO){
						posO++;
					} else {
						if (O.Prim -> Boton < posO){
							posO--;
						}
					}
				}
			}
			cont++;
			//cout << cont << endl;
		}
		
		//cout << "Salgo" << endl;
		
		while (O.Prim != NULL) {
			if (O.Prim -> Boton == posO){
					O.Eliminar();
			}else {
				if (O.Prim -> Boton < posO){
					posO--;
				}else{
					posO++;
				}
			}
			cont++;
		} 
		while (B.Prim != NULL) {
			if (B.Prim -> Boton == posB){
					B.Eliminar();
			}else {
				if (B.Prim -> Boton < posB){
					posB--;
				}else{
					posB++;
				}
			}
			cont++;
		}
		cout << "Case #" << i+1 << ": " << cont << endl;
		
	} 
	return 0;
}
