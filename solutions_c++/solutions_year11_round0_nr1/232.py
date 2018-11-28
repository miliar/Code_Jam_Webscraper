#include <cstdio>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <functional>

#define infilename "A-large.in" 
#define outfilename "output.txt" 

using namespace std; 

int n, m ; 
int seq[120][2] ; 
fstream fin, fout ; 

void openFile() {
	fin.open(infilename,ios::in);
	fout.open(outfilename,ios::out);
}

void closeFile() {
	fin.close();
	fout.close();
}


int process() {
	int pos[2] , next , tot=0;
	pos[0] = pos[1] = 1 ;
	next = 1 ; 
	for(int i=0;i<m;i++) {
		int first = seq[i][0] , second = 1-seq[i][0] , gap1 =abs(pos[first]-seq[i][1])+1 ; 

		next = pos[second] ;  
		for(int j=i+1 ; j<m;j++) {
			if (seq[j][0] == second ) { next = seq[j][1] ; break; }
		}

		tot += gap1 ; pos[first] = seq[i][1] ; 

		int gap2 = abs(pos[second]-next); 
		if (gap2>=gap1) {
			if ( pos[second]<next ) { pos[second] += gap1 ; }
			else { pos[second] -= gap1 ; }
		} else {
			pos[second] = next ; 
		}
	}
	return tot;
}

int main()
{
	openFile() ;

	fin >> n ; 

	for(int i=0;i<n;i++) {
		fin >> m ; 

		for(int j=0 ;j<m;j++) {
			char temp ; 
			fin >> temp ;
			seq[j][0] = (temp=='B' || temp=='b')?0:1 ; 
			fin >> seq[j][1] ; 
		}
		fout << "Case #" << i+1 << ": " << process() << endl ; 
	}

	closeFile();

//	printf("test\n");

//	char temp = getchar();
	return 0;
}
