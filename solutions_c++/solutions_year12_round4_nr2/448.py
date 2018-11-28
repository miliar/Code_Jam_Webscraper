//SkyHawk, CMC MSU

#include <stdio.h>
#include <iostream>
#include <list>
#include <string>
#include <vector>
#include <iterator>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <set>

using namespace std;

#define FOR(i,n) for(int i = 0;i < n;++i)
#define PII pair<int,int>
#define EPS 1e-9

typedef long double LD;

pair<int,int> r[1010];
int ansx[1010];
int ansy[1010];
int resx[1010];
int resy[1010];
int p;

void solve(int w,int l,int x,int y)
{
	if(p<0)
		return;
	ansx[p] = x;
	ansy[p] = y;
	int rbig = r[p].first;
	--p;
	if(p<0)
		return;
	if(l>=rbig+r[p].first)
		solve(0,l-r[p].first-rbig,x,y+r[p].first+rbig);
	if(p<0)
		return;
	if(w>=rbig+r[p].first)
		solve(w-r[p].first-rbig,0,x+r[p].first+rbig,y);
	if(p<0)
		return;
	if(l>=rbig+r[p].first && w>=rbig+r[p].first)
		solve(w-r[p].first-rbig,l-r[p].first-rbig,x+r[p].first+rbig,y+r[p].first+rbig);
}

int main(int argc, char** argv)
{
	freopen("B-small.in","r",stdin);
	freopen("B-small.out","w",stdout);
	int t;
	cin >> t;
	FOR(count,t)
	{
		int n;
		int w,l;
		cin >> n >> w >> l;
		FOR(i,n)
		{
			//cerr << "#";
			cin >> r[i].first;
			r[i].second = i;
		}
		sort(r,r+n);
		p = n-1;
		solve(w,l,0,0);
		if(p>=0)
			cerr << "Ololo!" << endl;
		printf("Case #%d: ",count+1);
		FOR(i,n)
		{
			resx[r[i].second] = ansx[i];
			resy[r[i].second] = ansy[i];
		}
		FOR(i,n)
			printf("%d %d ",resx[i],resy[i]);
		printf("\n");
	}
	return 0;
}
