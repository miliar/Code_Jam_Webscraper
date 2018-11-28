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

/** Globales **/
string map_char = "yhesocvxduiglbkrztnwjpfmaq";

/** Cuerpo principal **/
int main(){
	int T;
	cin >> T;

	string trash;
	getline(cin, trash);

	for (int ii = 1; ii <= T; ii++){
		string line;
		getline(cin, line);

		cout << "Case #" << ii << ": ";
		stringstream ss(line);
		string cad;
		bool prim = true;
		while (ss >> cad){
			if (!prim)
				cout << " ";
			for (int jj = 0; jj < cad.size(); jj++)
				cout << map_char[cad[jj] - 'a'];
			prim = false;
		}
		cout << endl;
	}

	//FIN
	return 0;
}
