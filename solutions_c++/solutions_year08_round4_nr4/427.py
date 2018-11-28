#define _CRT_SECURE_NO_DEPRECATE

#include <iostream>
#include <sstream>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <cmath>
#include <cstdlib>

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

void writeCaseNumber(int num) { printf("Case #%d: ",num); }

int getSize(string s) {
	int res=1;
	for (int i=1; i<sz(s); i++)
		if (s[i]!=s[i-1]) 
			res++;
	return res;
}

string getCode(string s, vi p) {
	string res(sz(s),' ');
	for (int i=0; i<sz(s); i++) {
		int to=(i/sz(p))*sz(p)+p[i%sz(p)];
		res[to]=s[i];
	}
	return res;
}

int main()
{
	freopen("d.in","r",stdin);
	freopen("d.out","w",stdout);

	int tn;
	cin>>tn;
	
	for (int tst=0; tst<tn; tst++) {
		writeCaseNumber(tst+1);
		int k;
		string s;
		cin>>k>>s;
		vi p(k);
		for (int i=0; i<k; i++) p[i]=i;
		int res=1<<30;
		do {
			res=min(res,getSize(getCode(s,p)));
		} while (next_permutation(all(p)));
		cout<<res<<endl;
	}

	return 0;
}
