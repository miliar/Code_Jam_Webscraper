#include <algorithm>
#include <bitset>
#include <cctype>
#include <cmath>
#include <cmath>
#include <cstdio>
#include <cstdio>
#include <cstdlib>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
#include <fstream>

#define sz(a) int((a).size())
#define ln(a) int((a).size())
#define pb push_back
#define all(c) (c).begin(),(c).end()
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define rep(i,s,n) for(int i=s; i<n; i++)
#define present(c,x) ((c).find(x) != (c).end())
#define cpresent(c,x) (find(all(c),x) != (c).end())
using namespace std;

char mapping[26];

char decode(char a)
{
	if(a == ' ') return ' ';
	else return mapping[a - 'a'];
}

int main()
{
	freopen("A-small.in","r",stdin);
	freopen("A-small.out","w",stdout);

	ifstream fin("code");
	char e,p;
	for(int i = 0; i < 26; i++)
	{
		fin>>e>>p;
		mapping[i] = p;
	}

	int T;
	cin>>T;
	string temp;
	getline(cin,temp);
	for(int i = 1; i <= T; i++)
	{
		string encodedLine, decodedLine;
		getline(cin, encodedLine);
		for(int j = 0; j < ln(encodedLine); j++)
			decodedLine += decode(encodedLine[j]);
		cout<<"Case #"<<i<<": "<<decodedLine<<endl;
	}
	return 0;
}
