
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
#define PR(v)              REP(iii,v.size())cout<<v[iii]<<" ";cout<<endl;

bool isUpperCase(char c){return c>='A' && c<='Z';}//NOTES:isUpperCase
bool isLowerCase(char c){return c>='a' && c<='z';}//NOTES:isLowerCase
bool isLetter(char c){return c>='A' && c<='Z' || c>='a' && c<='z';}//NOTES:isLetter
bool isDigit(char c){return c>='0' && c<='9';}//NOTES:isDigit(


//translator 
char toLowerCase(char c){return (isUpperCase(c))?(c+32):c;}//NOTES:toLowerCase
char toUpperCase(char c){return (isLowerCase(c))?(c-32):c;}//NOTES:toUpperCase
int toInt(string s){int r=0;istringstream sin(s);sin>>r;return r;}//NOTES:toInt
long long  toLL(string s){long long  r=0;istringstream sin(s);sin>>r;return r;}//NOTES:toLL
//double toFloat(string s){float r=0;istringstream sin(s);sin>>r;return r;}//NOTES:toFloat
//double toDouble(string s){double r=0;istringstream sin(s);sin>>r;return r;}//NOTES:toDouble


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


VVS SW(I indx, VS a, I n)
{	
	VVS r;
	FOR(i,indx+1,n)
	{
			swap(a[i],a[indx]);
			r.PB(a);
			swap(a[i],a[indx]);
	}
	return r;
}

void P(VS a)
{
	REP(i,a.size())
		cout<<a[i]<<endl;
	cout<<endl;
}

class my
{
	public:
		VS a;
		I val;
		my(VS aa, I vv)
		{
			a=aa;val=vv;
		}
};

bool isOk(VS a)
{
	I n=a.size();
	REP(i,n)REP(j,n)
		if(j>i and a[i][j]=='1')
		{
			return  false;
		}
	 return true;

}
I fn(I n, VS a , map<VS , I > &mp)
{
	queue<my> Q;
	I min=INF;
	if(isOk(a))
		return 0;

	my mm(a,0);
	Q.push(mm);
	mp[a]=1;
	while(!Q.empty())
	{
		my temp=Q.front();
		Q.pop();
		
		VS aa=temp.a;
		I v=temp.val;
		
//		P(aa);

		if(isOk(aa)) return v;

		REP(i,n-1)
		{
		//	VVS r=SW(i,aa,n);
			swap(aa[i],aa[i+1]);
				my mmm(aa,1+v);
				if(mp.find(aa)==mp.end())
				{
					Q.push(mmm);
					mp[aa]=1;
				}
			swap(aa[i],aa[i+1]);
		}
	}
//	cout<<"h\n";
}

int main()
{
	I nt;S(nt);
	I ii=0;
	while(nt--)
	{
		map<VS , I > mp;

		ii++;
		I n;S(n);
		VS a(n);
		REP(i,n) cin>>a[i];

		cout<<"Case #"<<ii<<": "<<fn(n,a,mp)<<endl;
	}
}
