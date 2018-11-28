#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define _for(i,x,n) for(int i=x;i<n;i++)
#define _forc(i,x,n,c) for(int i=x;i<n && c;i++)
#define _ifor(i,x,n) for(int i=(n);i>=x;i++)
#define _forv(it,v) for(typeof((v).begin()) it=(v).begin(); it!=(v).end(); it++)

#define _dv(var) cout<<"L"<<__LINE__<<": "<<#var<<": "<<var<<endl;
#define _dav(i,f) cout<<"L"<<__LINE__<<": "<<#i<<"-"<<#f<<": "; dav(i,f);
template<typename it> void dav(it i,it f)
	{ cout<<"[ "; while(i!=f) cout<<*(i++)	<<" "; cout<<"]"<<endl; }
#define _ln cout<<"_ln: "<<__LINE__<<endl;

int main()
{
	int T;
	cin>>T;
	for(int zz=1;zz<=T;zz++)
	{
		int R,C;
		cin>>R>>C;
		string p[R];
		_for(i,0,R)
			cin>>p[i];

		int dx[]={1,0,1};
		int dy[]={0,1,1};
		char nc[]={'\\','\\','/'};
		//string r[R];
		bool pos=true;
		_forc(i,0,R,pos)
			_forc(j,0,C,pos)
				if(p[i][j]=='#')
				{
					p[i][j]='/';
					bool b=true;
					for(int k=0;k<3 && b;k++)
					{
						int nx=i+dy[k],ny=j+dx[k];
						if(nx>=R || ny>=C || p[nx][ny]!='#')
							b=false;
						else
							p[nx][ny]=nc[k];
					}
					if(!b)
						pos=false;
				}

		if(pos)
		{
			cout<<"Case #"<<zz<<":"<<endl;
			_for(i,0,R)
				cout<<p[i]<<endl;
		}
		else
			cout<<"Case #"<<zz<<":\nImpossible"<<endl;
	}

	return 0;
}
