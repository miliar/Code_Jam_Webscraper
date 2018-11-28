#include <algorithm>
#include <vector>
//#include <queue>
//#include <stack>
#include <map>
#include <set> 
//#include <sstream>
#include <iostream>
#include <string>
//#include <cstdio>
#include <cmath>
//#include <cstdlib>
//#include <iomanip>
using namespace std;

#define FOR(i,a,b) for(typeof(a) i=(a), _b=(b); i < _b; i++)
#define FORD(i,a,b) for(typeof(a) i=(a)-1, _b=(b); i >= _b; i--)
#define S(x) ((int)((x).size()))
#define PB(x) push_back(x)
#define DEBUG(x) cerr << #x << " : " << (x) << endl
typedef long long LL;
typedef vector<int> VI;
typedef vector<string> VS;
typedef pair<int, int> PII;
ostream& operator<<(ostream& s, PII para)
{	s << para.first << " " << para.second; 	return s;	}
vector<string> tokenize(string text, string delim);
template<class T> inline T sqr(T x){return x*x;}

struct classcompX {
  bool operator() (const pair<int,int>& x, const pair<int,int>& y) const
  {
	  if(x.first>y.first) return true;
      return false;
  }
} paraX;
struct classcompY {
  bool operator() (const pair<int,int>& x, const pair<int,int>& y) const
  {
	  if(x.second>y.second) return true;
      return false;
  }
} paraY;


int main()
{
	int N;
	cin >> N;
	for(int iii=0;iii<N;iii++)
	{
		int T, NA, NB, h,m;
		char dummy;
		int ret=0;
		cin >> T >> NA >> NB;
		//vector<pair<int,int>> a(NA);
		//vector<pair<int,int>> b(NB);
		vector<int> aOUT(NA);
		vector<int> aIN(NB);
		vector<int> bOUT(NB);
		vector<int> bIN(NA);

		for(int i=0;i<NA;i++)
		{
			cin >> h >> dummy >> m;
			aOUT[i] =m+h*60;
			cin >> h >> dummy >> m;
			bIN[i]=m+h*60+T;
		}
		for(int i=0;i<NB;i++)
		{
			cin >> h >> dummy >> m;
			bOUT[i]=m+h*60;
			cin >> h >> dummy >> m;
			aIN[i]=m+h*60+T;
		}
		sort(aOUT.begin(), aOUT.end());
		sort(aIN.begin(), aIN.end());
		sort(bOUT.begin(), bOUT.end());
		sort(bIN.begin(), bIN.end());
		
		int ret1=0,ret2=0;
		int o=0,i=0;
		int akt=0;
		while(o<NA)
		{
			while(i<NB && aIN[i]<=aOUT[o])
			{
				akt--;
				i++;
			}
			akt++;
			o++;
			ret1=max(ret1,akt);
		}
		akt=0;
		o=0;
		i=0;
		while(o<NB)
		{
			while(i<NA && bIN[i]<=bOUT[o])
			{
				akt--;
				i++;
			}
			akt++;
			o++;
			ret2=max(ret2,akt);
		}

		cout << "Case #" << iii+1 <<": " << ret1 << " " << ret2 << endl;
	}
}

vector<string> tokenize(string text, string delim)
{
	vector<string> wyniki;
	string::size_type last = text.find_first_not_of(delim, 0);
	string::size_type pos = text.find_first_of(delim, last);

	while (pos != string::npos || last != string::npos)
	{
		wyniki.push_back(text.substr(last, pos - last));
		last = text.find_first_not_of(delim, pos);
		pos = text.find_first_of(delim, last);
	}
	return wyniki;
}
