#include<cstdio>
#include<cstring>
#include<cmath>
#include<cctype>
#include<cstdlib>
#include<cctype>

#include<iostream>
#include<vector>
#include<stack>
#include<list>
#include<queue>
#include<set>
#include<bitset>
#include<map>
#include<algorithm>

#define VI vector<int>
#define VD vector<double>
#define PII pair<int,int>
#define PDD pair<double,double>
#define VII vector<PII >
#define VDD vector<PDD >
#define STI stack<int>
#define STD stack<double>
#define STII stack<PII >
#define STDD stack<PDD >

#define pb push_back
#define pf push_front
#define clr clear
#define res resize
#define ass assign
#define fir first
#define sec second

#define For(i,a,b) for(register int i=a;i<=b;i++)
#define Dor(i,a,b) for(register int i=a;i>=b;i--)
#define Fill(a,b) memset(a,b,sizeof(a))
#define Max(a,b) (a>b?a:b)
#define Min(a,b) (a<b?a:b)

const int N=10010;
const int M=100010;
const double eps=1e-10;
const double dinf=1e10;
const int inf=1061109567;
const double Pi=3.14159265358;

using namespace std;

char s[6][6];

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int T,cas=1;
	scanf("%d",&T);
	while (cas<=T)
	{
		gets(s[4]);
		For(i,1,4) gets(s[i]+1);
		int dx=0,dy=0;
		For(i,1,4) For(j,1,4)
			if (s[i][j]=='T')
			{
				dx=i;
				dy=j;
				break;
			}
		s[dx][dy]='X';
		bool pass=0;
		For(i,1,4)
		{
			bool p=1;
			For(j,1,4) if (s[i][j]!='X') {p=0;break;}
			pass=p||pass;
		}
		For(i,1,4)
		{
			bool p=1;
			For(j,1,4) if (s[j][i]!='X') {p=0;break;}
			pass=p||pass;
		}
		{
			bool p=1;
			For(i,1,4) if (s[i][i]!='X') {p=0;break;}
			pass=p||pass;
		}
		{
			bool p=1;
			For(i,1,4) if (s[i][5-i]!='X') {p=0;break;}
			pass=p||pass;
		}
		if (pass)
		{
			printf("Case #%d: X won\n",cas++);
			continue;
		}


		s[dx][dy]='O';
		pass=0;
		For(i,1,4)
		{
			bool p=1;
			For(j,1,4) if (s[i][j]!='O')  {p=0;break;}
			pass=p||pass;
		}
		For(i,1,4)
		{
			bool p=1;
			For(j,1,4) if (s[j][i]!='O') {p=0;break;}
			pass=p||pass;
		}
		{
			bool p=1;
			For(i,1,4) if (s[i][i]!='O') {p=0;break;}
			pass=p||pass;
		}
		{
			bool p=1;
			For(i,1,4) if (s[i][5-i]!='O') {p=0;break;}
			pass=p||pass;
		}
		if (pass)
		{
			printf("Case #%d: O won\n",cas++);
			continue;
		}



		pass=1;
		For(i,1,4) For(j,1,4) if (s[i][j]=='.') pass=0;
		if (pass)
		{
			printf("Case #%d: Draw\n",cas++);
			continue;
		}



		printf("Case #%d: Game has not completed\n",cas);
		cas++;
	}
	return 0;
}
