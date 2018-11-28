#include <iostream>
#include <stdio.h>
#include <deque>
#include <algorithm>

// Bot Trust - Google code jam - Round 1C 2011

using namespace std;

struct elemento{
	int boton;
	int orden;};

typedef struct elemento Elemento;

int main() {
	freopen("A-large.txt", "r", stdin);
	freopen("out-large.txt", "w", stdout);
	
	int T;
	cin >> T;
	
	for (int i=1; i<=T; i++){
		int N;
		cin >> N;	
				
		deque<Elemento> O,B;		
		deque<Elemento>::iterator iO,iB;
		
        // leo N pares de entrada X 9 
		for (int j=1; j<=N; j++){
			char robot; int aux;
			Elemento E;
			
			cin >> robot >> aux;
					
			E.boton= aux;
			E.orden= j;
			if (robot=='O') O.push_back(E);
			else B.push_back(E);
		}
			
		// proceso los vectores O y B para contar segundos necesitados
		// actualizando la posicion de cada robot en el pasillo
		int segundos=0, posO=1, posB=1;
		
		while (!O.empty() && !B.empty()){
					
			if (O.front().orden < B.front().orden){
				//el proximo boton le corresponde pulsarlo a O.
				int destino=O.front().boton;
				
				while (posO!=destino){
					//se mueve O para acercarse a destino
					if (destino>posO) posO++;
					else posO--;
									
					//y aprovechamos a mover B si se puede
					if (posB != B.front().boton)
						if (B.front().boton>posB) posB++;
						else posB--;
				
					segundos++;
				}
				
				segundos++; //corresponde al pulsado del boton				
				//y aprovechamos a mover B si se puede
				if (posB != B.front().boton)
					if (B.front().boton>posB) posB++;
					else posB--;				
				
				O.pop_front();
			}
			else
			{
				//el proximo boton le corresponde pulsarlo a B.
				int destino=B.front().boton;
				
				while (posB!=destino){
					//se mueve B para acercarse a destino
					if (destino>posB) posB++;
					else posB--;
					
					//y aprovechamos a mover O si se puede
					if (posO != O.front().boton)
						if (O.front().boton>posO) posO++;
						else posO--;
					
					segundos++;
				}
				segundos++; //corresponde al pulsado del boton
				//y aprovechamos a mover O si se puede
				if (posO != O.front().boton)
					if (O.front().boton>posO) posO++;
					else posO--;
				
				B.pop_front();
			}	
		}
			
		// ahora hay que procesar la cola que todavía tenga elementos
		while (!O.empty()){
				
			int destino=O.front().boton;
					
			while (posO!=destino){
				if (destino>posO) posO++;
				else posO--;			
				segundos++;
			}
			segundos++; //corresponde al pulsado del boton				
			O.pop_front();
		}			
			
		while (!B.empty()){
			int destino=B.front().boton;
				
			while (posB!=destino){
				if (destino>posB) posB++;
				else posB--;		
				segundos++;
			}
			segundos++; //corresponde al pulsado del boton				
			B.pop_front();
		}								
		
		cout << "Case #" << i << ": " << segundos << endl;	
			
		O.clear();
		B.clear();
	}
	
	return 0;
} 
