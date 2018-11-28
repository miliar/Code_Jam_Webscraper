#include <iostream>
#include <vector>

using namespace std;

int main () {
	int T, caso = 1;
	cin >> T;
	while(caso <= T) {
		int result = 0;
		int N;
		cin >> N;
		vector<int> x1;
		vector<int> x2;
		int a,b;
		for(int i = 0; i < N; i++) {
			cin >> a >> b;
			for(int j = 0; j < x1.size(); j++)
				if(x1[j]<a && x2[j]>b || x1[j]>a && x2[j]<b) result++;
			x1.push_back(a);
			x2.push_back(b);
		}
		cout << "Case #" << caso++ << ": " << result << endl;
	}
	return 0;
}
