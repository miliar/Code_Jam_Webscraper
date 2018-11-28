#include <algorithm>
#include <numeric>
#include <string>
#include <string.h>
#include <map>
#include <set>
#include <vector>
#include <queue>
#include <iostream>
#include <fstream>
#include <cmath>
#include <math.h>
#include <iomanip>
#include <locale>

using namespace std;

#define FOR(i,n) for (int i=0; i<n; ++i)
#define FORE(i,n) for (int i=0; i<=n; ++i)
#define REP(i,a,b) for (int i=a; i<b; ++i)
#define REPE(i,a,b) for (int i=a; i<=b; ++i)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))


typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef long long int LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
const double pi = acos(-1.0);
const int inf =(int) 1e9;


int main()
{
	freopen("A-small-attempt0.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int t;
	scanf("%d",&t);
	cin.get();
	string s;
	getline(cin,s,'\n');
	s+=13;
	string z="yhesocvxduiglbkrztnwjpfmaq";
	cout<<"Case #1: ";
	int k=2;
	FOR(j,s.size()-1)
	{
		if (s[j]==13)
		{
			cout<<endl<<"Case #"<<k<<": ";
			++k;
			continue;
		}
		if (s[j]!=' ')
			cout<<z[s[j]-97];
		else
			cout<<" ";
	}
	return 0;
}