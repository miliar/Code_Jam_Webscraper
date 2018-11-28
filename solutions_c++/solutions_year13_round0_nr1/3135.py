#include <algorithm>
#include <functional>
#include <numeric>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cassert>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <sstream>
using namespace std;

#define LL long long
#define LD long double
#define PR pair<int,int>

#define For(i,n) for (i=0; i<int(n); i++)
#define ForR(i,n) for (i=int(n)-1; i>=0; i--)
#define Sz(s) int((s).size())
#define All(s) (s).begin(),(s).end()
#define Fill(s,v) memset(s,v,sizeof(s))
#define pb push_back
#define mp make_pair
#define x first
#define y second

template<typename T> T Abs(T x) { return(x < 0 ? -x : x); }
template<typename T> T Sqr(T x) { return(x*x); }

const int INF = (int)1e9;
const LD EPS = 1e-9;
const LD PI = acos(-1.0);

#define DEBUG 0
#define LIMN 2000
#define LIMA 250
char input[4][9];
int sx[]={0,0};
int sy[]={0,3};
int dx[]={1,1};
int dy[]={1,-1};
bool is_ok_for(char test,int x,int y,int cx,int cy)
{
	bool res=true;
	for(int i=0;i<4;i++)
	{
		char c=input[x][y];
		if((c!=test)&&(c!='T'))
		{
			res=false;
			break;
		}
		x+=cx;
		y+=cy;
	}
	return res;
}
bool is_ok(char test)
{
	//bool res=false;
	for(int i=0;i<4;i++)
	{
		bool temp=is_ok_for(test,i,0,0,1);
		if(temp){
			return true;
		}
		temp=is_ok_for(test,0,i,1,0);
		if(temp){
			return true;
		}
	}
	bool temp=is_ok_for(test,0,0,1,1);
	if(temp) return true;
	temp=is_ok_for(test,0,3,1,-1);
	if(temp) return true;
	return false;
}
int main()
{
	//files
	freopen("in.txt","r",stdin);
		if (!DEBUG)
			freopen("out.txt","w",stdout);
	//vars
	int tt,TT;
	//testcase loop
	scanf("%d",&TT);
		For(tt,TT)
		{
			//init
			printf("Case #%d: ",tt+1);
			//input
			bool complete=true;
			for(int i=0;i<4;i++){
				scanf("%s",&input[i]);
				for(int j=0;j<4;j++)
				{
					if(input[i][j]=='.') complete=false;
				}
			}
			bool winx=is_ok('X');
			bool wino=is_ok('O');
			if(winx)
			{
				printf("X won\n");
				continue;
			}
			if(wino)
			{
				printf("O won\n");
				continue;
			}
			if(complete)
			{
				printf("Draw\n");
			}else
			{
				printf("Game has not completed\n");
			}
		}
	return(0);
}