#include <fstream>
using namespace std;

int main() {
	int n,l,t,i,bst,vl,p,s;
	ifstream f("input.in");
	ofstream g("output.out");
	f>>t;
	for (l=1; l<=t; l++) {
		bst=0;
		f>>n>>s>>p;
		for (i=1; i<=n; i++) {
			f>>vl;
			if (!(vl%3)) {
				if (vl/3>=p)
					bst++;
				else if (vl/3+1>=p&&s&&vl!=0) {
					bst++;
					s--;
				}
			}
			else if (vl%3==1) {
				if (vl/3+1>=p)
					bst++;
			}
			else if (vl%3==2) {
				if (vl/3+1>=p)
					bst++;
				else if (vl/3+2>=p&&s) {
					bst++;
					s--;
				}
			}
		}
		g<<"Case #"<<l<<": "<<bst<<'\n';
	}
	
	g.close();
	return 0;
}
