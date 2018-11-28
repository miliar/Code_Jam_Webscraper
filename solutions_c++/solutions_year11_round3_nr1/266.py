#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <map>
#include <vector>
using namespace std;

int n, r, c;
int t;
int m[100][100];
char a;

int main(){
	scanf("%d", &t);
	
	for (int C = 1; C <= t; C++){
		printf("Case #%d:\n", C);
		
		scanf("%d %d", &r, &c);
		memset(m, 0, sizeof m);
		int counter = 0;
		for (int i = 0; i < r; i++){
			for (int j = 0; j < c; j++){
				cin >> a;
				if (a == '#'){
					counter++;
					m[i][j] = 1;
				}
				else{
					m[i][j] = 0;
				}
			}
		}
		
		if (counter % 4 != 0){
			puts("Impossible");
		}
		else{
			bool ok = true;
			for (int i = 0; i < r; i++){
				for (int j = 0; j < c; j++){
					if (m[i][j] == 1){
						bool ok2 = true;
						for (int k = i; k < i+2; k++){
							for (int l = j; l < j+2; l++){
								if (m[k][l] != 1){
									ok2 = false;
									k = 3;
									break;
								}
							}
						}
						if (ok2){
							int temp = 10;
							for (int k = i; k < i+2; k++){
								for (int l = j; l < j+2; l++){
									m[k][l] = temp;
									temp++;
								}
							}
						}
						else{
							i = r;
							ok = false;
							break;
						}
					}
				}
			}
			
			if (ok){
				for (int i = 0; i < r; i++){
					for (int j = 0; j < c; j++){
						if (m[i][j] == 0)
							cout << '.';
						else if (m[i][j] == 10)
							cout << '/';
						else if (m[i][j] == 11)
							cout << '\\';
						else if (m[i][j] == 12)
							cout << '\\';
						else cout << '/';
						/*switch(m[i][j]){
							case 0:
								cout << '.';
							case 10:
								cout << '/';
							case 11:
								cout << '\\';
							case 12:
								cout << '\\';
							case 13:	
								cout << '/';
							default:
								cout << '#';
						}*/
						//cout << m[i][j] << ' ';
					}
					cout << endl;
				}
			}
			else{
				puts("Impossible");
			}
		}
	}
	return 0;
}

