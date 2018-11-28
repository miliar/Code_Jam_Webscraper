#pragma comment(linker,"/STACK:64000000")
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <cmath>
#include <map>
#include <set>
#include <ctime>
#include <algorithm>
#include <memory.h>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

#define WR printf
#define RE scanf
#define PB push_back
#define SE second
#define FI first

#define FOR(i,k,n) for(int i=(k); i<=(n); i++)
#define DFOR(i,k,n) for(int i=(k); i>=(n); i--)
#define SZ(a) (int)((a).size())
#define FA(i,v) FOR(i,0,SZ(v)-1)
#define RFA(i,v) DFOR(i,SZ(v)-1,0)
#define CLR(a) memset(a, 0, sizeof(a))

#define LL long long
#define VI  vector<int>
#define PAR pair<int ,int>
#define o_O 1000000000 
void __never(int a){printf("\nOPS %d", a);}
#define ass(s) {if (!(s)) {__never(__LINE__);cout.flush();cerr.flush();abort();}}

int n;
int M[100][100];
int T[200][200];

int sol()
{
	/*FOR(a,1,n)
	{
		FOR(b,1,n) cout << M[a][b];
		cout << "\n";
	}*/
	int ans=o_O;
	FOR(a,n,3*n)
	{
		cerr << "a=" << a << "\n";
		FOR(x,0,a-n)
			FOR(y,0,a-n)
			{
				//CLR(T);
				//FOR(b,1,a) FOR(c,1,a) T[b][c]=0;
				int sum=0;
				FOR(b,1,n) FOR(c,1,n) T[b+x][c+y]=M[b][c];
				bool flag=true;
				FOR(b,x+1,x+n) FOR(c,y+1,y+n)
				{
					int p,q;
					p=c; q=b;
					if (x+1<=p && p<=x+n && y+1<=q && q<=y+n)
						if (T[b][c] != T[p][q])
						{
							flag=false;
							break;
						}
					p=a-c+1; q=a-b+1;
					if (x+1<=p && p<=x+n && y+1<=q && q<=y+n)
						if (T[b][c] != T[p][q])
						{
							flag=false;
							break;
						}
					p=a-b+1; q=a-c+1;
					if (x+1<=p && p<=x+n && y+1<=q && q<=y+n)
						if (T[b][c] != T[p][q])
						{
							flag=false;
							break;
						}
				}
				if (flag) return a*a-n*n;
				/*FOR(b,1,a) FOR(c,1,a) if (b<x+1 || b>x+n || c<y+1 || c>y+n)
				{
					T[b][c] = max(T[b][c], max(T[c][b], max(T[a-c+1][a-b+1], T[a-b+1][a-c+1])));
					sum++;
				}
				//FOR(b,1,a) { FOR(c,1,a) cout << T[b][c]; cout << "\n"; }
				FOR(b,1,a) FOR(c,1,a) if (T[b][c]!=T[c][b] || T[b][c]!=T[a-c+1][a-b+1] || T[b][c]!=T[a-b+1][a-c+1])
				{
					flag=false;
					break;
				}*/
				//cout << (flag==1?"flag=1":"flag=0") << "\n";
				//if (flag) return sum;
			}
	}
	return ans;
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	cin >> t;
	FOR(z,1,t)
	{
		cerr << z << "\n";
		cin >> n;
		FOR(a,1,n)
		{
			int x=1;
			int y=a;
			while(1<=x && x<=n && 1<=y && y<=n)
			{
				cin >> M[x][y];
				x++;
				y--;
			}
		}
		FOR(a,2,n)
		{
			int x=a;
			int y=n;
			while(1<=x && x<=n && 1<=y && y<=n)
			{
				cin >> M[x][y];
				x++;
				y--;
			}
		}
		//int a1=sol0();
		//int a2=sol();
		//ass(a1==a2);
		cout << "Case #" << z << ": " << sol() << "\n";
		//break;
	}
	return 0;
}