#include <iostream>
#include <fstream>
using namespace std;

int find_next(char *r, int N, int R, int n) {
	while (n<N && r[n]!=R) n++;
	return n;
}

int main(int argc, char *argv[]) {
	
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");
	
	int C;
	fin>>C;
	for (int c=0;c<C;c++) {
		int b[100];
		char r[100];
		int p1=1,p2=1,N,n=0,t=0;
		fin>>N;
		for (int j=0;j<N;j++)
			fin>>r[j]>>b[j];
		int n1=find_next(r,N,'O',n);
		int n2=find_next(r,N,'B',n);
		while (n1<N||n2<N) {
			t++;
			bool push=false;
			if (n1<N) {
				if (p1<b[n1])
					p1++;
				else if (p1>b[n1])
					p1--;
				else if (n1==n)
					push=true;
			}
			if (n2<N) {
				if (p2<b[n2])
					p2++;
				else if (p2>b[n2])
					p2--;
				else if (n2==n)
					push=true;
			}
			if (push) {
				if (n==n1)
					n1=find_next(r,N,'O',++n);
				else if (n==n2)
					n2=find_next(r,N,'B',++n);
			}
		}
		
		fout<<"Case #"<<c+1<<": "<<t<<endl;
	}
	
	fin.close();
	fout.close();
	
	return 0;
	
}

