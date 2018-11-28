/*
ID: Tariqul
PROG: 
LANG: C++
*/

#include <algorithm> 
#include <cctype> 
#include <cmath> 
#include <cstdio> 
#include <cstdlib> 
#include <cstring> 
#include <deque> 
#include <iostream> 
#include <list> 
#include <map> 
#include <numeric> 
#include <queue> 
#include <set> 
#include <sstream> 
#include <stack> 
#include <string> 
#include <vector>

using namespace std; 

#define fo(i,j,n) for(i=j;i<n;++i)
#define Fo(i,j,n) for(i=n-1;i>=j;--i)
#define foo(i,j,v) fo(i,j,sz(v))
#define Foo(i,j,v) Fo(i,j,sz(v))
#define li(v) v.begin(),v.end()
#define sz(v) ((int)v.size())
#define CLR(a,v) memset((a),(v),sizeof(a))
#define inf 1000000001
//typedef long long Long;
typedef __int64 Long;
#define pi (2*acos(0))
#define eps 1e-9

#define two(X) (1<<(X))
#define twoL(X) (((Long)(1))<<(X))
#define contain(S,X) (((S)&two(X))!=0)
#define containL(S,X) (((S)&twoL(X))!=0)

char BUFFER[100000 + 5];
bool readn(int &n)	{ return scanf("%d",&n) == 1; } 
bool readl(Long &n)	{ return scanf("%I64d",&n) == 1; } 
bool readd(double &n){ return scanf("%lf",&n) == 1; } 
bool reads(string &s){ s = ""; int n = scanf("%s",BUFFER); if(n == 1)s = BUFFER; return n == 1; }
bool readln(string &s){ char *valid = gets(BUFFER); if(valid)s = BUFFER; return ((bool)valid); }

string board[4];

void calculate(int i,int j,int &one,int &two,int &dot, int &T)
{	
	if(board[i][j] == 'X')one++;
	else if(board[i][j] == 'O')two++;
	else if(board[i][j] == 'T')T++;
	else dot++;
}

string getValue()
{
	int one = 0, two = 0, T = 0, dot = 0,i,j;
	
	one = 0, two = 0, T = 0, dot = 0; 
	fo(i,0,4)calculate(i,i,one,two,dot,T);
	if((one + T) >= 4)return "X won";
	if((two + T) >= 4)return "O won";

	one = 0, two = 0, T = 0, dot = 0; 
	fo(i,0,4)calculate(i,3-i,one,two,dot,T);
	if((one + T) >= 4)return "X won";
	if((two + T) >= 4)return "O won";

	fo(i,0,4)
	{
		one = 0,two = 0,T = 0, dot = 0;
		fo(j,0,4)calculate(i,j,one,two,dot,T);		
		if((one + T) >= 4)return "X won";
		if((two + T) >= 4)return "O won";
	}
	fo(j,0,4)
	{
		one = 0,two = 0,T = 0,dot = 0;
		fo(i,0,4)calculate(i,j,one,two,dot,T);		
		if((one + T) >= 4)return "X won";
		if((two + T) >= 4)return "O won";
	}

	one = 0, two = 0, T = 0, dot = 0; 
	fo(i,0,4)fo(j,0,4)calculate(i,j,one,two,dot,T);

	if(dot == 0)return "Draw";
	return "Game has not completed";	
}

int main()
{
	freopen("D://input.txt","r",stdin);
	freopen("D://output.txt","w",stdout);
	int Case,t,i;
	scanf("%d",&t);
	fo(Case,1,t+1)
	{	
		fo(i,0,4)cin >> board[i];
		
		printf("Case #%d: ",Case); cout << getValue();
		cout << endl;
	}
	return 0;
} 

