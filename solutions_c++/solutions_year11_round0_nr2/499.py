#include<iostream>
#include<vector>
#include<queue>
#include<set>
#include<cstdio>
#include<algorithm>
#include<string>
#include<map>
#include<cmath>
#include<cstdlib>
#include<ctime>
using namespace std;

int a[255][255];
int b[255][255];

string del(string a,int l,int r) {
	string res="";
	if (l>0) res+=a.substr(0,l);
	if (r!=a.length()-1) res+=a.substr(r+1,a.length()-r-1);
	return res;
}

string p(string a) {
	if (a.length()==0) return "[]";
	string ret="[";
	for (int i=0;i<a.length();i++) {
		ret+=a[i];
		if (i!=a.length()-1)
			ret+=", ";
	}
	ret+="]";
	return ret;
}

int main() {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int t; cin >> t;
	for (int k=0;k<t;k++) {
		memset(a,0,sizeof(a));
		memset(b,0,sizeof(b));
		int c; cin >> c; string str;
		for (int i=0;i<c;i++) {
			cin >> str;
			a[str[0]][str[1]]=str[2];
			a[str[1]][str[0]]=str[2];
		}
		int d; cin >> d;
		for (int i=0;i<d;i++) {
			cin >> str;
			b[str[0]][str[1]]=-1;
			b[str[1]][str[0]]=-1;
		}
		string ret="";
		int n; cin >> n;
		for (int i=0;i<n;i++) {
			char c; cin >> c;
			ret+=c;
			int len=ret.length();
			if (len>1) {
				if (a[ret[len-1]][ret[len-2]]>0) {
					char add=(char)a[ret[len-1]][ret[len-2]];
					ret.pop_back();
					ret.pop_back();
					ret+=add;
				} else {
					for (int i=len-2;i>=0;i--) {
						if (b[ret[i]][ret[len-1]]==-1) {
							ret="";
							break;
						}
					}
				}
			}
		}
		printf("Case #%d: %s\n",k+1,p(ret).c_str());
	}
	return 0;
}
