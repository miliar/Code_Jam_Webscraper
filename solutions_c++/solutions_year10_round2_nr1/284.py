#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>
#include <set>
#include <vector>
#include <cmath>
#include <cassert>
#include <cstdlib>
#include <map>

#define y0 y63475625
#define y1 y28435
#define sqr(x) ((x)*(x))

using namespace std;

typedef long long ll;
typedef long double ld;

const double pi = acos(-1.0);

map <string, set <string> > child;

int main()
{
	int T;
	cin >> T;
	for (int I=0;I<T;I++){
		child.clear();
		int n,m;
		cin >> n >> m;
		for (int i=0;i<n;i++){
			string s;
			cin >> s;
			string t="",cur="/";
			if (s[s.size()-1]!='/')s+='/';
			for (int j=1;j<(int)s.size();j++){
				if (s[j]=='/'){
					child[cur].insert(t);
					cur+=t+"/";
					t="";
				} else t+=s[j];
			}
		}
		int ans=0;
		for (int i=0;i<m;i++){
			string s;
			cin >> s;
			string t="",cur="/";
			if (s[s.size()-1]!='/')s+='/';
			for (int j=1;j<(int)s.size();j++){
				if (s[j]=='/'){
					if (child[cur].find(t)==child[cur].end()) {
						ans++;child[cur].insert(t);
					}
					cur+=t+"/";
					t="";
				} else t+=s[j];
			}
		}
		cout << "Case #" << I+1 << ": " << ans << endl;
	}
	return 0;
}
