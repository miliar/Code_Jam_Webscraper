
#include<iostream>
#include <vector>
#include <stack>
#include <map>
#include <queue>
#include <list>
#include <algorithm>
#include <set>
#include <cstring>
#include<string.h>
#include <cmath>
#include<math.h>
#include <cassert>
#include <sstream>
#include <climits>
#include <deque>
#include <fstream>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <ctime>
using namespace std;

#define FOR(i,a,b)         for(int i= (int )a ; i < (int )b ; ++i) 
#define REP(i,n)           FOR(i,0,n)
#define PB                 push_back
#define PP                 pop()
#define EM                 empty()
#define INF                2000000000
#define PF                 push_front
#define ALL(x)             x.begin(),x.end()
#define SORT(x)            sort(ALL(x))
#define V(x)               vector< x >
#define PRINT(x)           cout << #x << " " << x << endl
#define LET(x,a)           __typeof(a) x(a)
#define IFOR(i,a,b) 	   for(LET(i,a);i!=(b);++i)
#define EACH(it,v)  	   IFOR(it,v.begin(),v.end())
#define PRESENT(c,x) 	   ((c).find(x) != (c).end())
#define SZ(x) 		   x.size();
#define CPRESENT(c,x) 	   (find(c.begin(),c.end(),x) != (c).end())
#define S(N)		   scanf("%d",&N)

typedef map<int,int>    MI;
typedef pair<int,int>   PI;
typedef long long int   LL;
typedef V( int )        VI;
typedef V( VI )         VVI;
typedef V( bool )       VB;
typedef V( VB )         VVB;
typedef V( PI  )        VPI;
typedef V( string )     VS;
typedef V( VS )         VVS;
typedef int             I ;

class my
{
	public:

};

VS parse(string &str)
{
	VS ret;
	I l=str.size();
	REP(i,l)
	{
		if(str[i]=='(')
		{
			i++;
			string s;
			while(str[i]!=')')
				s.PB(str[i++]);
			ret.PB(s);

		}
		else
		{
			string s;
			s.PB(str[i]);
			ret.PB(s);
		}
	}
	return ret;
}

bool found(char ch , string &str)
{
	I l=str.size();
	REP(i,l)
		if(str[i]==ch)
			return true;
	return false;
}

int main()
{

	I l,d,n;
	S(l);S(d);S(n);
	VS  Dict(d);
	REP(i,d) 
		cin>>Dict[i];
	
	SORT(Dict);
	
	REP(ii,n)
	{
		cout<<"Case #"<<ii+1<<": ";
		string str;
		cin>>str;

		VS arr=parse(str);
		
		int count=0;
		REP(i,d)
		{
			if(i!=0 and Dict[i]==Dict[i-1])
				continue;
			I f=0;
			REP(j,l)
			{
				size_t found;
				found=arr[j].find(Dict[i][j]);
				if(found==string::npos)
				{
					f=1;
					break;
				}
			}
			if(f==0)
				count++;
		}
		printf("%d\n",count);
	}
}

