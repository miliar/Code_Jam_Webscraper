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

#define FOR(i,a,b) for( (i)=(a); i<(b); ++(i) ) //state i by yourselfe
#define rep(i,n) FOR(i,0,n)		//repeat
#define repstr(i,str) for( (i)=0 ;str[(i)]; ++(i) )
/*
#define SZ(v) ((int)(v).size()) 
*/

void main (void)
{
	freopen( "A-large.in", "r", stdin );
	freopen( "output.txt", "w", stdout );
	int T, I;
	T = gi();
	for(I=1; I<=T; I++)
	{
		printf("Case #%d:\n", I);

		/*input main code*/
		int n = gi(), i, j, count;
		char list[110][110];
		double wp[100][2], owp[100], oowp[100], sum;
		set(list, 0);
		getchar();
		rep(i, n)
		{
			sum = count = 0;
			scanf( "%s", list[i] );
			rep(j, n)
			{
				if(list[i][j]=='0' || list[i][j]=='1')
				{
					sum += list[i][j]-'0';
					count++;
				}
			}
			wp[i][0] = sum;
			wp[i][1] = count;
			//printf("%f,%d,%f ", sum, count, wp[i][0]/wp[i][1]);
		}
		//printf("\n" );
		rep(i, n)
		{
			sum = count = 0;
			rep(j, n)
			{
				if(list[i][j]=='0')
				{
					count++;
					sum += (wp[j][0]-1)/(wp[j][1]-1);
				}
				else if(list[i][j]=='1')
				{
					count++;
					sum += (wp[j][0])/(wp[j][1]-1);
				}
			}
			owp[i] = sum/count;
			//printf("%f,%d,%lf ", sum, count, owp[i]);
		}
		//printf("\n" );
		rep(i, n)
		{
			sum = count = 0;
			rep(j, n)
			{
				if(list[i][j]=='0' || list[i][j]=='1')
				{
					count++;
					sum += owp[j];
				}
			}
			oowp[i] = sum/count;
			//printf("%f,%d,%f ", sum, count, oowp[i]);
		}
		//printf("\n" );
		rep(i, n)
		{
			printf("%0.12lf\n", 0.25*wp[i][0]/wp[i][1] + \
				0.50*owp[i] + 0.25*oowp[i]);
		}
		//printf(" \n" );
	}
}