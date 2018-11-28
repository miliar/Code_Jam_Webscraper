
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
 *  *    else call split(s,DELIM);*/
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
int tc,r,c;
bool ok;
char str[64][64];
int main()
{
	scanf("%d",&tc);
	FOR(KK,1,tc+1)
	{
		ok=true;
		scanf("%d%d",&r,&c);
		REP(i,r)S(" %s",str[i]);
		REP(i,r)
		{
			REP(j,c)
			{
				if( str[i][j] == '#' )
				{
					if(i+1 < r && j+1 < c && str[i][j+1]=='#' && str[i+1][j]=='#' && str[i+1][j+1]=='#')
					{
						str[i][j] = '/';str[i][j+1] = '\\';
						str[i+1][j] = '\\';str[i+1][j+1]='/';
					}
					else
					{
						ok=false;
						i=r+1;
						j=c+1;
					}
				}
			}
		}
		if(ok==false)
			printf("Case #%d:\nImpossible\n",KK);
		else
		{
			printf("Case #%d:\n",KK);
			REP(i,r) 
			{
				REP(j,c) 
					printf("%c",str[i][j]);
				printf("\n");
			}
		}
	}
	return 0;
}
