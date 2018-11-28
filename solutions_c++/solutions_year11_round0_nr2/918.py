#include <iostream>

using namespace std;

int main (int argc, char const *argv[])
{
	int t;
	cin >> t;
	for(int index = 1; index <= t; index++) {
		int c;
		int d;
		int n;
		char tmp[5];
		int invoke[26][26];
		for(int i = 0; i < 26; i++) {
			for(int j = 0; j < 26; j++) {
				invoke[i][j] = -1;
			}
		}
		int oppose[26][26]={0};
		char data[101];
		cin >> c;
		for(int i = 0; i < c; i++) {
			cin >> tmp;
			invoke[tmp[0]-'A'][tmp[1]-'A']=tmp[2]-'A';
			invoke[tmp[1]-'A'][tmp[0]-'A']=tmp[2]-'A';
		}
		cin >> d;
		for(int i = 0; i < d; i++) {
			cin >> tmp;
			oppose[tmp[0]-'A'][tmp[1]-'A']=1;
			oppose[tmp[1]-'A'][tmp[0]-'A']=1;
		}
		cin >> n;
		cin >> data;
		char ans[101];
		int count = 1;
		ans[0] = data[0];
		for(int i = 1; i < n; i++) {
			ans[count] = data[i];
			count++;
			while (count > 1) {
				if (invoke[ans[count-1]-'A'][ans[count-2]-'A']!=-1) {
					ans[count-2] = invoke[ans[count-1]-'A'][ans[count-2]-'A']+'A';
					count--;
				} else {
					break;
				}
			}
			for(int j = 0; j < count-1; j++) {
				if (oppose[ans[j]-'A'][ans[count-1]-'A']) {
					count = 0;
					break;
				}
			}
		}
		cout << "Case #" << index << ": [";
		if (count > 0) {
			cout << ans[0];
		}
		for(int i = 1; i < count; i++) {
			cout << ", " << ans[i];
		}
		cout << "]" << endl;
	}
	return 0;
}