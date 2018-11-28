#include <cstdio>
#include <string>
#include <iostream>

using namespace std;

int diccionario[] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};

int main(){
	int n;
	string line;
	scanf("%d", &n);
	int c = 1;
	getline(cin,line);
	while(n--){
		getline(cin,line);
		string ans = "";
		for(int i = 0; i < line.length(); ++i){
			if('a' <= line[i] and line[i] <= 'z')
				ans += diccionario[line[i] - 'a'];
			else
				ans += ' ';
		}
		cout << "Case #" << c++ << ": " << ans  << endl;
	}
}
