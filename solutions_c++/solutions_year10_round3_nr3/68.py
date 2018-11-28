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

int n, m;
bool M[530][530];
int S[530][530];
char tmp[1000];
int boards[530];
bool T[10000000];

int char_to_int(char ch)
{
	if (ch>='0' && ch<='9') return ch-'0';
	if (ch>='A' && ch<='F') return ch-'A'+10;
	ass(false);
	return -1;
}

bool query(int X1, int Y1, int X2, int Y2, int ind=1, int XX1=1, int YY1=1, int XX2=512, int YY2=512)
{
	if (X1>X2 || Y1>Y2) return false;
	if (XX1>XX2 || YY1>YY2) return false;
	ass(ind<10000000);
	if (X1==XX1 && Y1==YY1 && X2==XX2 && Y2==YY2) return T[ind];
	int dx = ((XX1+XX2)>>1)+1;
	int dy = ((YY1+YY2)>>1)+1;
	if (X1<dx && Y1<dy) if (query(X1,Y1,min(dx-1,X2),min(dy-1,Y2),ind*4,XX1,YY1,dx-1,dy-1)) return true;
	if (X1<dx && Y2>=dy) if (query(X1,max(dy,Y1),min(dx-1,X2),Y2,ind*4+1,XX1,dy,dx-1,YY2)) return true;
	if (X2>=dx && Y1<dy) if (query(max(dx,X1),Y1,X2,min(dy-1,Y2),ind*4+2,dx,YY1,XX2,dy-1)) return true;
	if (X2>=dx && Y2>=dy) if (query(max(dx,X1),max(dy,Y1),X2,Y2,ind*4+3,dx,dy,XX2,YY2)) return true;
	return false;
}

void update(int x, int y, int ind=1, int XX1=1, int YY1=1, int XX2=512, int YY2=512)
{
	if (XX1>XX2 || YY1>YY2) return;
	if (x<XX1 || x>XX2 || y<YY1 || y>YY2) return;
	ass(ind<10000000);
	T[ind]=true;
	if (YY1==YY2 && XX1==XX2) return;
	int dx = ((XX1+XX2)>>1)+1;
	int dy = ((YY1+YY2)>>1)+1;
	if (x<dx)
	{
		if (y<dy) update(x,y,ind*4,XX1,YY1,dx-1,dy-1);
		else update(x,y,ind*4+1,XX1,dy,dx-1,YY2);
	}
	else
	{
		if (y<dy) update(x,y,ind*4+2,dx,YY1,XX2,dy-1);
		else update(x,y,ind*4+3,dx,dy,XX2,YY2);
	}
}

void sol()
{
	FOR(a,1,n) FOR(b,1,m) if ((a+b)&1) M[a][b]=!M[a][b];

	/*cout << "\n";
	FOR(a,1,n)
	{
		FOR(b,1,m) cout << (M[a][b]?"#":".");
		cout << "\n";
	}*/

	CLR(boards);
	CLR(T);

	FOR(b,1,n) FOR(c,1,m) S[b][c]=S[b-1][c]+S[b][c-1]-S[b-1][c-1]+(M[b][c]?1:0);

	DFOR(a,min(n,m),1)
	{
		cerr << a << "\n";
		FOR(b,1,n) FOR(c,1,m)
		{
			if (b+a-1<=n && c+a-1<=m)
			{
				int sum=S[b+a-1][c+a-1]-S[b-1][c+a-1]-S[b+a-1][c-1]+S[b-1][c-1];
				if (sum==0 || sum==a*a)
				{
					bool flag=!query(b,c,b+a-1,c+a-1);
					if (flag)
					{
						//cerr << a << " " << b << " " << c << "\n";
						boards[a]++;
						FOR(d,b,b+a-1) FOR(e,c,c+a-1)
						update(d,e);
					}
				}
			}
		}
	}

	/*FOR(a,1,n-1)
	{
		FOR(b,1,m-1) cout << (query(a,b,a+1,b+1)?1:0);
		cout << "\n";
	}*/

	int ans=0;
	FOR(a,1,max(n,m)) if (boards[a]) ans++;
	cout << ans;
	DFOR(a,max(n,m),1) if (boards[a]) cout << "\n" << a << " " << boards[a];
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	cin >> T;
	FOR(a,1,T)
	{
		cin >> n >> m;
		FOR(b,1,n)
		{
			RE("%s", tmp);
			FOR(c,0,m-1) M[b][c+1]=((char_to_int(tmp[c>>2])>>((3-c)&3))&1);
		}
		cout << "Case #" << a << ": ";
		sol();
		cout << "\n";
	}
	return 0;
}