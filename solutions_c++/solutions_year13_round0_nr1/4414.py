// a.cpp:
// By Andrew Moskalchuk (HorgH) 
//

#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <map>
#include <set>
#pragma comment(linker,"/STACK:16777216")
using namespace std;

//Loops
#define FOR(i,a,b) for(int (i) = (a); (i) <= (b); ++(i))
#define ROF(i,a,b) for(int (i) = (a); (i) >= (b); --(i))
#define rep(i,n) for (int (i) = 0; (i) < (n); ++(i))
#define fe(i,a) for (int (i) = 0; (i) < int((a).size()); ++(i))
#define MEM(a,b) memset((a),(b),sizeof(a))

//Constants
#define inf 1000000000
#define pi 2*acos(0.0)
#define N 100010
#define eps 1e-9

//Functions
#define pb push_back
#define ppb pop_back
#define all(c) (c).begin(), (c).end()
#define sz(x) int((x).size())
#define sqr(a) (a)*(a)

//Pairs
#define mp(a,b) make_pair((a), (b))
#define X first
#define Y second

//Input-Output
#define FREOPEN(a,b) freopen(a,"r",stdin); freopen(b,"w",stdout);

typedef vector<int> vint;
typedef long long ll;
typedef pair<int, int> pii;

char s[5][5];
bool e;
int main()
{
    FREOPEN("input.txt","output.txt");
    int test,x,y,t;
	bool f1,f2;
	string ans;
	scanf("%d\n",&test);
	rep(tt,test)
	{
		rep(i,4)gets(s[i]);
		scanf("\n");
		e=f1=f2=false;
		rep(i,4)
		{
			x=0; y=0; t=0;
		    rep(j,4)
			{
				if(s[i][j] == 'X')x++; else
				if(s[i][j] == 'O')y++; else
				if(s[i][j] == 'T')t++; else
				if(s[i][j] == '.')e=true;
			}
			if(x==4 || x==3 && t==1)f1=true;
			if(y==4 || y==3 && t==1)f2=true;
		}
		rep(j,4)
		{
			x=0; y=0; t=0;
		    rep(i,4)
			{
				if(s[i][j] == 'X')x++; else
				if(s[i][j] == 'O')y++; else
				if(s[i][j] == 'T')t++; else
				if(s[i][j] == '.')e=true;
			}
			if(x==4 || x==3 && t==1)f1=true;
			if(y==4 || y==3 && t==1)f2=true;
		}
		x=0; y=0; t=0;
		rep(i,4)
		{
				if(s[i][i] == 'X')x++; else
				if(s[i][i] == 'O')y++; else
				if(s[i][i] == 'T')t++; else
				if(s[i][i] == '.')e=true;
		}
		if(x==4 || x==3 && t==1)f1=true;
		if(y==4 || y==3 && t==1)f2=true;
		x=0; y=0; t=0;
		rep(i,4)
		{
				if(s[i][3-i] == 'X')x++; else
				if(s[i][3-i] == 'O')y++; else
				if(s[i][3-i] == 'T')t++; else
				if(s[i][3-i] == '.')e=true;
		}
		if(x==4 || x==3 && t==1)f1=true;
		if(y==4 || y==3 && t==1)f2=true;
		ans="WA";
		if(f1 && !f2)ans="X won"; else
		if(!f1 && f2)ans="O won"; else
		if(f1 && f2 || !f1 && !f2)
		{
			if(!e)ans="Draw"; else ans="Game has not completed";
		} 
		printf("Case #%d: ",tt+1);
		cout << ans << endl;
	}
	return 0;   
}
