#include <iostream>
#include <boost/lexical_cast.hpp>
#include <string>
using namespace std;

int main() {
	int Vi[1001][1001];
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++) {
		int A, B;
		cin >> A;
		cin >> B;
		for (int j = 0; j < 1001; j++)
			for (int k = 0; k < 1001; k++)
				Vi[j][k] = 0;
			
		int total = 0;
		for (int j = A; j <= B; j++) {
			string nuevo = boost::lexical_cast<string>(j);
			for (int k = 0; k < nuevo.size(); k++) {
				string creado = "";
				creado.append(nuevo,k,nuevo.size());
				creado.append(nuevo,0,k);
				int x = atoi(creado.c_str());
				if (x >= A && x <= B && x != j && Vi[x][j]== 0) {
					Vi[x][j] = 1;
					Vi[j][x] = 1;
					total++;
				}
			}
		}
		cout << "Case #" << i << ": " << total << endl;
		
	}
	
	return 0;
}
