#include <iostream>
#include <fstream>
using namespace std;

#define FOR(cont,to) for (int cont=0;cont<to;cont++)

int main(int argc, char *argv[]) {
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");
	int n;
	fin>>n;
	fin.ignore(255,'\n');
	string s1;
	int pr[10000];
	for (int i=0;i<n;i++) {
		getline(fin,s1);
		int p1=0,p2;
		int c=0, b[15];
		while ((p2=s1.find(' ',p1))!=string::npos) {
			b[c++]=atoi(s1.substr(p1,p2-p1).c_str());
			p1=p2+1;
		}
		b[c++]=atoi(s1.substr(p1,s1.length()-p1).c_str());
		
		int k=2;
		bool found=false;
		while (!found) {
			found=true;
			FOR(e,c) {
				int x=k, bb=b[e], ac=0, prn=0;
				bool este_es=false, este_no=false;
				do {
					ac=0;
					do {
						ac+=(x%bb)*(x%bb);
						x=x/bb;
					} while (x);
					if (ac==1) { este_es=true; break; }
					FOR(ff,prn) if (pr[ff]==ac) { este_no=true; break; }
					pr[prn++]=ac;
					x=ac;
				} while (!este_es && !este_no);
				if (este_no) {found=false; break;}
			}
			k++;
		}
		cerr<<"done\n";
		fout<<"Case #"<<i+1<<": "<<k-1<<endl;
	}
	fout.close();
	fin.close();
}
