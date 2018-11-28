#include <iostream>
#include <map>
#include <string>
using namespace std;

const int inf = 1000000;

const int maxq = 1020;
const int maxs = 105;

int b[maxq];
int s,q;

int proc() {
	int c = 0;
	bool d[maxs];
	memset(d,0,sizeof(d));
	int dc = 0;
	for(int i=0;i<q;i++) {
		if(!d[ b[i] ]) {
			d[b[i]] = true;
			dc++;
			if(dc>=s) {
				// incr
				c++;
				// clear
				memset(d,0,sizeof(d));
				dc = 0;
				d[b[i]] = true;
				dc = 1;
			}
		}
	}
	return c;
}

int main() {
	int n;
	cin>>n;
	for(int i=0;i<n;i++) {
		cin>>s;
		cin.ignore();
		map<string, int> mp;
		for(int j=0;j<s;j++) {
			string a;
			getline(cin, a);
//			cerr<<" [DEBUG]"<<a<<endl;
			mp[a] = j;
		}
		cin>>q;
		cin.ignore();
		for(int j=0;j<q;j++) {
			string a;
			getline(cin, a);
//			cerr<<" [DEBUG]"<<a<<endl;
			b[j] = mp[a];
		}

		cout<<"Case #"<<i+1<<": "<<proc()<<endl;
	}

	return 0;
}

