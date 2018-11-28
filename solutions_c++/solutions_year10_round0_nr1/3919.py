#include <iostream>
using namespace std;

int main(){
	int n;

	cin >> n;
	
	for (int i = 1; i <= n; i++){
		bool res;
		int a,b;
		cin >> a >> b;
		int tes = 1 << (a);
		int tis = b % tes;
		if (tis != tes - 1)
			res = false;
		else
			res = true;
			
		if (!res)
			cout << "Case #" << i << ": OFF" << endl;
		else
			cout << "Case #" << i << ": ON" << endl;
	}
	return 0;
}
