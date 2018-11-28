#include <cstdlib>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	
	int N;
	cin >> N;
	vector <int> V;
	for(int i =0; i< N; i++){
		int X;
		cin >> X;
		cout << "Case #" << i+1 << ": ";
		V.resize(X);
		int a = 0;
		for(int j=0; j<X; j++){
			cin >> V[j];
			a ^= V[j];
		}
		if(a != 0) cout << "NO" << endl;
		else{
			long long vys = V[0];
			int min = V[0];
			for(int j = 1; j < X; j++){
				vys += V[j];
				if(V[j]< min) min = V[j];
			}
			vys -= min;
			cout << vys << endl;
		}
	}
    //system("PAUSE");
    return 0;
}
