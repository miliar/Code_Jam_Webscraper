#include <iostream>
#include <vector>
#include <string>
#include <cstdio>
using namespace std;

void reemplazar (vector <string> &V, char letra) {
	for (int i=0; i<V.size(); i++) {
		for (int j=0; j<4; j++) {
			if (V[i][j] == 'T')
				V[i][j] = letra;
		}
	}
}


bool vertical (vector <string> V, char letra, int num) {
	bool flag = true;
	for (int j=0; j<4; j++) {
		for (int i=0; i<4; i++) {
			if (V[i][j] != letra) {
				flag = false;
				break;
			}
		}
		if (flag) {
			cout<<"Case #"<<num<<": "<<letra<<" won"<<endl;
			return true;
		}
		flag = true;
	}
	return false;
}



bool horizontal (vector <string> V, char letra, int num) {
	bool flag = true;
	for (int i=0; i<4; i++) {
		for (int j=0; j<4; j++) {
			if (V[i][j] != letra) {
				flag = false;
				break;
			}
		}
		if (flag) {
			cout<<"Case #"<<num<<": "<<letra<<" won"<<endl;
			return true;
		}
		flag = true;
	}
	return false;
}



bool oblicuo_izq_der (vector <string> V, char letra, int num) {
	bool flag = true;
	for (int i=0; i<4; i++) {
		if (V[i][i] != letra) {
			flag = false;
			break;
		}
	}
	if (flag) {
		cout<<"Case #"<<num<<": "<<letra<<" won"<<endl;
		return true;
	}
	return false;
}


bool oblicuo_der_izq (vector <string> V, char letra, int num) {
	bool flag = true;
	int j = 3;
	for (int i=0; i<4; i++) {
		if (V[i][j] != letra) {
			flag = false;
			break;
		}
		--j;
	}
	if (flag) {
		cout<<"Case #"<<num<<": "<<letra<<" won"<<endl;
		return true;
	}
	return false;
}


bool puntos (vector <string> V) {
	for (int i=0; i<4; i++) {
		for (int j=0; j<4; j++) {
			if (V[i][j] == '.') {
				return true;
			}
		}
	}
}



int main(int argc, char *argv[]) {
	freopen ("salida.out","w",stdout);
	int n,num=0;
	cin>>n;
	vector <string> A(4),B(4);
	
	while (num < n) {
		for (int i=0; i<4; i++) {
			cin>>A[i];
		}
		B=A;
		
		reemplazar(A,'X');
		reemplazar(B,'O');
		
		if (vertical(A,'X',num+1) || vertical(B,'O',num+1)) {
			num++;
			continue;
		}
		
		
		if (horizontal(A,'X',num+1) || horizontal(B,'O',num+1)) {
			num++;
			continue;
		}
		
		
		if (oblicuo_der_izq(A,'X',num+1) || oblicuo_der_izq(B,'O',num+1)) {
			num++;
			continue;
		}
		
		if (oblicuo_izq_der(A,'X',num+1) || oblicuo_izq_der(B,'O',num+1)) {
			num++;
			continue;
		}
		
		if (puntos(A))
			cout<<"Case #"<<num+1<<": "<<"Game has not completed"<<endl;
		else
			cout<<"Case #"<<num+1<<": "<<"Draw"<<endl;
		
		num++;
		
	}
	return 0;
}

