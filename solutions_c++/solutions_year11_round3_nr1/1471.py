#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

#define REP(i,n) for(i=0; i<n; i++)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define REVERSE(c) reverse(ALL(c))
#define INF 1000000000
#define X first
#define Y second
#define pb push_back
#define sz(c) (c).size()

using namespace std;

typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef vector<int> VI;
typedef vector<VI> VVI;


int main()
{
	int T,t;
	ifstream in("input.txt");
	ofstream out("output.txt");	
	in>>T;
	REP(t,T)
	{
		int n,m;
		in>>n>>m;
		vector<string> s(n);
		VVI v(n);
		for(int i=0; i<n; i++)
			in>>s[i];
		for(int i=0; i<n; i++)
			for(int j=0; j<m; j++)
				v[i].push_back(0);
		bool f=true;
		for(int i=0; (i<n); i++)
			for(int j=0; j<m; j++)
				if (s[i][j]=='#')
					v[i][j]=1;

		for(int i=1; (i<n); i++)
		{
			for(int j=0; (j<m-1); j++)
			{
				if (v[i][j] && (s[i-1][j]=='#')&&(s[i-1][j+1]=='#')&&(s[i][j]=='#')&&(s[i][j+1]=='#'))
				{
					v[i-1][j]=0;
					v[i-1][j+1]=0;
					v[i][j]=0;
					v[i][j+1]=0;
					s[i-1][j]='/';
					s[i-1][j+1]='\\';
					s[i][j]='\\';
					s[i][j+1]='/';
				}
			}
		}

		//for(int i=0; (i<n); i++)
		//{
		//	for(int j=0; (j<m); j++)
		//		cout<<v[i][j]<<" ";
		//	cout<<endl;
		//}
		for(int i=0; f&&(i<n); i++)
		{
			for(int j=0; f&&(j<m); j++)
			{
				if (v[i][j]) f=false;
			}
		}
		if (!f) out<<"Case #"<<(t+1)<<":\nImpossible"<<endl;
		else 
		{
			out<<"Case #"<<(t+1)<<":"<<endl;
			for(int i=0; i<n; i++)
				out<<s[i]<<endl;
		}
	}
	return 0;
}

