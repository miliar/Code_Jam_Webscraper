#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <list>
#include <cmath>
#include <iterator>
#include <algorithm>
#include <numeric>
#include <sstream>
#include <stack>
#include <cstdio>
#include <cstdlib>
#include <cctype>

using namespace std;

#define all(a) (a).begin(), (a).end()
#define rall(a) (a).rbegin(), (a).rend()
#define mp make_pair
#define pb push_back

void prepare()
{
#ifdef _DEBUG
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
#endif
}

void solve()
{
	string cod = "ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjv";
	string dec = "ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveup";
	map<char,char> decode;
	for (int i=0; i<cod.size(); ++i)
	{
		decode[cod[i]]=dec[i];
	}
	decode['z']='q';
	decode['q']='z';
	decode[' ']=' ';
	int n;
	cin>>n;
	string s;
	getline(cin,s);
	for (int test=1;test<=n;++test)
	{
		cout<<"Case #"<<test<<": ";
		getline(cin,s);
		for (int i=0;i<s.size(); ++i)
		{
			s[i]=decode[s[i]];
		}
		cout<<s;
		cout<<endl;
	}
}

int main()
{
	prepare();
	solve();
	return 0;
}