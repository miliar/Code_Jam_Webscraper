#include <iostream>
#include <cmath>
#include <algorithm>
#include <limits>
#include <vector>
#include <bitset>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <time.h>
#include <map>
#include <stack>
#include <string>
#include <climits>
#include <ctime>
#include <fstream>
#include <sstream>
using namespace std;
#define LL long long
#define ULL unsigned long long
#define LD long double
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)<(b)?(a):(b))
#define ABS(x) ((x)<0?-(x):(x))
#define si(n) scanf("%d",&n)
#define sf(n) scanf("%f",&n)
#define ss(n) scanf("%s",n)
#define pnl printf("\n")
#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define FORR(i,n) for(int i=(n);i>=0;i--)
#define DB(x) cout<<"\n"<<#x<<" = "<<(x)<<"\n";
#define CL(a,b) memset(a,b,sizeof(a))
#define GOLD ((1+sqrt(5))/2)
const double PI=3.14159265358979323846264338327950288419716939937510582097494459230;
void swaps (char *x,char *y){char temp;temp=*x;*x=*y;*y=temp;}
void swapi(int *a,int *b){int temp;temp=*a;*a=*b;*b=temp;}
ULL gcd(ULL a,ULL b){if(a==0)return b;if(b==0)return a;if(a==1||b==1)return 1;
if(a==b)return a;if(a>b)return gcd(b,a%b);else return gcd(a,b%a);}
char x[10][10];
int main()
{
    int t;
    si(t);
    string str;
    int O = 0 ,X = 0;
    int Complete;
    bool OFlag,XFlag;
    FOR(k,1,t+1)
    {
	    OFlag = false,XFlag = false;
	    O = 0,X = 0;
	    Complete = 0;
	    FOR(i,0,4)
	    {
		    cin>>str;
		    FOR(j,0,4)
		    {
			    x[i][j] = str[j];
		    }
	    }
	    cout<<"Case #"<<k<<": ";
	    FOR(i,0,4)
	    {
		    O = 0,X = 0;
		    FOR(j,0,4)
		    {
			    if(x[i][j]=='O')
				    O+=1;
			    if(x[i][j]=='X')
				    X+=1;
			    if(x[i][j]=='T')
			    {
				    O+=1;
				    X+=1;
			    }
			    if(x[i][j]=='.')
				    Complete = 1;
		    }
		    if(O==4)
			    OFlag = true;
		    if(X==4)
			    XFlag = true;
	    }
	    if(OFlag)
	    {
		    cout<<"O won"<<endl;
		    continue;
	    }
	    if(XFlag)
	    {
		    cout<<"X won"<<endl;
		    continue;
	    }
	    O = 0,X = 0;
	    FOR(j,0,4)
	    {
		    O = 0;
		    X = 0;
		    FOR(i,0,4)
		    {
			    if(x[i][j]=='O')
				    O+=1;
			    if(x[i][j]=='X')
				    X+=1;
			    if(x[i][j]=='T')
			    {
				    O+=1;
				    X+=1;
			    }
			    if(x[i][j]=='.')
				    Complete = 1;
		    }
		    if(O==4)
			    OFlag = true;
		    if(X==4)
			    XFlag = true;
	    }
	    if(OFlag)
	    {
		    cout<<"O won"<<endl;
		    continue;
	    }
	    if(XFlag)
	    {
		    cout<<"X won"<<endl;
		    continue;
	    }
	    O = 0,X = 0;
	    for(int i=0,j=0;i<4&&j<4;i++,j++)
	    { 
		    if(x[i][j]=='O')
			    O+=1;
		    if(x[i][j]=='X')
			    X+=1;
		    if(x[i][j]=='T')
		    {
			    O+=1;
			    X+=1;
		    }
	    }
	    if(O==4)
	    {
		    cout<<"O won"<<endl;
		    continue;
	    }
	    if(X==4)
	    {
		    cout<<"X won"<<endl;
		    continue;
	    }
	    O = 0,X = 0;
	    for(int i=3,j=0;i>=0&&j<4;i--,j++)
	    { 
		    if(x[i][j]=='O')
			    O+=1;
		    if(x[i][j]=='X')
			    X+=1;
		    if(x[i][j]=='T')
		    {
			    O+=1;
			    X+=1;
		    }
	    }
	    if(O==4)
	    {
		    cout<<"O won"<<endl;
		    continue;
	    }
	    if(X==4)
	    {
		    cout<<"X won"<<endl;
		    continue;
	    }
	    if(Complete)
		    cout<<"Game has not completed"<<endl;
	    else
		    cout<<"Draw"<<endl;

    }
    return 0;
}

