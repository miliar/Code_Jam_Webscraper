#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <string>

using namespace std;

int main(void){

	freopen("input.txt","r", stdin);
	
	int n;


	string letters[30];

	cin >> n >> ws;

	string output[n];
	string input[n];
	for(int i = 0; i < n; i++){
		getline(cin, input[i]);
	}

	freopen("output.txt","r", stdin);
	for(int i = 0; i < n; i++){
		getline(cin, output[i]);
	}


	for(int i = 0; i < n; i++){
		for(int j = 0; j < input[i].size(); j++){
			if(input[i][j] != ' ') 
			
		  letters[input[i][j] - 'a'] = output[i][j];

		}
	} 

	letters['q' - 'a'] = 'z';
	letters['z' - 'a'] = 'q';
	


	freopen("hola.txt", "r", stdin);
	freopen("salida.txt", "w", stdout);

	int m;

	cin >> m >> ws;

	string ip[m];
	string op[m];
	for(int i = 0; i < m; i++){
		getline(cin, ip[i]);
	}


	for(int i = 0; i < m; i++){
	//	cout << input[i];

		cout << "Case #" << i + 1 << ": ";
		for(int j = 0; j < ip[i].size(); j++){

		if(ip[i][j] != ' ')
			 cout << letters[ip[i][j] - 'a'];
		else
			cout << ' ';

		}
		
		cout << endl;
	}

	

	return 0;
}
