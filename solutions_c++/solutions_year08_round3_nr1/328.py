#include <algorithm>
#include <vector>
//#include <queue>
//#include <stack>
//#include <map>
//#include <set> 
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
		int tab[2001];


int main()
{
	int N;
	cin >> N;
	for(int iii=0;iii<N;iii++)
	{
		int P, K, L;
		cin >> P >> K >> L;
		//	getline(cin, zz);
		for(int i=0;i<L;i++)
			cin >> tab[i];
		
		sort(tab, tab+L);

		int ret=0;
		bool flag=false;
		for(int el=L-1, sk=0,rep=1;el>=0;el--)
		{
			if(rep==P+1)
			{
				flag=true;
				break;
			}
			ret += rep*tab[el];
			sk++;
			if(sk==K)
			{
				sk=0;
				rep++;
			}
		}
		if(flag==true)
		{
			cout << "Case #" << iii+1 <<": " << "Impossible" << endl;
		}
		else
			cout << "Case #" << iii+1 <<": " << ret << endl;
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
