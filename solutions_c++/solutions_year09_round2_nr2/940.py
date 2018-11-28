
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


bool isR(string a)
{	string b=a;
	sort(b.begin(),b.end());
	string c=b;
	reverse(c.begin(),c.end());
	I l=c.size();

/*	string d;
	d.PB(c[0]);
	for(I i=l-1;i>=0 and c[i]=='0';i--)
		d.PB(c[i]);
	FOR(i,1,l)if(c[i]!='0')d.PB(c[i]);

	*/
	REP(i,l) if(a[i]!=c[i]) return false;
	return true;

}

int main()
{
	I nt;S(nt);
	I ii=0;
	while(nt--)
	{
		ii++;
		cout<<"Case #"<<ii<<": ";
		string a;
		cin>>a;
		I l=a.size();
		VI dig(10,0);
		REP(i,l)
			dig[a[i]-'0']++;
		if(isR(a))
		{
			sort(a.begin(),a.end());
			I count=1;
			REP(i,l)if(a[i]=='0')count++;
			I f=0;
			REP(i,l)
			{
				if(a[i]!='0')
				{
					if(f==0)
					{
						f=1;
						cout<<a[i];
						REP(j,count)cout<<"0";
					}
					else
						cout<<a[i];
				}
			}
			cout<<endl;
			continue;
		}
	

		I ind=l-2;
		for(int i=l-1;i>0;i--)
		{
			if(a[i-1]<a[i])
			{
				ind=i-1;
				break;
			}
		}
		REP(i,ind)cout<<a[i];
		I p=a[ind];
		I ind1=ind+1;
		FOR(j,ind+2,l)
		{
			if(a[j]>a[ind] and a[j]<a[ind1])
				ind1=j;
		}
		swap(a[ind],a[ind1]);
		cout<<a[ind];
		sort(a.begin()+ind+1 , a.end());
		FOR(i,ind+1,l)cout<<a[i];
		cout<<endl;


		/*
		I f=0;
		for(int i=l-1;i>=0;i--)
		{
			if(f==1) break;
			for(I j=i-1;j>=0;j--)
			{
				
				if(a[i]>a[j])
				{
					swap(a[i],a[j]);
					f=1;
					break;
				}
			}
		}
		cout<<a<<endl;
		*/
		

		/*
		I ans=0;
		REP(i,l)ans=ans*10+a[i]-'0';
		ans++;
		for(;;ans++)
		{
			I t=ans;
			VI D(10,0);
			while(t)
			{
				D[t%10]++;
				t=t/10;
			}
			I ff=0;
			FOR(i,1,10)if(dig[i]!=D[i])
			{
				ff=1;
				break;
			}
			if(ff==0)
			{
				cout<<ans<<endl;
				break;
			}
		}
		*/
	}
}
