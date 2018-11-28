#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <queue> 
#include <stack> 
#include <bitset> 
#include <string>
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
#include <cctype>  
#include <cstring> 
#include <ctime> 
using namespace std;
/*
#define PB push_back 
#define MP make_pair 
#define maxsize 1100
typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef map<string,int> msi;
*/
int gi() { int a; scanf( "%d", &a ); return a; }//GetInteger
char gc() { char a; scanf( "%c", &a ); return a; }//GetCharacter
double gd() { double a; scanf( "%lf", &a ); return a; }//GetDouble
char StrBuf[100005];
string gstr() { scanf( "%s", StrBuf ); return StrBuf; }//GetString
char* gs() { scanf( "%s", StrBuf ); return StrBuf; }//GetString
long long gll() { long long a; scanf( "%lld", &a ); return a; }//GetLongLongInteger

#define set(a,b) memset( a, b, sizeof( a ) ) 

#define max(a,b) (a)>(b)?(a):(b) 
#define min(a,b) (a)<(b)?(a):(b) 

#define fo(i,a,b) for( (i)=(a); (i)<(int)(b); (i)++ ) //state i by yourselfe
#define rep(i,n) fo(i,0,n)		//repeat
#define repstr(i,str) for( (i)=0 ;str[(i)]; ++(i) )
/*
#define SZ(v) ((int)(v).size()) 
*/

void code(void)
{
/*input main code*/
	char field[60][60];
	int r = gi(), c = gi(), i, j, cnt;
	getchar();
	rep(i, r) 
		strcpy(field[i], gs());
	rep(i, r)
	{
		cnt = 0;
		rep(j, c)
		{
			if(field[i][j] == '.')
			{
				if(cnt%2)
				{ 
					printf("Impossible\n");
					return;
				}
				else 
				{
					cnt = 0;
				}
			}
			else if(field[i][j] == '#')
			{
				cnt++;
			}
		}
		if(cnt%2)
		{ 
			printf("Impossible\n");
			return;
		}
		else 
		{
			cnt = 0;
		}
	}
	rep(j, c)
	{
		cnt = 0;
		rep(i, r)
		{
			if(field[i][j] == '.')
			{
				if(cnt%2)
				{ 
					printf("Impossible\n");
					return;
				}
				else 
				{
					cnt = 0;
				}
			}
			else if(field[i][j] == '#')
			{
				cnt++;
			}
		}
		if(cnt%2)
		{ 
			printf("Impossible\n");
			return;
		}
		else 
		{
			cnt = 0;
		}
	}
	rep(i, r)
	{
		rep(j, c)
		{
			if(field[i][j] == '#')
			{
				field[i][j] = '/';
				field[i][j+1] = '\\';
				field[i+1][j] = '\\';
				field[i+1][j+1] = '/';
			}
		}
	}
	rep(i, r)
		printf("%s\n", field[i]);
//printf(" \n" );
}
int main (void)
{
	freopen( "A-large.in", "r", stdin );
	freopen( "output.txt", "w", stdout );
	int T, I;
	T = gi();
	rep(I, T)
	{
		printf("Case #%d:\n", I+1);
		code();
	}
	return 0;
}