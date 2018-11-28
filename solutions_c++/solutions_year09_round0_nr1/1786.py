#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
	int L,D,N,i,j,k,p,flag,ans;
	string str;
	vector <string> dict;
	
	cin >> L >> D >> N;
	
	dict.resize(D);
	for (i=0;i<D;i++) cin >> dict[i];
	for (i=0;i<N;i++) {
		cin >> str;
		ans = 0;
		for (j=0;j<D;j++) {
			for (k=0,p=0;k<L;k++,p++) {
				if (str[p] == '(') {
					flag = 0;
					while (str[++p] != ')') if (str[p] == dict[j][k]) flag = 1;
					if (!flag) break;
				} else {
					if (str[p] != dict[j][k]) break;
				}
			}
			if (k==L) ans++;
		}
		cout << "Case #" << i+1 << ": " << ans << endl;
	}
	
	return 0;
}
