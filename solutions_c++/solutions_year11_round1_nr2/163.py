#include<iostream>
#include<vector>
#include<map>
#include<fstream>
#include<string>
#include<math.h>
#include<queue>
#include<stack>
#include<sstream>
#include<algorithm>
#include<set>
#include<stdio.h>
#include<stdlib.h>

#define vint vector <int>
#define vstring vector <string>
#define np(a) next_permutation(a.begin(),a.end())
#define ff(i,n) for (i=0; i<n; i++)
#define pb(a,b) a.push_back(b)
#define mkp make_pair
#define all(a) a.begin() , a.end()

using namespace std;
typedef __int64 ll;
stringstream ss;

vector <string> s , ts;
string ins[11111];
string ans[11111] , p;
int n , m;
bool b[27];

bool ok(string a , string b , char c) {
	int len=a.length() , i;
	for (i=0; i<len; i++) if (((a[i]==c)&&(b[i]!=c))||((a[i]!=c)&&(b[i]==c))) return false;
	return true;
}

bool contan(string s , char c) {
	int i , len=s.length();
	for (i=0; i<len; i++) if (s[i]==c) return true;
	return false;
}

string find() {
	int i , j , k , best=-1 , tmp , len , tol , pp;
	string res , ff;
	char ch;
	for (i=1; i<=n; i++) {
		pp=0;
		len=ins[i].length();
		s.clear();
		ts.clear();
		for (j=1; j<=n; j++) if (len==ins[j].length()) pb(s,ins[j]);
		tmp=0;
		while (1) {
			memset(b,false,sizeof(b));
			tol=s.size();
			if (tol==1) break;
			for (j=0; j<tol; j++) 
				for (k=0; k<s[j].length(); k++) b[s[j][k]-'a']=true;		
			while (!b[p[pp]-'a']) pp++;
			ts.clear();
			if (contan(ins[i],p[pp])) {
				for (j=0; j<tol; j++) if (ok(ins[i],s[j],p[pp])) 
					pb(ts,s[j]);
			}
			else {
				for (j=0; j<tol; j++) if (!contan(s[j],p[pp])) 
					pb(ts,s[j]);
				tmp++;
			}
			s.clear();
			for (j=0; j<ts.size(); j++) pb(s,ts[j]);			
			pp++;
		}
		if (tmp>best) {
			best=tmp;
			res=ins[i];
		}
	}
	return res;
}

int main() {
	freopen("in.txt" , "r" , stdin);
	freopen("b.txt" , "w" , stdout);
	int i , j , k , tt , ttt;
	cin >> ttt;
	for (tt=1; tt<=ttt; tt++) {
		cin >> n >> m;
		for (i=1; i<=n; i++) cin >> ins[i];
		for (i=1; i<=m; i++) {
			cin >> p;
			ans[i]=find();
		}
		printf("Case #%d:" , tt);
		for (i=1; i<=m; i++) cout << " " << ans[i];
		cout << endl;
	}
	return 0;
}