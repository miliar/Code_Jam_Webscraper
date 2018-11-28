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
#include <fstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cctype>
using namespace std;

#define REP(i,n) for(int _n=n, i=0;i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define in(x,s) (s.find(x)!=s.end())

typedef long long int64;
typedef vector<int> VI;
typedef vector<string> VS;

const double eps = 1E-12;
const double pi=acos(-1.0); 


ifstream fin("a.in");
ofstream fout("a.out");

int N;

int win[120][120];
int games[120];
int w[120];
double wp[120];
double owp[120];
double oowp[120];
double res[120];
int main()
{
	fin>>N;
	for(int c=0;c<N;c++)
	{
		int T;
		fin>>T;
		memset(win,0,sizeof(win));
		memset(w,0,sizeof(w));
		memset(games,0,sizeof(w));
		for(int i=0;i<120;i++)
		{
			wp[i] = owp[i] = oowp[i] = 0.0;
			res[i] = 0.0;
		}
		for(int i=0;i<T;i++)
			for(int j=0;j<T;j++)
			{
				char ch;
				fin>>ch;
				if(ch=='1')
				{
					win[i][j] = 2;
					games[i]++;
					w[i]++;
				}
				else if(ch=='0')
				{
					games[i]++;
					win[i][j] = 1;
				}

			}
		for(int i=0;i<T;i++)
		{
			wp[i] = (double)w[i]/games[i];
			
		}
		for(int i=0;i<T;i++)
		{		
			double tmp = 0.0;
			for(int j=0;j<T;j++)
			{
				if(win[i][j] !=0)
				{
					int tw = w[j];
					int tg = games[j]-1;
					if(win[i][j]==1)
					{
						tw--;
					}
					tmp += (double)tw/tg;
				}
			}
			owp[i] = tmp/games[i];
		}
		for(int i=0;i<T;i++)
		{		
			double tmp = 0.0;
			for(int j=0;j<T;j++)
			{
				if(win[i][j] !=0)
					tmp += owp[j];
			}
			oowp[i] = tmp/games[i];
		}
		
		cout<<"Case #"<<c+1<<":"<<endl;
		fout<<"Case #"<<c+1<<":"<<endl;
		for(int i=0;i<T;i++)
		{
			res[i] = 0.25 * wp[i] + 0.5 *owp[i] + 0.25*oowp[i];
			cout<<res[i]<<endl;
			fout<<res[i]<<endl;
			
		}



	

		
	

	
	}
	return 0;
}
