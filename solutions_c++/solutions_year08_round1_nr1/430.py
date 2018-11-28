
#include <iostream>
#include <vector>
typedef long long LL;
using namespace std;

int main(void){
	int cases;
	cin >> cases;
	for(int case_no=1; case_no<=cases; case_no++){
		int n;
		cin >> n;
		vector<LL> v[2];
		for(int i=0; i<2; i++)
			for(int j=0; j<n; j++){
				long long t;
				cin >> t;
				v[i].push_back(t);
			}
		long long ans = 0;
		for(int i=0; i<2; i++)
			sort(v[i].begin(), v[i].end());
		for(int i=0; i<2; i++){
			while(v[i].size() && v[i].back() > 0LL && v[1-i].front() < 0LL){
				ans += v[i].back() * v[1-i].front();
				v[i].pop_back();
				v[1-i].erase(v[1-i].begin());
			}
		}
		for(int i=0; i<v[0].size(); i++)
			ans += v[0][i] * v[1][v[0].size()-1-i];
		cout << "Case #"<<case_no<<": "<< ans << endl;
	}
	return 0;
}
