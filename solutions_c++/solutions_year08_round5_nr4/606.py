#include <iostream>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <sstream> 
#include <cmath>
#include <cstring>

using namespace std;

#define pb push_back
#define mp make_pair
#define PII pair<int,int> 
#define A first
#define B second
#define PIII pair<int,PII> 

#define I(x,y) x <y> :: iterator 
#define set(a,c) memset(a,c,sizeof(a))

#define REP(i,n) for(int i=0;i<n;i++)
typedef unsigned long long LL;
LL reach [101][101];
int done[101][101];
int rock[101][101];
int MOD = 10007;
LL f(int x,int y){
	if(x<1 || y <1)
		return 0;
	LL &res = reach[x][y];
	if(done[x][y])
		return res;
	done[x][y] = 1;
	if(rock[x][y])
		res = 0 ;
	else
	res = (f(x-2,y-1) + f(x-1,y-2))%MOD;
	//cout<<"f("<<x<<","<<y<<") : "<<res<<endl;
	return res;
}

typedef unsigned long long LLU;
typedef long double LD;
int h,w,r;
int main()
{
	int KASES;
	int x,y;
	scanf("%d",&KASES);
	for(int kases=0;kases<KASES;kases++)
	{
		printf("Case #%d: ",kases+1);
		scanf("%d %d %d",&h,&w,&r);
		set(done,0);
		set (rock,0);

		set(reach,0);
		reach[1][1] = 1;
		done [1][1] = 1;
		for(int i=0;i<r;i++)
		{
			scanf("%d %d",&x,&y);
			rock[x][y] = 1;
		}
		if(rock[1][1]==1)
			printf("0\n");
		else
		cout<<f(h,w)<<endl;
	}
}

