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

		int tab[1003][1002];

int main()
{
	int N;
	cin >> N;
	for(int iii=0;iii<N;iii++)
	{
		int S,Q;
		cin >> S;
		map<string, int> dane;
		string zz;
			getline(cin, zz);//dummy
		for(int i=0;i<S;i++)
		{
			getline(cin, zz);
			dane[zz]=i;
		}
		cin >> Q;
			getline(cin, zz);//DUMMY
		for(int i=0;i<Q+1;i++)
			for(int j=0;j<S;j++)
				tab[i][j]=-1;
		for(int j=0;j<S;j++)
			tab[0][j]=0;

		string query;
		for(int i=0;i<Q;i++)
		{
			getline(cin, query);
			int co=dane[query];
			for(int j=0;j<S;j++)
				if(dane[query]!=j)
				{
					if(tab[i][j]!=-1)
						tab[i+1][j]=tab[i][j];
					else
					{
						int m=10000000;
						for(int k=0;k<S;k++)
							if(tab[i][k]!= -1 && tab[i][k]<m)
								m=tab[i][k];
						tab[i+1][j]=m+1;
					}
				}
		}

		int ret=100000000;
						for(int k=0;k<S;k++)
							if(tab[Q][k]!= -1 && tab[Q][k]<ret)
								ret=tab[Q][k];


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
