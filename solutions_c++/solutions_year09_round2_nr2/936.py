#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main() {
	int T,t,i,j;
	string nr;
	cin>>T;
	for (t=1; t<=T; t++) {
		cin>>nr;
		if (!next_permutation(nr.begin(), nr.end())) {
			nr="0"+nr;
			i=0;
			while (nr[i]=='0') {
				i++;
			}
			nr[0]=nr[i];
			nr[i]='0';
		}
		cout<<"Case #"<<t<<": "<<nr<<endl;
	}
	return 0;
}
