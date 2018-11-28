#include <fstream>
#include <cstring>
using namespace std;


int nrc(int x) {
	int nr=0;
	while (x) {
		x/=10;
		nr++;
	}
	return nr;
}

int powten(int n) {
	int k=1;
	while (n) {
		n--;
		k*=10;
	}
	return k;
}
		

int shift(int x, int n, int nr) {
	int a,b,res;
	a=x/(powten(n));
	b=x%(powten(n));
	
	res=b*powten(nr-n)+a;
	return res;
}

int v[5],srs;
int main() {
	int t,l,a,b,nrr,q,x,i,j,sch,k;
	ifstream f("input.in");
	ofstream g("output.out");
	f>>t;
	for (l=1; l<=t; l++) {
		nrr=0;
		f>>a>>b;
		for (i=a; i<=b; i++) {
			x=i;
			q=nrc(x);
			for (j=1; j<q; j++) {
				sch=shift(x,j,q);
				v[j]=sch;
				srs=1;
				for (k=1; k<j; k++)
					if (v[k]==v[j])
						srs=0;
				if (sch>=a&&sch<=b&&sch!=i&&nrc(sch)==q&&sch>i&&srs) 
					nrr++;
				
				
			}
		}
					
		g<<"Case #"<<l<<": "<<nrr<<'\n';
	}
	
	g.close();
	return 0;
}
