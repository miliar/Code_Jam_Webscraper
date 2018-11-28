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

string format(int x) {
	ostringstream out;
	out<<x;
	string res=out.str();
	while (sz(res)<4) res='0'+res;
	return res;
}

int ans[570][50];
string s2="welcome to code jam";
string s1;

int solve(int i1, int i2) {
	if (i2==sz(s2)) return 1;
	if (i1==sz(s1)) return 0;
	int &res=ans[i1][i2];
	if (res!=-1) return res;
	res=solve(i1+1,i2);
	if (s1[i1]==s2[i2])
		res+=solve(i1+1,i2+1);
	res%=10000;
	return res;
}

int solve(string s) {
	s1=s;
	memset(ans,-1,sizeof(ans));
	return solve(0,0);
}

int main()
{
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);

	int tn;
	scanf("%d\n",&tn);
	for (int tst=1; tst<=tn; tst++) {
		printf("Case #%d: ",tst);
		char buf[10000];
		gets(buf);
		string str=buf;
		cout<<format(solve(str))<<endl;
	}

	return 0;
}
