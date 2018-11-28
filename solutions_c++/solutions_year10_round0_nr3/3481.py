#include <iostream>
#include <vector>
#include <algorithm>
#include <iterator>
#define pb(z) push_back(z)
#define all(z) (z).begin(), (z).end()
using namespace std;

int main(){
	unsigned int T,R,k,N,gi,i,j,RES,personas,m;
	vector<unsigned int> cola;
	cin >> T;
	for(i=1;i<=T;i++){
		cin >> R >> k >> N;
		cola.clear();
		for(j=0;j<N;j++){
			cin >> gi;
			cola.pb(gi);
		}
		RES = 0;
		for(m=1;m<=R;m++){
			personas = 0;
			for(j=0;j<N && personas<=k ; j++){
				if(personas+cola[j]>k) {  break; }
				else {
					personas += cola[j];
				}
			}
			RES += personas;
			if(j<N)
			rotate(cola.begin(),cola.begin()+j,cola.end());
		}
		cout << "Case #" << i <<": " << RES << endl;
	}


	return 0;
}
