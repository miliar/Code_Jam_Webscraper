#include <iostream>
#include <vector>
using namespace std;

int main() {
	int t,p,k,l;
	int i,j,let,test = 1;
	long long int min;
	vector<int> f;
	cin >> t;
	while(t--) {
		f.clear();
		cin >> p >> k >> l;
		for(i=0;i<l;i++) {
			cin >> j;
			f.push_back(j);
		}
		sort(f.begin(),f.end());
		i=l-1;
		min = 0; let=1;
		if(i>p*k) {
			cout << "Case #" << (test++) << ": " << "impossible" << endl;
			continue;
		}
		for(let=1;let<=p;let++) {
			for(j=0;j<k;j++) {
				min+=f[i]*let;
				i--;
				if(i<0)
					break;
			}
			if(i<0)
				break;
		}
		cout << "Case #" << (test++) << ": " << min << endl;
	}
}
