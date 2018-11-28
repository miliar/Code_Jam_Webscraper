#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <map>
#include <queue>
#include <deque>
#include <stack>
#include <set>
#include <utility>
#include <sstream>
#include <cstring>

using namespace std;

typedef unsigned long long ll;

#define RP(i,s,e) for(int i=s;i<e;i++) 
#define R(i,x) RP(i,0,(x).size())
#define RP3(x,y,z) RP(i,0,x) RP(j,0,y) RP(k,0,z)
#define RI(i,x) for(typeof((x).begin()) i=(x).begin();i!=(x).end();++i)
#define pB push_back
#define P(a) cout << #a << " : " << a << endl;
#define M make_pair

template <class T, class R>
ostream & operator<<(ostream & o, pair<T,R> a){return o<<a._1<<"," << a._2;}

template <class T>
ostream & operator<<(ostream & o, vector<T> a){R(i,a) o<<a[i]<<","; return o;}
#define y1 Y1
int x1[1100],y1[1100],x2[1100],y2[1100];
/*
int nw[1100];

int gd(int a)
{
	int b=a;
	while(nw[b]!=-1) b=nw[b];
	int c=a;
	while(nw[a]!=-1) {a=nw[a]; nw[c]=b; c=a;}
	return b;
}

int link(int a, int b)
{
	int ae=gd(a),be=gd(b);
	if(ae!=be)
		nw[ae]=be;
}*/

int grid[210][210];

int main()
{
	int C;
	cin >> C;
	for(int cs=0;cs<C; ++cs)
	{
		int R;
		
		cin >> R;
		
		RP(i,0,R) {cin >> x1[i] >> y1[i] >> x2[i] >> y2[i]; }//nw[i]=-1}
		
		memset(grid,0,sizeof(grid));
		
		RP(p,0,R) {
			for(int i=x1[p]; i<=x2[p]; ++i)
			for(int j=y1[p]; j<=y2[p]; ++j)
			{
				grid[i+1][j+1]=1;
				//cout << i << " " << j << endl;
			}
		}
		
		
		//for(int i=1; i<10; ++i) {for(int j=1; j<10; ++j) cout << grid[i][j]; cout << endl;}
		//cout << endl;
		int f=1,c;
		for(c=0; f; ++c)
		{
			f=0;
			
			for(int i=205; i>0; --i)
			for(int j=205; j>0; --j){
				
				if(grid[i-1][j] && grid[i][j-1]) grid[i][j]=1;
				else if(!(grid[i-1][j] || grid[i][j-1])) grid[i][j]=0;
				if(grid[i][j]) f=1;
			}
			
			//for(int i=1; i<10; ++i) {for(int j=1; j<10; ++j) cout << grid[i][j]; cout << endl;}
			//cout << endl;
		}
		
		
		cout << "Case #" << cs+1 << ": " << c;
		
		cout << endl;
	}
	
	
}
