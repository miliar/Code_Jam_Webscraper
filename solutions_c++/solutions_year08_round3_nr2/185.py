#include <iostream>
using namespace std;

long long int count2;
string a;

bool ugly(long long int x) {
	if(x%2==0 || x%3==0 || x%5==0 || x%7==0 || x==0)
		return true;
	return false;
}

void rec(int pos, bool pv, long long int val, long long int last) {
	char ch;
	if(pos==a.size()) {
		val = pv?(val+last):(val-last);
		if(ugly(val))
			count2++;
		return;
	}
	long long int i,val2;
	ch = a[pos];
	for(i=0;i<3;i++) {
		switch(i) {
			case 0:
				rec(pos+1,pv,val,last*10 + (ch-'0'));
				break;
			case 1:
				val2 = pv?(val+last):(val-last);
				rec(pos+1,pv,val2,(ch-'0'));
				break;
			case 2:
				val2 = pv?(val+last):(val-last);
				rec(pos+1,!pv,val2,(ch-'0'));
				break;
		}
	}
}

int main() {
	int t, test=1;
	cin >> t;
	char ch;
	while(t--) {
		cin >> a;
		count2 = 0;
		ch = a[0];
		rec(1,true,0,a[0]-'0');
		cout << "Case #" << (test++) << ": " << count2 << endl;
	}
	return 0;
}
