#include <fstream>
using namespace std;
char v[33][33],fin[101];
int lgfin,fr[35],el[35];
int main() {
	int i,j,l,n,t;
	char c1,c2,c3,chr;
	n=0;
	ifstream f("magicka.in");
	ofstream g("magicka.out");
	f>>t;
	for (l=1; l<=t; l++) {
		for (i=1; i<=35; i++)
			fr[i]=0;
		for (i=1; i<=30; i++)
			for (j=1; j<=30; j++)
				v[i][j]='f';
		for (i=1; i<=30; i++)
			el[i]=0;
		f>>n;
		for (i=1; i<=n; i++) {
			f>>c1>>c2>>c3;
			v[(int)c1-64][(int)c2-64]=c3;
			v[(int)c2-64][(int)c1-64]=c3;
		}
		f>>n;
		for (i=1; i<=n; i++) {
			f>>c1>>c2;
			el[(int)c1-64]=(int)c2-64;
			el[(int)c2-64]=(int)c1-64;
		}
		f>>n;
		lgfin=0;
		for (i=1; i<=n; i++) {
			f>>chr;
			if (lgfin>0) {
				if (v[(int)chr-64][(int)fin[lgfin]-64]!='f') {
					fr[(int)fin[lgfin]-64]--;
					fr[(int)v[(int)chr-64][(int)fin[lgfin]-64]-64]++;
					fin[lgfin]=v[(int)chr-64][(int)fin[lgfin]-64];
				}
				else if (fr[el[(int)chr-64]]>0) {
					lgfin=0;
					for (j=1; j<=30; j++)
						fr[j]=0;
				}
				else {
					lgfin++;
					fin[lgfin]=chr;
					fr[(int)chr-64]++;
				}				
			}
			else {
				lgfin++;
				fr[(int)chr-64]++;
				fin[lgfin]=chr;
			}
		}
		g<<"Case #"<<l<<": ";
		if (!lgfin)
			g<<"[]"<<'\n';
		else {
			g<<"[";
			for (i=1; i<lgfin; i++)
				g<<fin[i]<<", ";
			g<<fin[lgfin]<<"]"<<'\n';
		}
	}
	f.close();
	g.close();
	return 0; }
	
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			