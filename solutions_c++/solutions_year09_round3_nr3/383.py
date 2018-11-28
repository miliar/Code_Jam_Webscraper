#include <iostream>

using namespace std;

int main(){
	int T;
	int P, Q;
	int prison[105];
	int f[105][105];
   	
	cin >> T; 

	for (int cnt = 1; cnt <=T; ++cnt){
		cin >> P >> Q;
		prison[0] = 0;
		for (int i=1; i<=Q; ++i){
			cin >> prison[i];
		}
		prison[Q+1] = P+1;

	for (int i=0; i<Q; ++i){
		f[i][i+2] = (prison[i+2]-1)-(prison[i]+1);
	}

	for (int k=3; k<=Q+1; ++k){
		for (int i=0; i<=Q+1-k; ++i){
			f[i][i+k] = f[i][i+1] + f[i+1][i+k];
			for (int j=1; j<=k-1; ++j){
				if (f[i][i+k] >f[i][i+j] + f[i+j][i+k])
					f[i][i+k] = f[i][i+j] + f[i+j][i+k];
			}
			f[i][i+k] += (prison[i+k]-1) - (prison[i]+1);
			cerr << "f[" << i << "][" << i+k << "] = " << f[i][i+k] << endl;
		}
	}
	
	cout << "Case #" << cnt << ": ";
	cout << f[0][Q+1] << endl;
	}

	cerr << "Program Terminated Property." << endl;

	return 0;
}
