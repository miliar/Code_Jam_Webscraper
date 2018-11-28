#include <iostream>
#include <cstdio>
#include <cmath>
#include <map>

using namespace std;

int main() {
		int t;
		int caso = 1;
		scanf("%d", &t);
		while(t--) {
			string aux0, aux1, xua;
			string ser = "";
			map <string, char> www;
			map <string, bool> noy;
			int c;
			scanf("%d", &c);
			int d, n;
			char m0, m1;
			for(int i = 0; i < c; ++i) {
				cin >> aux0;
				aux1 = "";
				m0 = aux0[0];
				m1 = aux0[1];
				aux1 = aux1 + m1;
				aux1 = aux1 + m0;
				www[aux1] = aux0[2];
				www[aux0.substr(0,2)] = www[aux1];
			}
			scanf("%d", &d);
			for(int i = 0; i < d; ++i) {
				cin >> aux0;
				aux1 = "";
				m1 = aux0[1];
				m0 = aux0[0];
				aux1 = aux1 + m1;
				aux1 = aux1 + m0;
				noy[aux1]  = true;
				noy[aux0.substr(0,2)] = noy[aux1];
			}
			scanf("%d", &n);
			cin >> xua;
			if(n != 0) {
				ser = ser + xua[0];
			}
			for(int i = 1; i < n; i++) {
				bool test = true;
				ser = ser + xua[i];
				while(test == true) {
					test = false;
					if(ser.size() > 1) 
						if(www[ser.substr(ser.size() - 2, 2)]) {
							ser[ser.size() - 2] = www[ser.substr(ser.size() - 2, 2)];
							ser.erase(ser.end() - 1);
							test = true;
					}
					if(ser.size() > 1) {
						for(int j = 0; j < ser.size() - 1; ++j) {
							m0 = ser[j];
							string auxilio;
							auxilio = "";
							auxilio = auxilio + m0;
							auxilio = auxilio + ser[ser.size() - 1];
							if(noy[auxilio]) {
								ser = "";
								test = false;
								break;
							}
						}
					}
				}
			}
			printf("Case #%d: [", caso);
			if(ser.size()) {
				cout << ser[0];
			}
			for(int i = 1; i < ser.size(); ++i) {
			printf(", ");
			cout << ser[i];
			}
			printf("]\n");
			caso = caso + 1;
			}
		return 0;
}
