#include <iostream>
#include <vector>

using namespace std;

int main() {
	long long t;
	cin >> t;
	/*int pow2[31];
	pow2[0]=1;
	for (int i=1;i<=30;i++) pow2[i]=pow2[i-1]*2;*/
	for (long long i=1;i<=t;i++) {
		long long r,n,k;
		cin >> r >> k >> n;
		vector<long long> g;
		vector<long long> run;
		vector<long long> atg;
		vector<long long> curans;
		run.push_back(0);
		atg.push_back(0);
		curans.push_back(0);
		for (long long j=0;j<n;j++) {
			long long size;
			cin >> size;
			g.push_back(size);
			run.push_back(0);
		}
		long long ans=0;
		for (long long j=1;j<=r;j++) {
			long long left=k;
			long long pos;
			if (j==1) pos=0;
			else pos=atg[atg.size()-1];
			long long startpos=pos;
			bool once=true;
			while (true) {
				// try fit pos in
				if ((once || startpos!=pos) && g[pos]<=left) {
					left-=g[pos];
					pos++;
					if (pos==g.size()) pos=0;
					once=false;
				}
				else break;
			}
			ans+=k-left;
			//cout << ans << " " << pos << endl;
			atg.push_back(pos);
			curans.push_back(ans);
			if (run[pos]==0) {
				run[pos]=j;
			}
			else { // cyc, calc all
				//cout << "Cyc calc" << endl;
				long long runstogo = r-j;
				long long runspercyc = j-run[pos];
				long long cyclesfit = runstogo/runspercyc;
				long long eupercyc = curans[curans.size()-1] - curans[curans.size()-1-runspercyc];
				long long extraruns = runstogo%runspercyc;
				long long fingroup = run[pos]+extraruns;
				long long extraeu = curans[fingroup]-curans[run[pos]];
				//cout << run[pos] << " " << atg[run[pos]];
				/*cout << "Cur run done = " << j << endl;
				cout << "runstogo = " << runstogo << endl;
				cout << "runspercyc = " << runspercyc << endl;
				cout << "cyclesfit = " << cyclesfit << endl;
				cout << "eupercyc = " << eupercyc << endl;//<< " = " << curans[curans.size()-1] << "-" << curans[curans.size()-1-runspercyc] << endl;
				cout << "extraruns = " << extraruns << endl;
				cout << "extraeu = " << extraeu << endl; //" = " << curans[fingroup] << "-" << curans[atg[run[pos]]] << endl;
				*/ans += eupercyc*cyclesfit + extraeu;
				break;
			}
		}
		cout << "Case #" << i << ": " << ans << endl;
	}
	return 0;
}
