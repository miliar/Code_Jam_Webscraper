#include <cstdio>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <functional>

#define infilename "D-large.in" 
#define outfilename "output.txt" 

using namespace std; 

int n, m , num[1009]; 
fstream fin, fout ; 

void openFile() {
	fin.open(infilename,ios::in);
	fout.open(outfilename,ios::out);
}

void closeFile() {
	fin.close();
	fout.close();
}


void process() {
	int cnt = m ; 
	for (int i=0;i<m;i++) { if (num[i]==i+1) cnt--; }
	fout << cnt << ".000000" ; 
}

int main()
{
	openFile() ;

	fin >> n ; 

	for(int i=0;i<n;i++) {
		fin >> m ; 

		for(int j=0 ;j<m;j++) {
			fin >> num[j] ; 
		}
		fout << "Case #" << i+1 << ": ";
		process();
		fout << endl ; 
	}

	closeFile();

	return 0;
}
