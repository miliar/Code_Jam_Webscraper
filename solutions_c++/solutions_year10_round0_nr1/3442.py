#include <fstream>
using namespace std;
int main (int argc, char * const argv[]) {
	
	int t,test,k,n,i,rez;
	ifstream in("A.in");
	ofstream out("A.out");
	in >> t;
	
	for (test = 0; test < t; test++) {
		
		in >> n >> k;
		rez = 0;
		for (i=0; i<n; i++) {
			if(k & 1){
				rez++;
			}
			k >>= 1;
		}
		if(rez == n ){
			out << "Case #" << test+1 << ": ON" << endl;
		}else{
			out << "Case #" << test+1 << ": OFF" << endl;
		}
	}
	
	
	
	return 0;
}
