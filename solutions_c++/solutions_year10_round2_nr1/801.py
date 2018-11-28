#include <iostream>
#include <fstream>
#include <set>
#include <string>

using namespace std;
set<string> dir;
int n, m;
int tot;

void insert(string s) {
	string sub;
	for (int i=1; i<(int)s.length(); i++)
		if (s[i]=='/' || i==(int)s.length()-1) {
			if (s[i]=='/')
				sub = s.substr(0,i);
			else sub = s.substr(0,i+1);
			if (dir.find(sub)==dir.end()) {
				tot++;
				dir.insert(sub);
//				cout<<sub<<endl;
			}
		}			
}
void init()
{
	string s;
	dir.clear();
	cin>>n>>m;
	tot = 0;
	for (int i=0; i<n; i++) {
		cin>>s;
		insert(s);
	}
}
int calc()
{
	string s;
	tot = 0;
	for (int i=0; i<m; i++) {
		cin>>s;
		insert(s);
	}
	return tot;
}
int main()
{
	int t;
	cin>>t;
	for (int i=1; i<=t; i++) {	
		init();
		printf("Case #%d: %d\n",i,calc());
	}
	return 0;
}
