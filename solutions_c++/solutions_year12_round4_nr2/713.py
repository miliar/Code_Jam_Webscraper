#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;
typedef long long LL;
const int MAXN=10000;
const int TEST=100;
LL r[MAXN+10];
LL X[MAXN+10],Y[MAXN+10];
int n,h,w;
void ReadIn()
{
	scanf("%d%d%d",&n,&w,&h);
	for (int i=0;i<n;i++) scanf("%lld",&r[i]);
}
LL getRand(const LL &RANGE)
{
	return (LL)rand()*rand()%(RANGE+1);
}
inline LL getSqr(LL x)
{
	return x*x;
}
bool cross(LL x,LL y,int now)
{
	for (int i=0;i<now;i++)
		if (getSqr(x-X[i])+getSqr(y-Y[i])<getSqr(r[i]+r[now])) return false;
	return true;
}
bool DFS(int now)
{
	if (now==n) {
		for (int i=0;i<n;i++)
			printf(" %lld %lld",X[i],Y[i]);
		puts("");
		return true;
	}
	for (int i=0;i<TEST;i++) {
		LL x=getRand(w), y=getRand(h);
		if (cross(x,y,now)) {
			X[now]=x,Y[now]=y;
			if (DFS(now+1)) return true;
		}
	}
	DFS(now-1);
}
int main()
{
	srand((unsigned)time(NULL));
	int cases;
	scanf("%d",&cases);
	for (int c=1;c<=cases;c++) {
		ReadIn();
		printf("Case #%d:",c);
		DFS(0);
	}
	return 0;
}
