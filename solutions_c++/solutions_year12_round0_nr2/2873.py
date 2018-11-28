#include <iostream>
#include <fstream>
using namespace std;

int S,p;

bool isbest (int x) {
	if (x<3*p-4) return false;
	else if (x>=3*p-2) return true;
	else if (x==0) return false;
	else if (((x==3*p-4)||(x==3*p-3))&&(S>0)) {
		S--;
		return true;
	}
	else return false;
}

int main () {
	ifstream fin ("dance.in");
	ofstream fout ("dance.out");
	int T,N,*t,w,counter=0;
	fin>>T;
	for (int q=1;q<=T;q++) {
		counter=0;
		fin>>N>>S>>p;
		t=new int [N];
		for (w=0;w<N;w++) {
			fin>>t[w];
		}
		for (w=0;w<N;w++) {
			if (isbest (t[w])) counter++;
		}
		fout<<"Case #"<<q<<": "<<counter<<'\n';
	}
	return 0;
}