#include <iostream>
#include <set>
#include <string>

using namespace std;

int n,m;
set<string> ml;

int main(){
	freopen("A-large.in","r",stdin);
	freopen("File Fix-it.out","w",stdout);
	int i,j,k,test,p,tt,ans;
	string s;
	cin>>test;
	for (tt=1;tt<=test;tt++) {
		ml.clear();
		ml.insert("");
		ans=0;
		cin>>n>>m;
		for (i=1;i<=n;i++) {
			cin>>s;
			for (j=0;j<s.length();j++) {
				if (s[j]=='/') {
					ml.insert(s.substr(0,j));
				}
				ml.insert(s);
			}
		};
		for (i=1;i<=m;i++) {
			cin>>s;
			for (j=0;j<s.length();j++) {
				if (s[j]=='/') {
					if (ml.find(s.substr(0,j))==ml.end()) {
						ans++;
						ml.insert(s.substr(0,j));
					}
				}
			}
			if (ml.find(s)==ml.end()) {
				ans++;
				ml.insert(s);
			}
		}
		cout<<"Case #"<<tt<<": "<<ans<<endl;
	}
	return 0;
}