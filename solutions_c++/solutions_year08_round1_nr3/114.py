#include <iostream>
#include <map>
#include <vector>
#include <sstream>
using namespace std;
map<int, int> ans;
vector<int> vec;
int mapping[110];
int main(){
	int cases, m = -1;
	cin >> cases;
	for (int i = 0; i != cases; ++i){
		int n;
		cin >> n;
		if (n > m) m = n;
		mapping[i] = n;
		ans.insert(make_pair(n, 0));
	}
	int a = 2, b = 6;
	for (int i = 0; i != m; ++i){
		int temp = (6 * b - a * 4) % 1000;
		a = b; b = temp;
		if (ans.find(i + 2) != ans.end()) ans[i + 2] = temp;
		if (i % 10000000 == 0) cerr << i << endl;
	}
	for (int i = 0; i != cases; ++i){
		int temp = mapping[i];
		int x = (ans[temp] + 999) % 1000;
		ostringstream os;
		os << x;
		string out = os.str();
		out = "000" + out; out = out.substr(out.size() - 3, 3);
		cout << "Case #" << i + 1 << ": " << out << endl;
		//system("pause");
	}
	return 0;
	//system("pause");
}
