#pragma comment(linker,"/STACK:64000000")
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <cmath>
#include <map>
#include <set>
#include <ctime>
#include <algorithm>
#include <memory.h>

using namespace std;

#define WR printf
#define RE scanf
#define PB push_back
#define SE second
#define FI first

#define FOR(i,k,n) for(int i=(k); i<=(n); i++)
#define DFOR(i,k,n) for(int i=(k); i>=(n); i--)
#define SZ(a) (int)((a).size())
#define FA(i,v) FOR(i,0,SZ(v)-1)
#define RFA(i,v) DFOR(i,SZ(v)-1,0)
#define CLR(a) memset(a, 0, sizeof(a))

#define LL long long
#define VI  vector<int>
#define PAR pair<int ,int>
#define o_O 1000000000 
void __never(int a){printf("\nOPS %d", a);}
#define ass(s) {if (!(s)) {__never(__LINE__);cout.flush();cerr.flush();abort();}}

map< string, char > combine;
set< string > opposed;
int n;
string S;

void sol()
{
	string re;
	FA(a,S)
	{
		re.push_back(S[a]);
		while (SZ(re)>1)
		{
			string tmp;
			tmp.push_back(re[SZ(re)-1]);
			tmp.push_back(re[SZ(re)-2]);
			if (combine.find(tmp) != combine.end())
			{
				re.resize(SZ(re)-2);
				re.push_back(combine[tmp]);
			}
			else break;
		}

		FOR(b,0,SZ(re)-2)
		{
			string tmp;
			tmp.push_back(re[b]);
			tmp.push_back(re[SZ(re)-1]);
			if (opposed.find(tmp) != opposed.end())
			{
				re.clear();
				break;
			}
		}
	}

	cout << "[";
	FA(a,re)
	{
		cout << re[a];
		if (a==SZ(re)-1) cout << "]"; else cout << ", ";
	}
	if (SZ(re)==0) cout << "]";
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	cin >> T;
	FOR(t,1,T)
	{
		int x;
		string str;

		combine.clear();
		opposed.clear();

		cin >> x;
		FOR(a,1,x)
		{
			cin >> str;
			string s1, s2;
			s1.push_back(str[0]);
			s1.push_back(str[1]);
			s2.push_back(str[1]);
			s2.push_back(str[0]);
			combine[s1]=str[2];
			combine[s2]=str[2];
		}

		cin >> x;
		FOR(a,1,x)
		{
			cin >> str;
			opposed.insert(str);
			swap(str[0], str[1]);
			opposed.insert(str);
		}

		cin >> n;
		cin >> S;

		cout << "Case #" << t << ": ";
		sol();
		cout << "\n";
	}

	return 0;
}