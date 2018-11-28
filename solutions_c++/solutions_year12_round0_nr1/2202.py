/*
ID: andrewc1
PROG:
LANG: C++
*/
#include <fstream>
#include <stdlib.h>


using namespace std;

int main(){
	char translator[26] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};
	ifstream fin("input.in");
	ofstream fout("output.txt");
	int n;
	fin >> n;
	fin.get();//to remove an extra newline
	char nc;
	for(int i = 1;i<=n;i++){
		fout << "Case #" << i << ": ";
		nc = fin.get();
		while(nc != '\n'){
			if(nc!=' '){
				fout << translator[nc-'a'];
			}else{
				fout << ' ';
			}
			nc = fin.get();
		}
		fout << '\n';
	}
	return 0;
}
