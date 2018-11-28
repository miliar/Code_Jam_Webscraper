#include <iostream>
#define _USE_MATH_DEFINES
#include <cmath>
#include <vector>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <list>
#include <stack>
#include <queue>
#include <sstream>
#include <cstdio>
#include <cstdlib>

using namespace std;
#define forn(i,n) for (int i=0;i<n;++i)
#define all(a) a.begin(),a.end()
#define and 1


void solve(){
	int n;
	cin >> n;
	string s;
	cin >> s;
	vector<int> per(n);
	forn(i,n)per[i]=i;
	int ans=1000000000;
	do {
		string s1="";
		for (int i=0;i<s.length();i+=n){
			string ss="";
			forn(j,n)ss+=" ";
			forn(j,n)ss[j]=s[i+per[j]];
			s1+=ss;
		}
		int cur=0;
		forn(i,s1.length())if (i&&s1[i]!=s1[i-1])cur++;
		ans=min(ans,cur+1);

	}while (next_permutation(per.begin(),per.end()));
	cout << ans << endl;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int n;
	cin >> n;
	forn(i,n){
		cout << "Case #" << i+1 << ": ";
		solve();
	}

	return 0;
}