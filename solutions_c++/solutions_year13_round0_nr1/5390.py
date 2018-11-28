#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <iomanip>
#include <cmath>
#include <algorithm>
#include <queue>
#include <map>
#include <string>
#include <vector>

#define forn(i,n) for(int i = 0; i < (n); i++)
#define forsn(i,s,n) for(int i = (s); i < (n); i++)
#define pb push_back
#define x first
#define y second


using namespace std;

char tictac[10][10];
int dx[4] = {0,1,1,1};
int dy[4] = {1,1,0,-1};

bool valid(int a, int b)
{
	return ( (a >= 0) and (a < 4) and (b >= 0) and (b < 4) );
}

int buscar(char c,int i, int j)
{
	//cout << c << " : " << endl;
	int res = -1;
	int a,b;
	bool found;
	forn(k,4){
		a = i; b = j;
		found = true;
		for(int l = 1; (l < 4) and valid(a,b); l++){
			a = a + dx[k];
			b = b + dy[k];
			//cout << tictac[a][b] << " ";
			if(tictac[a][b] != 'T'){if((tictac[a][b] != c) or (tictac[a][b] == '.')){ found = false; break; }}
		}
		if(found){
			if(c == 'X') res = 0;
			else res = 1;
			break;
		}
	}
	return res;
}

int main()
{
	int t;
	string output[4] = {"X won","O won","Draw","Game has not completed"};
	char act;
	int res;
	bool lleno;
	cin >> t;
	forn(caso,t){
		forn(i,4) forn(j,4) cin >> tictac[i][j];
		res = -1;
		lleno = true;
		bool win = false;
		for(int i = 0; (i < 4) and (!win); i++){
			for(int j = 0; (j < 4) and (!win); j++) {
				act = tictac[i][j];
				if(act == '.') lleno = false;
				if((act != '.') and (act != 'T')){
					res = buscar(act,i,j);
					if( (res == 0) or (res == 1) ) win = true;
				}
			}
		}

		if(!win){
			if(lleno) res = 2;
			else res = 3;
		}

		cout << "Case #" << (caso+1) << ": " << output[res] << endl;
	}
	return 0;
}
