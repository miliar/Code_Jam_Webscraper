//#include "stdafx.h"

#include <algorithm> 
#include <cctype> 
#include <cmath> 
#include <cstdio> 
#include <cstdlib> 
#include <cstring> 
#include <deque> 
#include <iostream> 
#include <list> 
#include <map> 
#include <numeric> 
#include <queue> 
#include <set> 
#include <sstream> 
#include <stack> 
#include <string> 
#include <vector>

using namespace std; 

#define fo(i,j,n) for(i=j;i<n;++i)
#define Fo(i,j,n) for(i=n-1;i>=j;--i)
#define foo(i,j,v) fo(i,j,sz(v))
#define Foo(i,j,v) Fo(i,j,sz(v))
#define li(v) v.begin(),v.end()
#define sz(v) ((int)v.size())
#define CLR(a,v) memset((a),(v),sizeof(a))
#define inf 1000000001
//typedef long long Long;
typedef __int64 Long;
#define pi (2*acos(0))
#define eps 1e-9

#define two(X) (1<<(X))
#define twoL(X) (((Long)(1))<<(X))
#define contain(S,X) (((S)&two(X))!=0)
#define containL(S,X) (((S)&twoL(X))!=0)

char BUFFER[1000000 + 5];
bool readn(int &n)	{ return scanf("%d",&n) == 1; } 
bool readl(Long &n)	{ return scanf("%I64d",&n) == 1; } 
bool readd(double &n){ return scanf("%lf",&n) == 1; } 
bool reads(string &s){ s = ""; int n = scanf("%s",BUFFER); if(n == 1)s = BUFFER; return n == 1; }
bool readln(string &s){ char *valid = gets(BUFFER); if(valid)s = BUFFER; return ((bool)valid); }

int rowX[4], rowO[4], colX[4], colO[4], DiagX1, DiagX2, DiagO1, DiagO2;

string board[4];

int main()
{
	freopen("D://input.in","r",stdin);
	freopen("D://out.in","w",stdout);
	int t = 0;	
	
	bool anyDot =false; int j,k;
	char ch;

	cin>>t;

	for(int i=0;i<t;i++)
	{		
		anyDot =false; CLR(rowX,0); CLR(rowO,0); CLR(colX,0); CLR(colO,0);  DiagX1 = DiagX2 =  DiagO1 = DiagO2 = 0;

		for(j=0;j<4;j++)cin >> board[j];
		
		for(j=0;j<4;j++)
		{
			for(k=0;k<4;k++)
			{
				//cin >> ch;
				ch = board[j][k];

				if(ch=='X') 
				{
					rowX[j]++;
					colX[k]++;
					if(j == k) DiagX1++;
					else if((j+k) == 3) DiagX2++;
				}
				else if(ch == 'O')
				{
					rowO[j]++;
					colO[k]++;
					if(j == k) DiagO1++;
					else if((j+k) == 3) DiagO2++;
				}
				else if(ch == 'T')
				{
					rowX[j]++;
					colX[k]++;
					rowO[j]++;
					colO[k]++;

					if(j == k){ DiagX1++;DiagO1++;}
					else if((j+k) == 3){ DiagX2++;DiagO2++;}
				}
				else if(ch == '.')
				{
					anyDot = true;
				}
			}
		}
		
		printf("Case #%d: ",i+1);
		//cout<<"Case #"<<i+1<<": ";

		if( rowX[0] == 4 || rowX[1] == 4 || rowX[2] == 4 || rowX[3] == 4 ||
			colX[0] == 4 || colX[1] == 4 || colX[2] == 4 || colX[3] == 4 ||
			DiagX1 == 4 || DiagX2 == 4)
		{ cout<<"X won\n";}
		else if( rowO[0] == 4 || rowO[1] == 4 || rowO[2] == 4 || rowO[3] == 4 ||
				 colO[0] == 4 || colO[1] == 4 || colO[2] == 4 || colO[3] == 4 ||
				 DiagO1 == 4 || DiagO2 == 4)
		{ cout<<"O won\n";}
		else if(anyDot) { cout<<"Game has not completed\n";}
		else{ cout<<"Draw\n";}

		/*anyDot =false;
		
		for(int i=0;i<4;i++)
		{
			rowX[i] = 0; rowO[i] = 0; colX[i] = 0; colO[i] = 0;			
		}
		DiagX1 = DiagX2 =  DiagO1 = DiagO2 = 0;
		*/
	}

	//printf("\n");
	return 0;
} 

