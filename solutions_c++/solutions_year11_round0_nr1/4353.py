#include <fstream>
using namespace std;
int b[101],o[101],v[202],s[202];
char c[202];
int main () {
	int i,n,t,l,posb,poso,cr,scr,sposo,sposb;
	ifstream f("a-small.in");
	ofstream g("a-small.out");
	f>>t;
	for (l=1; l<=t; l++) {
		f>>n;
		for (i=1; i<=n; i++)
			f>>c[i]>>v[i];
		posb=poso=sposo=sposb=1;
		sposo=sposb=0;
		for (i=1; i<=n; i++) {
			if (c[i]=='O') {
				cr=poso;
				scr=sposo;
			}
			else {
				cr=posb;
				scr=sposb;
			}
			if (c[i]==c[i-1])
				s[i]=s[i-1]+abs(v[i]-v[i-1])+1;
			else if (c[i]!=c[i-1])
				s[i]=max(s[i-1],scr+abs(v[i]-cr))+1;
			if (c[i]=='O') {
				poso=v[i];
				sposo=s[i];
			}
			else {
				posb=v[i];
				sposb=s[i];
			}
		}
		g<<"Case #"<<l<<": "<<s[n]<<'\n';
	}
	g.close();
	return 0; }
				
			
			