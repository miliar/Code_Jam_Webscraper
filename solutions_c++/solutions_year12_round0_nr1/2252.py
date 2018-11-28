#include <iostream>
#include <cstdio>
using namespace std;
int main(){
	int T, i, j;
	char G[200], letters[27] = "yhesocvxduiglbkrztnwjpfmaq";
	cin >> T;
	for(i = 1; i <= T; i++){
		scanf("\n");
		for(j = 0; j < 200; j++)
			G[j] = 'A';
		cin.getline(G, 200);
		for(j = 0; j < 200; j++){
			if((G[j] >= 'a') && (G[j] <= 'z'))
				G[j] = letters[G[j]-'a'];
		}
		cout << "Case #" << i << ": " << G << endl;
	}
	return 0;
}
