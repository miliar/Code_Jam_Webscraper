#include <iostream>
using namespace std;

int main(){
	int T, N, K;
	cin >> T;
	for(int c = 1; c <= T; c++){
		cin >> N >> K;
		cout << "Case #" << c << ": ";
		if (K%(1<<N) == (1<<N)-1){
			cout << "ON\n";
		}
		else{
			cout << "OFF\n";
		}
	}
	return 0;
}
/*
Inicial

POWER   RECIB   NOREC   NOREC LAMP OFF
STATU   OFF     OFF     OFF

1 snap

POWER   RECIB   RECIB   NOREC LAMP OFF
STATU   ON      OFF     OFF

2 snap

POWER   RECIB   NOREC   NOREC LAMP OFF
STATU   OFF     ON      OFF

3 snap

POWER   RECIB   RECIB   RECIB LAMP OFF
STATU   ON      ON      OFF

4 snap

POWER   RECIB   NOREC   NOREC LAMP OFF
STATU   OFF     OFF     ON

5 snap

POWER   RECIB   RECIB   NOREC LAMP OFF
STATU   ON      OFF     ON

6 snap

POWER   RECIB   NOREC   NOREC LAMP OFF
STATU   OFF     ON      ON

7 snap

POWER   RECIB   RECIB   RECIB LAMP ON
STATU   ON      ON      ON



*/