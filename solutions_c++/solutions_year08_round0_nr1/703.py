#include <iostream>
#include <map>
#include <string>
#include <vector>

using namespace std;

int n,s,q;
map<string,int> se;
bool used[101];
int cnt,switches;

int main() {
	cin >> n;
	for(int i=1;i<=n;i++) {
		se.clear();
		cnt = 0;
		switches = 0;
		cin >> s;
		for(int k=0;k<s;k++)
			used[k] = false;
		cin.ignore();
		for(int k=0;k<s;k++)  {
			string temp;
			getline(cin,temp);
			se[temp] = k;
		}
		cin >> q;
		cin.ignore();
		for(int k=0;k<q;k++) {
			string temp;
			getline(cin,temp);
			if (used[se[temp]]==false) {
				if (cnt==(s-1)) {
					switches++;
					cnt = 1;
					for(int j=0;j<s;j++) used[j] = false;
					used[se[temp]] = true;
				} else {
					cnt++;
					used[se[temp]] = true;
				}
			}
		}
		cout << "Case #" << i << ": " << switches << endl;
	}
	return 0;
}
