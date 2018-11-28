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
	int N;
	cin >> N;
	for(int iii=0;iii<N;iii++)
	{
		int n,m,X,Y,Z;
		cin >> n >> m >> X >> Y >> Z;
		vector<long long int> signs(1002,0);
		vector<int> ile(1002,1);
		vector<long long int> A(102,0);
		for(int i=0;i<m;i++)
			cin >> A[i];
		for(int i=0;i<n;i++)
		{
			signs[i]=A[i%m];
			A[i%m]=(X * A[i % m] + (long long)Y * (long long)(i + 1)) % Z;
		}
		//for(int i=0;i<n;i++)
		//	cerr << signs[i] << " ";
		//cerr << endl;
		for(int i=0;i<n;i++)
		{
			for(int j=i+1;j<n;j++)
				if(signs[j]>signs[i])
				{
					ile[j]+=ile[i];
					if(ile[j]>=1000000007)
						ile[j]%=1000000007;
				}
		}
		int ret=0;
		for(int i=0;i<n;i++)
		{
			ret+=ile[i];
			if(ret>=1000000007)
				ret%=1000000007;
		
		}
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
