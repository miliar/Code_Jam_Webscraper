#include <iostream>
#include <vector>

using namespace std;


int main() {
	int cases;
	cin >> cases;
	for(int c=0; c<cases; c++) {
		int k;
		string str, str0;

		cin >> k >> str0;

		vector<int> p;
		for(int i=0; i<k; i++) p.push_back(i);
		
		int ans = 1<<29;
		do {
			str = str0;
			for(int i=0; i<str.size(); i+=k) {
				for(int j=0; j<k; j++)  str[i+p[j]] = str0[i+j];
			}

			int cur=0;
			int pos=0;
			while(pos < str.size()) {
				do {
					pos++;
				} while(pos < str.size() && str[pos] == str[pos-1]);
				cur++;
			}
			//cout << str << ": " << cur<<endl;
			//cout << "P :";
			//for(int i=0; i<p.size(); i++) cout << " " <<p[i];cout<<endl;
			ans <?= cur;
		} while(next_permutation(p.begin(), p.end()));

		cout << "Case #"<<(c+1)<< ": "<<ans<<endl;

	}

}
