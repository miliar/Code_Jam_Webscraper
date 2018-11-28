#include <stdio.h>
#include <iostream>
#include <vector>
#include <set>
#include <cmath>

using namespace std;

struct recicled{
	int m, n;	
};

class comparacion {
public:
	bool operator() ( const recicled &r1, const recicled &r2) {	
		if (r1.m < r2.m) return true;
		if (r1.m == r2.m && r1.n < r2.n) return true;
		else return false;
	}
};

int cantdig(int n){
	//retorna la cantidad de digitos que tiene un número entero
	// ejemplo: cantdig(1234)=4
	int aux=1;
	while (n>=10) {
		aux++;
		n=n/10;
	}
	return aux;	
}

int pot(int base, int expo){
	if (expo==0) return 1;
	else return base * pot(base, expo-1);
}

int digiguales(int n){
	// retorna true si todos los dígitos del número son iguales
	if (cantdig(n)==1)
		return 1;
	else
		if (n%10 == (n/10)%10)
		   return digiguales(n/10);
		else 
		   return 0;	
}

int dign(int n, int p){
	//retorna el dígito en la posición p de n, posiciones: 1,2,3,4,...
	
	if (cantdig(n)==p) return n%10;
	else return dign(n/10, p);	
}

int izquierda(int n, int dig){
	// retorna un entero conteniendo los dig digitos a la izquierda de un número
	// ejemplo: izquierda(1234, 2) retorna 12		
	int cd= cantdig(n);	
	// hay que dividir por 10 a n, tantas veces como cd - dig	
	for (int i=1; i<= (cd-dig); i++) n=n/10;	
	return n;	
}

int derecha(int n, int dig){
	// retorna un entero conteniendo los dig digitos a la derecha de un número
	// ejemplo: derecha(1234, 2) retorna 34		
	int cd= cantdig(n);		
	int aux= n % pot (10, dig);
	
	return aux;	
}

vector<int> reciclados(int m) {
	vector < int > vaux;
	int cd=cantdig(m);
	
	if (digiguales(m)) return vaux;
	
	for (int ancho=1; ancho<cd; ancho++){
		int valor= pot (10, cd-ancho);
			
		if (dign( (derecha(m,ancho)),1) == 0) continue;
				
		int aux= derecha(m, ancho)*valor + izquierda(m, cd-ancho);
		if (m<aux) vaux.push_back(aux);			
	}	
	return vaux;	
}

using namespace std;
int main() {
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);	

	int casos, a, b, m, n;
	cin >> casos; 
	
	for (int i=1; i<=casos; i++){
			
		cin >> a >> b;
	
		int cont=0;
		set<recicled, comparacion> conjunto;	
		for (m=a; m<=b; m++){
			// genero los números reciclados de m
			vector<int> rec= reciclados(m); 
			vector<int>::iterator i1;
				
			for (i1=rec.begin(); i1!= rec.end(); i1++)
				if (*i1 > m && *i1 <=b){
					cont++;
					//cout << m << " y " << *i1 << endl;
				
					recicled tempo;
					tempo.m=m; tempo.n=*i1;
					conjunto.insert(tempo);
				}
		}
		cout << "Case #" << i << ": " << conjunto.size() << endl;
		
		}
	return 0;
}
