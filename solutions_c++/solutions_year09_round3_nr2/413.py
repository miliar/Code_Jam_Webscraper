
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

int main()
{
	I nt;S(nt);
	I ii=0;
	while(nt--)
	{
		ii++;
		cout<<"Case #"<<ii<<": ";
		I n;S(n);
		vector<double> x(n),y(n),z(n),vx(n),vy(n),vz(n);
		REP(i,n)
			cin>>x[i]>>y[i]>>z[i]>>vx[i]>>vy[i]>>vz[i];
		
		double cm[3];
		cm[0]=cm[1]=cm[2]=0;
		REP(i,n)
			cm[0] +=x[i];
		REP(i,n)
			cm[1] +=y[i];
		REP(i,n)
			cm[2] +=z[i];
		cm[0]=cm[0]/n;
		cm[1]=cm[1]/n;
		cm[2]=cm[2]/n;
			
		double xx=cm[0] , yy=cm[1] , zz=cm[2];

		double Vx=0, Vy=0,Vz=0;
		REP(i,n)Vx +=vx[i];
		Vx=Vx/n;
		REP(i,n)Vy +=vy[i];
		Vy=Vy/n;
		REP(i,n)Vz +=vz[i];
		Vz=Vz/n;

		double a=(Vx*Vx + Vy*Vy + Vz*Vz);
		double b=2*(xx*Vx+yy*Vy + zz*Vz);
		double c=xx*xx+yy*yy+zz*zz;

	//	cout<<a<<" "<<b<<" "<<c<<endl;

		if(a==0)
		{
			if(b>=0)
				printf("%.8lf 0.000000\n",sqrt(c));
			else
				printf("0.000000 %.8lf\n",-(c/b));
		}
		else if(b>=0)
		{
			printf("%.8lf 0.000000\n",sqrt(c));
		}
		else //b <0
		{
			if(b*b-4*a*c <0)
			{
				double t=-(b/(2*a));
				printf("%.8lf %.8lf\n",sqrt(a*t*t+b*t+c),t);	
			}
			else
			{
			//	cout<<"here\n";
				double d=b*b-4*a*c;
				double ans1=(-b-sqrt(d))/(2*a);
				double ans2=(-b+sqrt(d))/(2*a);
				//cout<<ans1<<" "<<ans2<<endl;
		//		if(ans1>=0)
		//			ans2=min(ans1,ans2);
			//	cout<<"0 "<<ans2<<endl;
				printf("0.000000 %lf\n",ans2);
			}
		}
	}
}
