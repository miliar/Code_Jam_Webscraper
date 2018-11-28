#define _CRT_SECURE_NO_DEPRECATE
#pragma comment (linker,"/STACK:64000000")

#include <iostream>
#include <cstdio>
#include <sstream>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>

using namespace std;

#define sz(v) ((int)(v).size())
#define all(v) v.begin(), v.end()
#define pb push_back
#define mp make_pair

typedef long long ll;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<string> vs;

template<class T>T abs(T x) { return (x>0) ? x : -x; }
template<class T>T sqr(T x) { return x*x;            }

int len,nstr,npat;
string str[5218];

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);

	cin>>len>>nstr>>npat;
	for (int i=0; i<nstr; i++)
		cin>>str[i];
	for (int p=0; p<npat; p++) {
		printf("Case #%d: ",p+1);
		string pat;
		cin>>pat;
		int depth=0;
		vector<set<char> > v;
		set<char> cur;
		for (int i=0; i<sz(pat); i++) {
			if (pat[i]=='(') depth++;
			if (pat[i]==')') depth--;
			if (isalpha(pat[i]))
				cur.insert(pat[i]);
			if (depth==0) {
				v.pb(cur);
				cur.clear();
			}
		}
		assert(sz(v)==len);
		int res=0;
		for (int s=0; s<nstr; s++) {
			bool ok=true;
			for (int i=0; i<len; i++)
				ok&=v[i].count(str[s][i]);
			if (ok) res++;
		}
		cout<<res<<endl;
	}

	return 0;
}
