#include <iostream>
#include <string>
#include <vector>

using namespace std;

int check(vector<string> &tablero, int mode, int num);
int checkRow(vector<string> &tablero, int num);
int checkColumn(vector<string> &tablero, int num);
int checkDiagonal(vector<string> &tablero, int num);
bool hayAlgunPunto(vector<string> &tablero);
void imprimirTablero(vector<string> &tablero);

int main (){
	
	unsigned long long T, k=1;
	string linea;
	
	string X, O, Draw, Not;
	X = "X won";
	O = "O won";
	Draw = "Draw";
	Not = "Game has not completed";
	
	cin >> T;
	
	
	while (k<=T){
		vector<string> tablero(4);
		
		cin >> linea;
		tablero[0]=linea;
		
		cin >> linea;
		tablero[1]=linea;
		
		cin >> linea;
		tablero[2]=linea;
		
		cin >> linea;
		tablero[3]=linea;
		
		//~ imprimirTablero(tablero);
		
		cout << "Case #" << k << ": ";
		
		
		int res;
		
		res = check(tablero, 0, 0);
		if (res == 1){
			cout << X << endl;
			++k;
			continue;
		}
		if (res == 2){
			cout << O << endl;
			++k;
			continue;
		}
		
		res = check(tablero, 0, 1);
		if (res == 1){
			cout << X << endl;
			++k;
			continue;
		}
		if (res == 2){
			cout << O << endl;
			++k;
			continue;
		}
		
		res = check(tablero, 0, 2);
		if (res == 1){
			cout << X << endl;
			++k;
			continue;
		}
		if (res == 2){
			cout << O << endl;
			++k;
			continue;
		}
		
		res = check(tablero, 0, 3);
		if (res == 1){
			cout << X << endl;
			++k;
			continue;
		}
		if (res == 2){
			cout << O << endl;
			++k;
			continue;
		}
	//~ ###################################################	
	//~ ###################################################
		res = check(tablero, 1, 0);
		if (res == 1){
			cout << X << endl;
			++k;
			continue;
		}
		if (res == 2){
			cout << O << endl;
			++k;
			continue;
		}
		
		res = check(tablero, 1, 1);
		if (res == 1){
			cout << X << endl;
			++k;
			continue;
		}
		if (res == 2){
			cout << O << endl;
			++k;
			continue;
		}
		
		res = check(tablero, 1, 2);
		if (res == 1){
			cout << X << endl;
			++k;
			continue;
		}
		if (res == 2){
			cout << O << endl;
			++k;
			continue;
		}
		
		res = check(tablero, 1, 3);
		if (res == 1){
			cout << X << endl;
			++k;
			continue;
		}
		if (res == 2){
			cout << O << endl;
			++k;
			continue;
		}
		
	//~ ###################################################	
	//~ ###################################################
		res = check(tablero, 2, 0);
		if (res == 1){
			cout << X << endl;
			++k;
			continue;
		}
		if (res == 2){
			cout << O << endl;
			++k;
			continue;
		}
		
		res = check(tablero, 2, 1);
		if (res == 1){
			cout << X << endl;
			++k;
			continue;
		}
		if (res == 2){
			cout << O << endl;
			++k;
			continue;
		}

		
		if (hayAlgunPunto(tablero)){
			cout << Not << endl;
		} else{
			cout << Draw << endl;
		}

		++k;
	}
	
	return 0;
}

int check(vector<string> &tablero, int mode, int num){
	
	int res=0;
	
	if (mode == 0){
		res = checkRow(tablero, num);
	}
	if (mode == 1){
		res = checkColumn(tablero, num);
	}
	if (mode == 2){
		res = checkDiagonal(tablero, num);
	}
	
	return res;
}

int checkRow(vector<string> &tablero, int num){
	int res = 0;
	bool hayO = false, hayX=false;
	
	for (int i = 0; i < 4; i++)
	{
		if (tablero[num][i] == 'X')
			hayX = true;
		else{
			if (tablero[num][i] == 'O')
				hayO = true;
			else{
				if (tablero[num][i] == '.')
					return 0;
			}
		}
	}
	
	if (hayO && hayX)
		res = 0;
	else{
		if (hayX)
			res = 1;
		else{
			if (hayO)
				res = 2;
		}
	}
	return res;
}

int checkColumn(vector<string> &tablero, int num){
	int res=0;
	bool hayO = false, hayX=false;
	
	for (int i = 0; i < 4; i++)
	{
		if (tablero[i][num] == 'X')
			hayX = true;
		else{
			if (tablero[i][num] == 'O')
				hayO = true;
			else{
				if (tablero[i][num] == '.')
					return 0;
			}
		}
	}
	
	if (hayO && hayX)
		res = 0;
	else{
		if (hayX)
			res = 1;
		else{	
			if (hayO)
				res = 2;
		}
	}
	return res;
	
}

int checkDiagonal(vector<string> &tablero, int num){
	int res=0;
	bool hayO = false, hayX=false;
	
	if (num==0){   
		for (int i = 0; i < 4; i++)
		{
			if (tablero[i][i] == 'X')
				hayX = true;
			else{
				if (tablero[i][i] == 'O')
					hayO = true;
				else{
					if (tablero[i][i] == '.')
						return 0;
				}
			}
		}
		
	} else{      
		for (int i = 0; i < 4; i++)
		{
			if (tablero[i][3-i] == 'X')
				hayX = true;
			else{
				if (tablero[i][3-i] == 'O')
					hayO = true;
				else{
					if (tablero[i][3-i] == '.')
						return 0;
				}
			}
		}

	
	}
	
	if (hayO && hayX)
		res = 0;
	else{
		if (hayX)
			res = 1;
		else{
			if (hayO)
				res = 2;
		}
	}
	return res;
}

bool hayAlgunPunto(vector<string> &tablero){
	for (int i = 0; i < 4; i++)
	{
		for (int j = 0; j < 4; j++)
		{
			if (tablero[i][j]=='.') return true;
		}
		
	}
	
	return false;
	
}

void imprimirTablero(vector<string> &tablero){
	for (int i = 0; i < 4; i++)
	{
		cout << tablero[i] << endl;
	}
	
}
