#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <vector>
#include <algorithm>
#include <string>
#include <cstdio> 
#include <deque>  
#include <queue>
#include <stack> 
#include <iomanip>
#include <cctype>

#define rep(i,n) for(i=0;i<n;i++)
#define INF 1000000000

using namespace std;

int main()
{
	int i,j,k,ii,T,H,W;
	ifstream in("input.txt");
	ofstream out("output.txt");
	in>>T;
	rep(k,T)
	{
		int n,w,e,s;
		in>>H>>W;
		vector< vector<int> > m;
		vector< vector<int> > b;
		vector< vector<char> > v;
		m.resize(H);
		v.resize(H);
		b.resize(H);
		rep(i,H)
		{
			m[i].resize(W);
			v[i].resize(W);
			b[i].resize(W);
		}
		rep(i,H)
		{
			rep(j,W)
			{
				in>>m[i][j];
				v[i][j]='*';
				b[i][j]=i*W+j;
			}
		}
		rep(i,H)
		{
			rep(j,W)
			{
				n=w=e=s=INF;
				if (i>0) n=m[i-1][j];
				if (i<(H-1)) s=m[i+1][j];
				if (j>0) w=m[i][j-1];
				if (j<(W-1)) e=m[i][j+1];
				if (!((m[i][j]<n)&&(m[i][j]<w)&&(m[i][j]<e)&&(m[i][j]<s)))
				{
					if ((n<=w)&&(n<=e)&&(n<=s)&&(n<m[i][j])) b[i][j]=b[i-1][j];
					else if ((w<n)&&(w<=e)&&(w<=s)&&(w<m[i][j])) b[i][j]=b[i][j-1];
					else if ((e<n)&&(e<w)&&(e<=s)&&(e<m[i][j])) b[i][j]=b[i][j+1];
					else if ((s<n)&&(s<w)&&(s<e)&&(s<m[i][j])) b[i][j]=b[i+1][j];
				}
			}
		}
		vector <char> tc;
		vector <int> tn;
		vector <int>::iterator it;
		char c='a';
		rep(i,H)
		{
			rep(j,W)
			{	
				if (v[i][j]=='*')
				{
					int x=i,y=j;
					vector <int> X,Y;
					while ((b[x][y])!=(x*W+y))
					{
						int _x=x,_y=y;
						X.push_back(x);
						Y.push_back(y);
						v[_x][_y]=c;
						x=((b[_x][_y])/W);
						y=((b[_x][_y])%W);
					}
					if (v[x][y]!='*')
						rep(ii,X.size())
							v[X[ii]][Y[ii]]=v[x][y];
					else v[x][y]=c++;
				}
			}
		}
		out<<"Case #"<<(k+1)<<":"<<endl;
		rep(i,H)
		{
			rep(j,W)
				out<<v[i][j]<<" ";
			out<<endl;
		}
	}
	return 0;
}

