#include <iostream>
#include <stdlib.h>
#include <string.h>
#include <fstream>

using namespace std;

//int max = 1000;
int counter(int a, int b){
	
	int x,y, p, c = 0;
	for(int k = 1000; k >= 1; k /=10){
		if(a >= k){
			for(int i = a; i < b; i++){
				for(int j = k; j >= 10; j /=10){
					x = i%j;
					y = i/j;
					p = x*(k*10 / j) + y;
					if(p > i && p <= b){ 
						c++;
						//cout << j << " " << i << " " << p << endl;
					}
				}
			
			}
			break;
		}
	}
	return c; 
}
int main(int argc, char** argv){
	string s;
	ifstream file;
	ofstream out;

	file.open (argv[1]);
    out.open (argv[2]);

	getline(file,s); 
	int n = atoi(s.c_str());
	char c;
	int a;
	int b;
	for(int i = 0; i < n; i++){
		out << "Case #" << i + 1 << ": ";
		
		file >> a;
		file >> b;
		out << counter(a, b) << endl;
	}
}
