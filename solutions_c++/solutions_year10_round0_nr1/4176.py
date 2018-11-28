#include <fstream>

using namespace std;

int main () {

	ifstream fin("A-small.in");	
	ofstream fout("A.out");
	
	unsigned int m,h,l;
	
	fin >> m;
	
	for (int i = 0; i < m; i++) {

		fin >> h >> l;

		fout << "Case #" << i+1 << ": " << (((l+1)%(1 << h))? "OFF" : "ON") << endl;
	
	}
	
	fin.close();
	fout.close();
	
	return 0;

}
