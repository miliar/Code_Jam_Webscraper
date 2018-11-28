/*
	Author : ChnLich
*/
#include<cstdio>
#include<cmath>
#include<iomanip>
#include<cstring>
#include<cstdlib>
#include<ctime>
#include<iostream>
#include<sstream>
#include<fstream>
#include<algorithm>
#include<vector>
#include<list>
#include<stack>
#include<queue>
#include<deque>
#include<set>
#include<map>
#include<string>
#include<bitset>
#include<functional>
#include<utility>

using namespace std;

typedef long long llint;
typedef pair<int,int> ipair;
typedef unsigned int uint;
#define pb push_back
#define fi first
#define se second
#define mp make_pair

const int MOD=1000000007,dx[]={0,1,0,-1},dy[]={1,0,-1,0};
const double eps=1e-8;

void read(int &k)
{
	k=0; char x=getchar();
	while(x<'0'||x>'9') x=getchar();
	while(x>='0'&&x<='9') { k=k*10-48+x; x=getchar(); }
}

int T,win;
char s[10][10],x[10];

int check(char x0,char x1,char x2,char x3)
{
	x[0]=x0; x[1]=x1; x[2]=x2; x[3]=x3;
	sort(x,x+4);
	for(int i=0;i<4;i++) if (x[i]=='.') return 0;
	if (x[1]=='T') return 0;
	if (x[0]=='T')
	{
		for(int i=2;i<4;i++) if (x[i]!=x[1]) return 0;
		if (x[1]=='X') win=1; else win=-1;
		return 1;
	} else
	{
		for(int i=1;i<4;i++) if (x[i]!=x[0]) return 0;
		if (x[1]=='X') win=1; else win=-1;
		return 1;
	}
}

int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	scanf("%d",&T);
	for(int tt=1;tt<=T;tt++)
	{
		win=0;
		printf("Case #%d: ",tt);
		for(int i=0;i<4;i++) scanf("%s",s[i]);
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++) if (s[i][j]=='O') s[i][j]='Y';
		for(int i=0;i<4;i++)
		{
			check(s[i][0],s[i][1],s[i][2],s[i][3]);
			check(s[0][i],s[1][i],s[2][i],s[3][i]);
		}
		check(s[0][0],s[1][1],s[2][2],s[3][3]);
		check(s[0][3],s[1][2],s[2][1],s[3][0]);
		if (win==1) printf("X won\n"); else if (win==-1) printf("O won\n");
		else
		{
			int tot=0;
			for(int i=0;i<4;i++)
				for(int j=0;j<4;j++) if (s[i][j]=='.') tot++;
			if (tot) puts("Game has not completed"); else puts("Draw");
		}
	}
	
	return 0;
}
