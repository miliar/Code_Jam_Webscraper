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
#include <cassert>
#include <queue>
using namespace std;

#define REP(i,n) for(int _n=n, i=0;i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define in(x,s) (s.find(x)!=s.end())

typedef long long int64;
typedef vector<int> VI;
typedef vector<string> VS;

const double eps = 1E-12;
const double pi=acos(-1.0); 


ifstream fin("c.in");
ofstream fout("c.out");

int T;
int R,C;

char m[100][100];
bool reach[100][100];
bool flip[100][100];
int main()
{
	
	fin>>T;
	for(int c=1;c<=T;c++)
	{		
		fin>>R>>C;
		for(int i=0;i<R;i++)
			for(int j=0;j<C;j++)
			{
				fin>>m[i][j];
			}

		int res = 0;
		int N= 1<<(R*C);
		for(int p=0;p<N;p++)
		{
			for(int i=0;i<R;i++)
				for(int j=0;j<C;j++)
				{
					int x = (1<<(i*C+j)) & p;
					if(x>0)
						flip[i][j] = true;
					else
						flip[i][j] = false;
				}
			memset(reach,false,sizeof(reach));
			bool bad = false;
			for(int i=0;i<R;i++)
				for(int j=0;j<C;j++)
				{
					int ti=i;
					int tj=j;
					if(m[i][j] == '-')
					{
						if(flip[i][j]) tj=(tj+C-1)%C;
						else tj = (tj+1)%C;
					}
					else if(m[i][j] == '|')
					{
						if(flip[i][j]) ti=(ti+R-1)%R;
						else ti = (ti+1)%R;
					}
					else if(m[i][j] == '/')
					{
						if(flip[i][j])  {tj=(tj+C-1)%C; ti=(ti+1)%R;}
						else { tj = (tj+1)%C; ti = (ti+R-1)%R;}
					}
					else if(m[i][j] == '\\')
					{
						if(flip[i][j]) {tj=(tj+C-1)%C; ti=(ti+R-1)%R;}
						else {tj = (tj+1)%C;ti = (ti+1)%R;}
					}
					if(reach[ti][tj])
					{
						bad = true;
						break;
					}
					reach[ti][tj] = true;

				}
			if(!bad)
				res ++;
		}
		

		


		cout<<"Case #"<<c<<": "<<res<<endl;
		fout<<"Case #"<<c<<": "<<res<<endl;
		
	}
	return 0;
}
