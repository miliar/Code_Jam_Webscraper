#include <iostream>
using namespace std;

int main (){
	int T, i;
	
	cin >> T;
	
	for (int i=1; i<=T; i++){
		int n, soma=0, k=0, menor=0x3f3f3f3f, res=0;
		cin >> n;
		for (int j=1; j<=n; j++){
			int c;
			cin >> c;
			k=k^c;
			soma=soma+c;
			if (c<menor) menor=c;			
		}
		cout << "Case #" << i << ": ";
		if (k!=0) cout << "NO" << endl;
		else{
			res=soma-menor;
			cout << res << endl;
		}
	}
	
	return 0;
}
