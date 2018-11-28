#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <math.h>
#include <queue>
#include <sstream>
using namespace std;
int t;
string i2s(int x){
	stringstream ss;
	ss << x;
	return ss.str();
}
int s2i(string str){
	stringstream ss (str);
	int res;
	ss>>res;
	return res;
}
int main() {
	//	freopen("hz.in","r",stdin);
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	cin >> t;
	int n,m;
	string s,hz;
	for (int c=0;c<t;c++) {
		set <string> dir;
		cin >> n >> m; int res=0;
		for (int i=0;i<n;i++) {
			cin >> s;
			for (int i=1;i<=s.length();i++)
				if (s[i]=='/' || s[i]==0) {
					hz=s.substr(0,i);
					if (hz!="") dir.insert(s.substr(0,i));
				}
		}

		for (int i=0;i<m;i++) {
			cin >> s;
			for (int i=1;i<=s.length();i++)
				if (s[i]=='/' || s[i]==0) { 
					hz=s.substr(0,i);
					if (hz!="")
					if (dir.find(hz)==dir.end()) {
						dir.insert(hz);
						res++;
					}
				}
		}

		cout << "Case #" << c+1 << ": ";
		cout << res;
		cout << endl;
	}
}