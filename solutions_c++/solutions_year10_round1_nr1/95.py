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

char board[100][100], b2[100][100], b3[100][100];

int main()
{
	int C;
	cin >> C;
	for(int cs=0; cs<C; ++cs)
	{
		int n,K;
		
		cin >> n >> K;
		
		RP3(n,n,1) cin >> board[i][j];
		
		int p=0;
		
		RP3(n,n,1) b2[j][n-1-i]=board[i][j];
		
		RP3(n,n,1) b3[i][j]='.';
		
		RP(x,0,n) {
			int k=n-1;
			for(int y=n-1; y>=0; --y) if(b2[y][x]!='.') b3[k--][x]=b2[y][x];
		}
		
		RP3(n,n,1)
		{
			int f=1;
			if(b3[i][j]=='.') continue;
			if(b3[i][j]=='R') ++f;
			for(int k=0; (k<K || (p|=f,0)) && b3[i][j] == b3[i+k][j] && k+i<n; ++k);
			for(int k=0; (k<K || (p|=f,0)) && b3[i][j] == b3[i][j+k] && k+j<n; ++k);
			for(int k=0; (k<K || (p|=f,0)) && b3[i][j] == b3[i+k][j+k] && k+j<n && k+i<n; ++k);
			for(int k=0; (k<K || (p|=f,0)) && b3[i][j] == b3[i-k][j+k] && k+j<n && i-k>=0; ++k);
		}
		/*
		RP(i,0,n){RP(j,0,n) cout << b2[i][j]; cout << endl;}
		cout << endl;
		RP(i,0,n){RP(j,0,n) cout << b3[i][j]; cout << endl;}
		cout << endl;
		*/
		cout << "Case #" << cs+1 << ": ";
		if(p==0) cout << "Neither";
		else if(p==1) cout << "Blue";
		else if(p==2) cout << "Red";
		else if(p==3) cout << "Both";
		cout << endl;
	}
}


