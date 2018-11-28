#include <iostream>

using namespace std;

char eng[] = "abcdefghijklmnopqrstuvwxyz";
char goo[] = "ynficwlbkuomxsevzpdrjgthaq";

char code(char c) {
	for(int i = 0; eng[i] != 0; i++) if(c == eng[i]) return goo[i];
	return c;
}

char decode(char c) {
	for(int i = 0; goo[i] != 0; i++) if(c == goo[i]) return eng[i];
	return c;
}

int main(){
	int T;
	cin >> T;
	
	char line[256]; cin.getline(line, 256);
	for(int i = 0; i < T; i++){
		cin.getline(line, 256);
		for(int j = 0; line[j] >= 32; j++) {
			line[j] = decode(line[j]);
		}
		cout << "Case #" << (i+1) << ": ";
		cout << line << endl;
	}
	return 0;
}
