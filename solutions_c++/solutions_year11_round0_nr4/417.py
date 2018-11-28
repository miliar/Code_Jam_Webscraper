#include <iostream>

using namespace std;

int main(){
	int test;
	cin >> test;
	for (int t=1 ; t<=test ; t++){
		int n;
		cin >> n;
		int res= n;
		for (int i=1 ; i<=n ; i++){
			int k;
			cin >> k;
			res-= (k==i);
		}
		cout << "Case #" << t << ": " << res << ".000000" << endl;
	}
	return 0;
}