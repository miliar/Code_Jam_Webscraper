
#define _CRT_SECURE_NO_DEPRECATE
#include <iostream> 
#include <string>
#include <vector>
#include <sstream>
#include <queue>
#include <algorithm>
#include <iomanip>
#include <map>
#include <set>
#include <math.h>
#include <stack>
#include <deque>
#include <numeric>
#define all(x) x.begin(),x.end()
#define mpair make_pair
using namespace std;
typedef long long ll;
typedef long double ld;
const ld epsylon = 1e-9;
int n,m;
inline int code(int x,int y)
{
	return x*m + y;
}
inline void decode(int code,int &x,int &y)
{
	x = code / m;
	y = code % m;
}
template<class T >
string to_s(const vector<T>& a,char delim = ' ')
{
	ostringstream out;
	for(int i=0;i<(int)a.size();i++)
	{
		out<<a[i];
		if(i!= (int)a.size()-1)
			out<<delim;
	}
	return out.str();
}
int move[4][2] = {{-1,0},{0,-1},{0,1},{1,0}};
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int nt;
	cin>>nt;
	for(int it=1;it<=nt;it++)
	{
		cin>>n>>m;
		vector<vector<int> > a(n);
		for(int i=0;i<n;i++)
			a[i].resize(m);
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<m;j++)
			{
				cin>>a[i][j];
			}
		}
		vector<vector<int> > ne(n*m);
		for(int i=0;i<n; i++)
		{
			for(int j=0;j<m;j++)
			{
				int best = a[i][j];
				int bi = -1;
				for(int l=0;l<4;l++)
				{
					int tx = i + move[l][0];
					int ty = j + move[l][1];
					if(tx >= 0 && ty >= 0 && tx < n && ty < m)
					{
						if(a[tx][ty] < best)
						{
							best = a[tx][ty];
							bi = code(tx,ty);
						}
					}
				}
				if(bi >= 0)
				{
					int index = code(i,j);
					ne[index].push_back(bi);
					ne[bi].push_back(index);
				}
			}
		}
		vector<vector<char> > b(n);
		for(int i=0;i<n;i++)
			b[i].resize(m,'\0');
		char name = 'a';
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<m;j++)
			{
				if(b[i][j] != '\0')
					continue;
				b[i][j] = name;
				queue<int> tc;
				tc.push(code(i,j));
				while(!tc.empty())
				{
					int c = tc.front();
					tc.pop();
					for(int l=0;l<ne[c].size();l++)
					{
						int x,y;
						decode(ne[c][l],x,y);
						if(b[x][y] == '\0')
						{
							b[x][y] = name;
							tc.push(ne[c][l]);
						}
					}
				}
				name++;
			}
		}
		cout<<"Case #"<<it<<":"<<endl;
		for(int i=0;i<n;i++)
		{
			cout<<to_s(b[i])<<endl;
		}
	}
	return 0;
}
