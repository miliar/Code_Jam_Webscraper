#include <iostream>
#include <fstream>
using namespace std;

int main() {
	fstream f, g;
	f.open("input.txt",ios::in);
	g.open("output.txt",ios::out);
	int T;	// input set
	int n;	// participant count
	int s;	// surprising count
	int p;	// minimum desired max-score
	int t;	// current total score
	int ns;	// no-surprising count
	int sc;	// surprising count
	int tt;	// total count
	f >> T;
	for(int i=1; i<=T; i++) {	// for each input set
		f >> n;
		f >> s;
		f >> p;
		ns = 0;
		sc = 0;
		for(int j=0; j<n; j++) {	// for each participant
			f >> t;
			if(p==1){
				if(t>=1)
					ns++;
			}
			else if(t >= 3*p-2)
				ns++;
			else if(t >= 3*p-4)
				sc++;
		}
		tt = ns + min(s,sc);
		g << "Case #" << i << ": " << tt << endl;
			//" s: " << s << " sc: " << sc << " ns: " << ns << //endl;
			//" p: " << p << " s: " << s << endl;
	}
	return 0;
}