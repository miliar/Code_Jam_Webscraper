#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

#define MAX 1000

int main(int argc, char *argv[]) {
	
	int pc=1,pf=0;
	int primos[MAX/2+5];
	primos[0]=2;
	int sets[MAX];
	for (int i=3;i<=MAX;i+=2) {
		bool primo=true;
		int l = sqrt(i);
		for (int j=3;j<=l;j+=2) {
			if (i%j==0) {
				primo=false;
				break;
			}
		}
		if (primo) {
			primos[pc]=i;
			pc++;
		}
	}
	
	ifstream fin("B-small-attempt0.in");
	ofstream fout("B-small-attempt0.out");
	int cant_cases;
	fin>>cant_cases;
	for (int case_number=0;case_number<cant_cases;case_number++) {
		int a,b,p;
		fin>>a>>b>>p;
		if (a>b) { int aux=b; b=a; a=aux; }
		int nsets=b-a+1,n=b-a+1;
		for (int i=0;i<n;i++) {
			sets[i]=i;
		}
		pf=pc;
		for (int i=0;i<pc;i++) {
			if (primos[i]>=p) { pf=i; break; }
		}
		for (int i=a;i<=b;i++) {
			for (int j=i+1;j<=b;j++) {
				if (sets[i-a]!=sets[j-a]) {
					bool es=false;
					for (int k=pf;k<pc;k++) {
						if (i%primos[k]==0 && j%primos[k]==0) {
							es=true;
							break;
						}
					}
					if (es) {
						nsets--;
						int sfc=sets[j-a];
						int stc=sets[i-a];
						for (int t=0;t<n;t++) {
							if (sets[t]==sfc)
								sets[t]=stc;
						}
					}
				}
			}
		}
		fout<<"Case #"<<case_number+1<<": "<<nsets<<endl;
	}
	fout.close();
	fin.close();
	return 0;
}

