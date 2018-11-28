
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
int tc,n;
ll l,h,inp[10010],lcm,ret;
bool ok;
bool gogo(int p)
{
	REP(i,n) if( inp[i]%p !=0 && p%inp[i]!=0 ) return false;
	return true;
}
int main()
{
	scanf("%d",&tc);
	FOR(KK,1,tc+1)
	{
		ok=false;
		scanf("%d%lld%lld",&n,&l,&h);
		REP(i,n)S("%lld",&inp[i]);
		for( int i=l;i<=h;i++)
			if(gogo(i)) {ret=i;ok=true;i=h+1;}
		if( ok==0 ) printf("Case #%d: NO\n",KK);
		else printf("Case #%d: %lld\n",KK,ret);
	}
	return 0;
}
