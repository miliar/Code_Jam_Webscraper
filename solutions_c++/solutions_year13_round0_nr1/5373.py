// A - Tic Tac Toe
// wahyuoi

#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
#include <map>
#include <queue>
#include <stack>
#include <set>
#include <cmath>
using namespace std;
#define ll int
#define INF 1000000000
#define debug puts("DEBUUGG")
#define vi vector<ll>
#define pii pair<ll,ll>
#define vii vector<pii>
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define rep(a,b,c) for(a=b;a<c;a++)
#define repe(a,b,c) for(a=b;a<=c;a++)
#define repd(a,b,c) for(a=b-1;a>=c;a--)
#define ALL(a) (a.begin(),a.end())
bool O,X;
char s[10][10];
void datar(int r, char c){
	if (c=='.')
	{
		return;
	} else if (c=='T')
	{
		datar(r,s[r][1]);
	}
	bool ret = true;
	for (int i=0;i<4 ;++i )
	{
		if (s[r][i]!=c && s[r][i]!='T')
		{
			ret=false;
		}
	}
	if (c=='X')
	{
		X |= ret;
	} else {
		O |=ret;
	}
}
void turun(int col, char c){
	if (c=='.')
	{
		return;
	} else if (c=='T')
	{
		turun(col,s[1][col]);
	}
	bool ret= true;
	for (int i=0;i<4 ;++i )
	{
		if (s[i][col]!=c && s[i][col]!='T')
		{
			ret=false;
		}
	}
	if (c=='X')
	{
		X |= ret;
	} else {
		O |= ret;
	}
}
void dig1(char c){
	if (c=='.')
	{
		return;
	} else if (c=='T')
	{
		dig1(s[1][1]);
	}
	bool ret=true;
	for (int i=0; i<4; ++i)
	{
		if (s[i][i]!=c && s[i][i]!='T')
		{
			ret=false;
		}
	}
	if (c=='X')
	{
		X |= ret;
	} else {
		O |= ret;
	}
}
void dig2(char c){
	if (c=='.')
	{
		return;
	} else if (c=='T')
	{
		dig1(s[1][2]);
	}
	bool ret=true;
	for (int i=0; i<4; ++i)
	{
		if (s[i][3-i]!=c && s[i][3-i]!='T')
		{
			ret=false;
		}
	}
	if (c=='X')
	{
		X |= ret;
	} else {
		O |= ret;
	}
}
void solve(int tc){
	scanf("\n");
	O = X = false;
	for (int i=0;i<4 ;++i )
	{
		gets(s[i]);
	}
	for (int i=0;i<4 ;++i )
	{
		datar(i,s[i][0]);
		turun(i,s[0][i]);
	}
	dig1(s[0][0]); 
	dig2(s[0][3]);
	if (X)
	{
		printf("Case #%d: X won\n",tc);
		fprintf(stderr,"Case #%d: X won\n",tc);
	} else if (O)
	{
		printf("Case #%d: O won\n",tc);
		fprintf(stderr,"Case #%d: O won\n",tc);
	} else {
		bool dot = false;
		for (int i=0; i<4; ++i)
		{
			for (int j=0;j<4 ;++j )
			{
				if (s[i][j]=='.')
				{
					dot=true;
				}
			}
		}
		if (dot)
		{
			printf("Case #%d: Game has not completed\n",tc);
			fprintf(stderr,"Case #%d: Game has not completed\n",tc);
		} else {
			printf("Case #%d: Draw\n",tc);
			fprintf(stderr,"Case #%d: Draw\n",tc);
		}
	}
}
int main(){
	int n;
	scanf("%d",&n);
	for (int tc=1;tc<=n ;++tc )
	{
		solve(tc);
	}
}
