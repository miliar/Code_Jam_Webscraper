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
int table[120][120] ; 
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
	
	double wp[120], owp[120], oowp[120] ; 
	for(int i=0;i<n;i++) {
		wp[i]=0 ; int cnt = 0 ;
		for(int j=0;j<n;j++) {
			if ( table[i][j] >= 0 ) { cnt++ ; }
			if ( table[i][j] == 1 ) wp[i]++ ; 
		}
		wp[i] = wp[i]/cnt ; // fout << wp[i] << " " ;
	} //fout << endl ; 

	for(int i=0;i<n;i++) {
		owp[i]=0 ; int cnt = 0 ; double wp2[120];
		for(int j=0;j<n;j++) {
			if ( table[i][j] >= 0 ) { 
				cnt++ ; wp2[j] = 0 ; int cnt2= 0 ; 
				for(int k=0;k<n;k++ ) {
					if ( k==i) continue ; 
					if ( table[j][k] >= 0 ) { cnt2++ ; }
					if ( table[j][k] == 1 ) wp2[j]++ ; 
				}
				owp[i] += (wp2[j]/cnt2);
			}
		}
		owp[i] = owp[i]/cnt ;  // fout << owp[i] << " " ;
	} //fout << endl ; 

	for(int i=0;i<n;i++) {
		oowp[i] = 0 ; int cnt =0 ; 
		for(int j=0;j<n;j++) {
			if ( table[i][j]>=0 ) {
				cnt++ ; oowp[i] += owp[j]  ; 
			}
		}
		oowp[i] /= cnt ; //fout << oowp[i] << " " ;
	} //fout << endl ; 

	for(int i=0;i<n;i++) {
		fout << wp[i]*0.25+owp[i]*0.5+oowp[i]*0.25 << endl ; 
	}

	return m;
}

int main()
{
	int cases;
	openFile() ;

	fin >> cases ; 
	fout.precision(12);

	for(int i=0;i<cases;i++) {
		fin >> n ; 

		for(int j=0 ;j<n;j++) {
			for(int k=0;k<n;k++) {
				char temp ; 
				fin >> temp ;
				table[j][k] = (temp=='.')?-1 : temp-'0' ; 
			} 
		}
		fout << "Case #" << i+1 << ":" << endl;
		process()  ; 
	}

	closeFile();

//	printf("test\n");

//	char temp = getchar();
	return 0;
}
