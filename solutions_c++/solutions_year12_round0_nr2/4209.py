
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	int T;
	cin >> T;
	
	for (int i=1;i <=T;++i) {
		
		int N,S,p;
		
		cin >> N >> S >> p;
		
		vector<int> G;
		
		for (int j=0;j < N;++j) {int q; cin >> q; G.push_back(q);}
		
		int s1 = std::count_if(G.begin(),G.end(),[p](int q) { return (q+2)/3 >= p;});
		int s2 = std::count_if(G.begin(),G.end(),[p](int q) { return q < 3 ? q >= p : 1+(q+1)/3 >= p;})-s1;
		
		cout << "Case #" << i << ": " << s1 + std::min(s2,S) << endl;
	}
	return 0;
	
}