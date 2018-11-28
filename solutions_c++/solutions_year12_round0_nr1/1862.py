#include <iostream>
#include <fstream>
#include <conio.h>
#include <string>

using namespace std;

int main(){
	fstream fin1, fin2;
	
	fin1.open("in.txt", fstream::in); 
	fin2.open ("A-small-attempt1.in", fstream::in);
	fstream fout;
	fout.open ("out.txt", fstream::out);
	
	char a[26];
	for(int i = 0; i < 26 ; i++)
		a[i] = '#';
	
	a['y' - 'a'] = 'a';
	a['e' - 'a'] = 'o';
	a['q' - 'a'] = 'z';
	
	for(int k = 0; k < 3; k++){
		string buf1, buf2;
		getline(fin1, buf1);
		getline(fin1, buf2);
		for(int i =0; i < buf1.length(); i++){
			a[buf1[i] - 'a'] = buf2[i];
		}
	}
	a['z' - 'a'] = 'q';
	
	
	int ntest;
	fin2 >> ntest;
	fin2.ignore();
	
	for(int k = 1; k <= ntest; k++){
		string buf1;
		getline(fin2, buf1);
		string buf2 = buf1;
		for(int i = 0; i < buf1.length(); i++){
			buf2[i] = a[buf1[i] - 'a'];
		}
		fout << "Case #" << k << ": " << buf2 << endl;
	}
	return 0;
}
