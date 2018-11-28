#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
	int N;
	
	cin >> N;
	for (int n=0;n<N;n++) {
		int C;
		cin >> C;
		string row;
		vector<int> M;
		int ans=0;
		for (int i=0;i<C;i++) {
			cin >> row;
			for (int j=C-1;j>=0;j--) {
				if (row[j]=='1') {
					M.push_back(j);
					break;
				}
				else if (j==0) M.push_back(0);
			}
		}
		/*for (int i=0;i<C;i++) {
			cout << M[i];
		}
		cout << endl;*/
		for (int i=0;i<C;i++) {
			// sort each row
			for (int j=i;j<C;j++) {
				if (M[j]<=i) {
					M.insert(M.begin(),M[j]);
					M.erase(M.begin()+j+1);
					ans+=j-i;
					//cout << ans<<endl;
					break;
				}
			}
		}
		cout << "Case #"<<(n+1)<<": "<<ans<<endl;
	}
	
	
	
	return 0;	
}
