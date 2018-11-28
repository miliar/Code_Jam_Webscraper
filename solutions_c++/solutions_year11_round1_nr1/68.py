#include <iostream>
#include <fstream>
using namespace std;

#define FILENAME "A-large"

long long mcd(long long a, long long b) {
	if (a>b) return mcd(a-b,b);
	if (a<b) return mcd(a,b-a);
	return a;
}

int main(int argc, char *argv[]) {
	
	ifstream fin(FILENAME".in");
	ofstream fout(FILENAME".out");
	
	int C;
	fin>>C;
	for (int c=0;c<C;c++) {
		long long n,pd,pg;
		fin>>n>>pd>>pg;
		bool posible=true;
		if (pg==100 && pd<100) {
			posible=false;
		} else if (pd>0 && pg==0) {
			posible=false;
		} else if (n>=100 || pd==0) {
			posible=true;
		} else {
			long long m=mcd(pd,100);
			posible = 100/m<=n;
		}
		fout<<"Case #"<<c+1<<": "<< (posible?"Possible":"Broken") <<endl;
	}
	
	fin.close();
	fout.close();
	return 0;
	
}

