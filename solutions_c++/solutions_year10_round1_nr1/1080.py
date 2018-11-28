#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <map>
#include <queue>
#include <stack>
#include <cstdlib>
#include <cmath>
#include <cstdio>
#include <algorithm>
#include <numeric>

#define all(x) x.begin() , x.end()
#define sz(x) ((int) x.size())
#define INF 0x7fffffff
#define LL long long
#define LD long double
#define VI vector<int>
#define VS vector<string>

using namespace std;

int checkrow(VS &B, int K, int &b, int &r,int i,int j)
{
	string cb = string(K,'B');
	string cr = string(K,'R');
	
	int N=B.size();
	string  row="";
	for(int k=0 ; k<K  && j+k<N ; k++)
		row += string(1,B[i][j+k]);

	if(row == cb && row.size() == K) b=2;
	if(row == cr && row.size() == K) r=1;
}

int checkcol(VS &B, int K, int &b, int &r,int i,int j)
{
	string cb = string(K,'B');
	string cr = string(K,'R');
	
	int N=B.size();
	string  col="";
	for(int k=0 ; k<K  && i+k<N ; k++)
		col += string(1,B[i+k][j]);

	if(col == cb && col.size() == K) b=2;
	if(col == cr && col.size() == K) r=1;
}


int checkdia(VS &B, int K, int &b, int &r,int i,int j)
{
	string cb = string(K,'B');
	string cr = string(K,'R');
	
	int N=B.size();
	string  d1="",d2="";
	for(int k=0 ; k<K  && i+k<N &&  j+k<N ; k++)
		d1 += string(1,B[i+k][j+k]);

	for(int k=0 ; k<K  && i+k<N &&  j-k>=0 ; k++)
		d2 += string(1,B[i+k][j-k]);

	if((d1 == cb && d1.size() == K)|| (d2.size() == K && d2 == cb)) b=2;
	if((d1 == cr && d1.size() == K)|| (d2.size() == K && d2 == cr)) r=1;
}

int getRes(vector<string> & B,int N,int K)
{
	VS t=B;
	int b=0 , r=0;

	//gravity
	for(int i=0 ; i<N ; i++)
	{
		string col="";
		for(int j=0; j<N; j++)
		{
			if(B[j][i] != '.')
				col += string(1,B[j][i]);
		}

		col = string(N-col.size(),'.') + col;
	   
		for(int j=0 ; j<N; j++)
			t[j][i] = col[j];
	}



	for(int i=0  ;i<N ; i++)
	{
		for(int j=0 ; j<N ; j++)
		{
			checkrow(t,K,b,r,i,j);
			checkcol(t,K,b,r,i,j);
			checkdia(t,K,b,r,i,j);
		}
	}

	return b+r;
}

int main()
{
	int Te;
	cin >> Te;
	for(int te=0 ; te<Te  ; te++)
	{
		cout << "Case #"<<te+1 << ": ";
		int N,K;
		cin >> N >> K;
		cin.ignore();

		vector<string> board;

		for(int i=0 ; i<N ; i++)
		{
			string s;
			cin >> s;
			board.push_back(s);
		}

		vector<string> rotated;

		for(int i=0 ; i<N ; i++)
		{
			string col ="";
			for(int j=N-1 ; j>=0 ; j--)
				col += string(1,board[j][i]);
			rotated.push_back(col);
		}

		int val = getRes(rotated,N,K);
		if(val == 0) cout << "Neither\n";
		else if(val == 1) cout << "Red\n";
		else if(val == 2) cout << "Blue\n";
		else cout << "Both\n";
		
	}
}
