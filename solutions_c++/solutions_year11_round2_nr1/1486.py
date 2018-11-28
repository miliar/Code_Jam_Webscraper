
/***** Author : Akshay *****/
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

#include <cmath>
#include <cstdio>
#include <queue>
#include <list>
#include <stack>
#include <utility>
#include <numeric>
#include <map>
#include <cctype>
#include <cstring>
#include <sstream>
#include <cstdlib>
#include <cassert>
#include <iomanip>
#include <set>
#include <fstream>

using namespace std;

#define REP(a,b) for(int a=0;a<b;a++)
#define FOR(a,b,c) for(int a=b;a<c;a++)
#define FORD(a,b,c) for(int a=b;a>=c;a--)

#define S scanf
#define P printf

#define LEN(x) ((int)x.length())
#define SZ(x) ((int)x.size())
#define ALL(x) x.begin(), x.end()
#define MP(x,y) make_pair(x,y)
#define PB(x) push_back(x)
#define INF 1000000000

typedef long long ll;
typedef pair<int,int> ii;
typedef pair<int, ii> Lii;
typedef vector<int> VI;
typedef vector<bool> VB;
typedef vector<string> VS;

int dx[]={1,-1,0,0};
int dy[]={0,0,1,-1};

/* Function for string split . If string starts with de-lim then call split(s.substr(1,s.length()),DELIM);
 *    else call split(s,DELIM);*/
std::vector<std::string> &split(const std::string &s, char delim, std::vector<std::string> &elems) {
	std::stringstream ss(s);
	std::string item;
	while(std::getline(ss, item, delim)) {
		elems.push_back(item);
	}
	return elems;
}


std::vector<std::string> split(const std::string &s, char delim) 
{
	std::vector<std::string> elems;
	return split(s, delim, elems);
}
string tostring(int n)
{
	stringstream ss ; ss<<n; return ss.str();
}
int tc,n;
char inp[105][105],tmp[105][105];
double wp[105],owp[105],oowp[105];
void getWp(void)
{
	double win=0.00;
	double played=0.00;
	for( int i = 0 ; i < n ; i++)
	{
		win=0.00;
		played=0.00;
		for( int j = 0 ; j < n ; j++ )
		{
			if( inp[i][j]=='1') 
			{
				win++;
				played++;
			}
			else if( inp[i][j] =='0' )
				played++;
		}
		wp[i] = (double)((double)win/(double)played);
	}
}
void getOwp(void)
{
	for( int i = 0 ; i < n ; i++ )
	{
		for( int j = 0 ; j < n ; j++ ) 
		{
			for( int k = 0 ; k <  n ; k++ )
				tmp[j][k]  = inp[j][k];
		}
		for( int j = 0 ; j < n ; j++ )
		{
			if( inp[i][j] == '1' || inp[i][j] == '0' )
			{
				inp[i][j]='.';
				inp[j][i]='.';
			}
		}
		double win=0.00;
		double played=0.00;
		double sum=0.00; 
		double pl=0.00;
		//inp has modified table
		for( int j = 0 ; j <  n ; j++ )
		{
			if( j == i ) continue;
			if( tmp[j][i]!='.')
			{
				pl++;
				win=0.00;
				played=0.00;
				for( int k = 0 ; k <  n ; k++ )
				{
					if( inp[j][k] == '1' )
					{
						win++;
						played++;
					}
					else if( inp[j][k] == '0' )
						played++;
				}
				if(played)
					sum = sum + (double)((double)(win)/(double)played);
			}
		}
		owp[i] = (double)((double)sum/(double)(pl));
		for( int j = 0 ; j <  n  ; j++ )
		{
			for( int k = 0 ; k <  n ; k++ )
				inp[j][k]=tmp[j][k];
		}
	}
}
void getOowp(void)
{
	for( int i = 0 ;  i < n ; i++) 
	{
		double sum = 0.00;
		double pl = 0.00;
		for( int j = 0 ; j < n ;j++)
		{
			if( inp[i][j]!='.')
			{
				sum+=owp[j];
				pl++;
			}
		}
		oowp[i] = (double)((double)sum/(double)pl);
	}
}
int main()
{
	S("%d",&tc);
	FOR(KK,1,tc+1)
	{
		S("%d",&n);
		REP(i,n) S("%s",inp[i]);
		getWp();
		getOwp();
		getOowp();
		printf("Case #%d: \n",KK);
		REP(i,n) printf("%.6lf\n",0.25*wp[i] + 0.50*owp[i] + 0.25*oowp[i]);
	}
	return 0;
}
