#include <iostream>
#include <fstream>
using namespace std;

int main(int argc, char *argv[]) {
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");
	int n;
	fin>>n;
	char names[1010][110], queries[1010][110];
	int flags[110], steps, scount, qcount, changes;
	for (int i=0;i<n;i++) {
		
		int s;
		fin>>s;
		fin.ignore(255,'\n');
		for (int j=0;j<s;j++) {
			fin.getline(names[j],110,'\n');
			flags[j]=0;
		}
		
		int q;
		fin>>q;
		fin.ignore(255,'\n');
		if (q==0) {
			changes=0;
		} else {
			for (int j=0;j<q;j++)
				fin.getline(queries[j],110,'\n');
			
			qcount=changes=scount=0;
			steps=1; 
			
			int aux;
			while (qcount<q) {
				aux=0;
				while (strcmp(names[aux],queries[qcount])!=0) 
					aux++;
				if (flags[aux]!=steps) {
					flags[aux]=steps;
					scount++;
					if (scount==s) {
						changes++;
						steps++;
						scount=1;
						flags[aux]=steps;
					}
				}
				qcount++;
			}
		}
		
		fout<<"Case #"<<i+1<<": "<<changes<<endl;
	}
	fout.close();
	fin.close();
	return 0;
}

