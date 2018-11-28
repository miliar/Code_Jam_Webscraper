#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <functional>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <stack>
#include <vector>

using namespace std;
/*========================================Templates=============================================*/
// datatypes
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef double db;
typedef float ft;
typedef unsigned int uint;
int gcd( int a, int b ) {  if( !b ) return a;  return gcd( b, a % b ); }


#define tests(tc) int tc;scanf("%d",&tc);while(tc--)
#define REP(i,n) for(int i=0;i<(n);++i)
#define FOR(i,a,b) for(int i=(a);i<=(b);++i)
#define FORN(i,a,b,n) for(int i=(a);i<=(b);i+=n)
#define FORR(i,a,b) for(int i=(a);i>=(b);--i)
#define FORRN(i,a,b,n) for(int i=(a);i>=(b);i-=n)
#define CLEAR(arr,v)      memset(arr,v,sizeof(arr))
#define DB(x) cerr<<#x<<" : "<<x<<endl<<flush;
#define DB2(x,y) cerr<<#x<<" : "<<x<<" "<<#y<<" : "<<y<<endl<<flush;
#define DB3(x,y,z) cerr<<#x<<" : "<<x<<" "<<#y<<" : "<<y<<" "<<#z<<" : "<<z<<endl<<flush;
#define DBAR(arr,a,b) cout<<#arr<<" : ";FOR(dbar,a,b) cerr<<arr[dbar]<<" ";cerr<<endl;
#define DBAR2(arr,a,b,x,y) cout<<#arr<<endl;FOR(dbar,a,b){ FOR(dbar2,x,y)cerr<<arr[dbar][dbar2]<<" ";cerr<<endl;}
#define INF 1<<30

/*======================================Templates Ends========================*/
/* Main Code Starts from here */
int main()
{
		freopen("A-large.in","r",stdin);
		freopen("output.txt","w",stdout);

	int t,j,i,k,p,dots,fla;
	char s[10][10];
	scanf("%d",&t);
	t=t+1;
	string dummy,s1[5];
	getline(cin,dummy);
	for(p=1;p<=t;p++)
	{
		
		 dots=0; fla=0;
		int x_r[5],o_r[5],t_r[5],x_c[5],o_c[5],t_c[5],x_d1=0,o_d1=0,t_d1=0,x_d2=0,o_d2=0,t_d2=0;
		for(i=1;i<=5;i++)
		{
			x_r[i]=0; o_r[i]=0; t_r[i]=0; x_c[i]=0; o_c[i]=0; t_c[i]=0; 
		}
		for(i=1;i<=4;i++)
		{
			cin>>s1[i];
		}
		for(i=1;i<=4;i++)
		{
			for(j=0;j<4;j++)
			{
				s[i][j+1]=s1[i][j];
				if(s[i][j+1]=='X')
				x_r[i]++;
				else if(s[i][j+1]=='O')
				o_r[i]++;
				else if(s[i][j+1]=='T')
				t_r[i]++;
				else if(s[i][j+1]=='.')
				dots++;
			}
		}
	
/*		for(i=1;i<=4;i++)
		{
			for(j=1;j<=4;j++)
			{
				cout<<s[i][j];
			}cout<<endl;
		}*/
		for(j=1;j<=4;j++)
		{
			for(i=1;i<=4;i++)
			{
				if(s[i][j]=='X')
				x_c[j]++;
				else if(s[i][j]=='O')
				o_c[j]++;
				else if(s[i][j]=='T')
				t_c[j]++;
			}
		}
	
		for(i=1;i<=4;i++)
		{
			for(j=1;j<=4;j++)
			{
				if(i==j)
				{
					if(s[i][j]=='X')
					x_d1++;
					else if(s[i][j]=='O')
					o_d1++;
					else if(s[i][j]=='T')
					t_d1++;
				}
				if(i+j==5)
				{
					if(s[i][j]=='X')
					x_d2++;
					else if(s[i][j]=='O')
					o_d2++;
					else if(s[i][j]=='T')
					t_d2++;
				}
			}
		}
		int fl=0;
		for(i=1;i<=4;i++)
		{
			if((x_r[i]==4 || (x_r[i]==3 && t_r[i]==1))&&fl==0)
			{ printf("Case #%d: X won\n",p); fla=1;fl=1; }
			else if((o_r[i]==4 || (o_r[i]==3 && t_r[i]==1))&&fl==0)
			{ printf("Case #%d: O won\n",p); fla=1; fl=1; }
			else if((x_c[i]==4 || (x_c[i]==3 && t_c[i]==1))&&fl==0)
			{ printf("Case #%d: X won\n",p); fla=1;fl=1; }
			else if((o_c[i]==4 || (o_c[i]==3 && t_c[i]==1))&&fl==0)
			{ printf("Case #%d: O won\n",p); fla=1;fl=1; }
		}
		if((x_d1==4 || (x_d1==3 && t_d1==1))&&fl==0)
		{ printf("Case #%d: X won\n",p); fla=1; }
		else if((o_d1==4 || (o_d1==3 && t_d1==1))&&fl==0)
		{ printf("Case #%d: O won\n",p); fla=1; }
		
		else if((x_d2==4 || (x_d2==3 && t_d2==1))&&fl==0)
		{ printf("Case #%d: X won\n",p); fla=1; }
		else if((o_d2==4 || (o_d2==3 && t_d2==1))&&fl==0)
		{ printf("Case #%d: O won\n",p); fla=1; }
		
		else if(dots>0 && fla==0&&fl==0)
		printf("Case #%d: Game has not completed\n",p);
		else if(dots==0 && fla==0&&fl==0) 
		printf("Case #%d: Draw\n",p);
					
		
	}
	return 0;
}
