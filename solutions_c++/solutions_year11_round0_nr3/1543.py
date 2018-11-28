#include<fstream>
#include<iostream>
#include<string>

using namespace std;

int main(){

	ifstream fin("C-large.in");
	ofstream fout("C-large.out");
	cin.rdbuf(fin.rdbuf());
	cout.rdbuf(fout.rdbuf());	


	int n,m,sum,x,xor;


	int ntc;
	cin >> ntc;
	for (int tc=1;tc<=ntc;tc++){
		m = INT_MAX;
		sum = xor = 0;
		cin >> n;
		while(n--){
			cin >> x;
			m = min(m,x);
			sum += x;
			xor ^= x;
		}
		cout << "Case #" << tc << ": ";
		if (xor)
			cout << "NO" << endl;
		else
			cout << sum-m << endl;

	}


	

	return 0;
}