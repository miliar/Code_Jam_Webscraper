#include <fstream>

using namespace std;

int main () {

	ifstream fin("A-large.in",ios_base::in);	
	ofstream fout("A.out",ios_base::out);
	
	unsigned int t,n,k;
	
	fin >> t;
	
	for (int i = 0; i < t; i++) {

		fin >> n >> k;

		fout << "Case #" << i+1 << ": " << (((k+1)%(1 << n))? "OFF" : "ON") << endl;
	
	}
	
	fin.close();
	fout.close();
	
	return 0;

}
