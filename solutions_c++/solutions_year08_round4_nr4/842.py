#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <fstream>

using namespace std;

int main() {
	freopen("D-small.in","rt",stdin);
	freopen("D-small.out", "wt", stdout);
	int N,k;
	cin>>N;
	string str;
	for(int i = 1; i <= N; i++) {
		cin>>k;
		cin>>str;
		vector<int> pem(k);
		for(int j = 0; j < k; j++) {
			pem[j] = j;
		}
		int res = (int)str.size();
		do {
			string temp = str;
			for(int j = 0; j < (int)temp.size(); j += k) {
				for(int q = j; q < j + k;q++) {
					temp[q] = str[j+pem[q-j]]; 
				}
			}
			int cnt = 1;
			char cur = temp[0];
			for(int j = 1; j < (int)temp.size(); j++) {
				if(temp[j] != cur) {
					cnt ++;
					cur = temp[j];
				}
			}
			if(cnt < res ) res = cnt;
		}while(next_permutation (pem.begin(),pem.end()));
		cout<<"Case #"<<i<<": "<<res<<endl;
	}
	return 0;
}