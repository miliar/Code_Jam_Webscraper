#include <iostream>
#include <algorithm>

using namespace std;

int main(){
	int T, N;
	cin >> T;
	
	for (int t = 1; t <= T; t++){
		cin >> N;
		int d = 0;
		int n;
		for (int i = 1; i <= N; i++){
			cin >> n;
			if (i != n)
				++d;
		}
		cout << "Case #" << t << ": " << d << endl;		
	}
	return 0;
}
