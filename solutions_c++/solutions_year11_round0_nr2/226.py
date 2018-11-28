#include <cstdio>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <functional>

#define infilename "B-large.in" 
#define outfilename "output.txt" 

using namespace std; 

int ncases, c, d, n ;
char combine[100][4], opposed[100][3], seq[200];
string answer; 
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
	answer = "" ; answer.reserve(200);
	int l = 0 ; 
	for(int i=0; i<n;i++) {
		if (l==0 ) {
			answer += seq[i] ; l++ ;
			continue ; 
		}

		bool found = false ; 
		for(int j=0 ;j<c ;j++) {
			if ( (combine[j][0] == seq[i] && combine[j][1] == answer[l-1] ) 
				|| ( combine[j][1] == seq[i] && combine[j][0] == answer[l-1] ) ) {
				answer[l-1] = combine[j][2] ; 
				found = true ; 
				break; 
			} 
		}

		if (found) continue ; 

		for(int j=0;j<d;j++) {

			if ( (opposed[j][0] == seq[i] && answer.find(opposed[j][1]) != -1  ) 
				|| ( opposed[j][1] == seq[i] && answer.find(opposed[j][0]) != -1 ) ) {
				answer = "" ; l = 0 ; 
				found = true ; 
				break; 
			} 
		}

		if (!found) { answer += seq[i] ;l++ ; }
	}


	fout << "[" ; 
	for(int i=0;i<l-1;i++) fout << answer[i] << ", " ; 
	if (l>0) fout << answer[l-1] ;
	fout << "]" ; 

}

int main()
{
	openFile() ;

	fin >> ncases ; 

	for(int i=0;i<ncases;i++) {
		fin >> c ; for(int j=0;j<c;j++) { fin >> combine[j] ; }
		fin >> d ; for(int j=0;j<d;j++) { fin >> opposed[j] ; }
		fin >> n ; fin >> seq ; 

		fout << "Case #" << i+1 << ": ";
		process();
		fout << endl ; 
	}

	closeFile();

	return 0;
}
