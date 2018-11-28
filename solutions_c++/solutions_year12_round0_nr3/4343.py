
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
std::vector<std::string> &split(const std::string &s, char delim, std::vector<std::string> &elems) 
{
	std::stringstream ss(s);
	std::string item;
	while(std::getline(ss, item, delim)) 
		elems.push_back(item);
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
int tc,a,b,res;
bool gogo( int p,int q )
{
	string s1=tostring(p);
	string s2=tostring(q);
	int l1 = s1.length();
	int l2 = s2.length();
	if( l1 != l2 ) return false;
	if( s1 == s2 ) return true;
	for(int i=1;i<l1;i++)
	{
		string t = s1.substr(i) + s1.substr(0,i) ;
		if( s2 == t ) return true;
	}
	return false;
}
int main()
{
	scanf("%d",&tc);
	for(int k=0;k<tc;k++)
	{
		scanf("%d%d",&a,&b);
		res=0;
		for(int i=a;i<=b;i++)
		{
			for(int j=i+1;j<=b;j++) if(gogo(i,j)) res++;
		}
		printf("Case #%d: %d\n",k+1,res);
	}
	return 0;
}
