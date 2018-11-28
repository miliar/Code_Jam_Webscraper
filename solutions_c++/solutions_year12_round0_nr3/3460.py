/** Librerias **/
#include <iostream>
#include <iomanip>
#include <limits>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <cstdlib>
#include <cstdio>
#include <ctime>
#include <cmath>
#include <cstring>
#include <cctype>
#include <sstream>

/** Namespaces **/
using namespace std;

/** Funciones **/
bool es_reciclado(int n, int m){
	char cad_n[20], cad_m[20];
	sprintf(cad_n, "%d", n);
	sprintf(cad_m, "%d", m);

	string str_n(cad_n), str_m(cad_m);
	int tam_n = str_n.size(), tam_m = str_m.size();

	if (str_n == str_m)
		return true;

	if (tam_n != tam_n)
		return false;

	for (int ii = 1; ii < tam_n; ii++){
		if ((str_n.substr(ii, tam_n - ii) + str_n.substr(0, ii)) == str_m)
			return true;
	}
	return false;
}

/** Cuerpo principal **/
int main(){
	int T;
	cin >> T;

	for (int caso = 1; caso <=  T; caso++){
		int A, B;
		cin >> A >> B;

		int cont_r = 0;
		for (int m = B; m > A; m--){
			for (int n = m - 1; n >= A; n--){
				if (es_reciclado(n, m))
					cont_r++;
			}
		}
		cout << "Case #" << caso << ": " << cont_r << endl;
	}

	//FIN
	return 0;
}
