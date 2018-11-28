#include <iostream>
#include <set>

using namespace std;

int main(){
	int a, b;
	int T;

	cin >> T;

	for (int cnt=0; cnt<T; ++cnt){
		cin >> a >> b;

		int d = 1;
		long factor = 1;
		while (a>=factor){
			factor*=10;
			d++;
		}
		d--;
		factor /= 10;

		long ans = 0;

		for (int i=a; i<=b; ++i){
			long ifactor = 10;
			long myfactor = factor;
			int done[20];
			int ndone = 0;
			for (int j=1; j<d; ++j){
				int nw =  (i % ifactor) * myfactor + i/ifactor ;
//				cout << i << "'s nw is " << nw << endl;
				if (nw >i && nw <=b) {
					bool okay = true;
					for (int k=0; k<ndone; ++k)
						if (done[k]==nw){
							okay = false;
							break;
						}
					if (okay) {
						ans++;
						done[ndone] = nw;
						ndone++;
					}
				}
				ifactor*=10;
				myfactor/=10;
			}
		}
		cout << "Case #" << cnt+1 << ": " << ans << endl;
	}

	return 0;
}
