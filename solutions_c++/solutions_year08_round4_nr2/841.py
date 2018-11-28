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


int main()
{
	int C;
	cin >> C;
	for(int iii=0;iii<C;iii++)
	{
		int N, MM, A;
		cin >> N >> MM >> A;
		//	getline(cin, zz);
		//for(int i=0;i<L;i++)
		//	cin >> tab[i];
		bool stop=false;
		for(int i=0; stop==false && i<=N;i++)
		for(int j=0;stop==false && j<=MM;j++)
		for(int k=0;stop==false && k<=N;k++)
		for(int m=0;stop==false && m<=MM;m++)
		{
			int kw=max(j, m) * max(i,k) * 2;
			if((k-i) * (m-j) < 0)
			{
					kw = kw - j*i - m*k - abs((i-k)*(j-m));
			}
			else
			{
				if(m>j)
					kw = kw-m*k - i*j - 2*abs(k-i)*j - abs(k-i)*abs(m-j);
				else
					kw = kw-m*k - i*j - 2*abs(k-i)*m - abs(k-i)*abs(m-j);
			}
			if(kw==A)
			{
				stop=true;
				cout << "Case #" << iii+1 <<": 0 0 " << i << " " << j << " " << k << " " << m << endl;
			}
		}
		if(stop==false)
				cout << "Case #" << iii+1 <<": IMPOSSIBLE" << endl;
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
