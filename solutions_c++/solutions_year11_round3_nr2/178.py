
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
int tc,n,l,c,cur;
ll t,inp[1000100],T,T1;
int main()
{
	int i,j;
	scanf("%d",&tc);
	FOR(KK,1,tc+1)
	{
		scanf("%d%lld%d%d",&l,&t,&n,&c);
		for(  i = 0 ; i < c  ; i++ ) S("%lld",&inp[i]);
		i=c;
		T=0;
		while( i < n )
		{
			j=0;
			while( j < c )
			{
				inp[i] = inp[j];
				j++;
				i++;
				if( i == n ) break;
			}
		}
		for( i = 0 ; i < n  ; i++) T+=inp[i];
		T *= 2  ;
		//This would have been required time there had been no speed boosters
		//t- time for speed boosters to be set up
		cur=0;
		T1 = 0 ;
		while(cur < n )
		{
			if( T1+ 2*inp[cur] <= t ) 
			{
				T1 = T1+2*inp[cur];
				cur=cur+1;
			}
			else
			{
				priority_queue<ll> pq;
				pq.push(inp[cur]-((t-T1)/2));
				for( int k = cur+1; k < n ; k++ ) pq.push(inp[k]);
				i = 0 ;
				while( i < l )
				{
					if(pq.empty()==true) break;
					T-=pq.top();
					pq.pop();
					i++;
				}
				break;
			}
		}
		printf("Case #%d: %lld\n",KK,T);
	}
	return 0;
}
