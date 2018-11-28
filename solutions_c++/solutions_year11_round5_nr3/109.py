#include <vector>
#include <cstring>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <queue>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <stdlib.h>
#include <ctime>
#include <string>
#include <complex>
#ifdef __ASD__
#include <windows.h>
#endif
using namespace std;
#define all(a) a.begin(),a.end()
#define forn(i,n) for(int i=0;i<(n);++i)
#define fornn(i,n) for(i=0;i<(n);++i)
#define lng long long
#define SQ(a) ((a)*(a))
#define forv(i,v) for(int i=0;i<(int)v.size();++i)
#define mp make_pair
#define pb push_back
#define ABS(a) ((a)<0?-(a):(a))
#define iinf 1000000000
#define left asdleft
#define prev asdprev
#define eps 1e-10
#define y1 asdy1
#define y2 asdy2
#define EQ(a,b) abs((a)-(b))<eps
void mytimer(string task){
#ifdef __ASD__
	static LARGE_INTEGER prev;	LARGE_INTEGER cur,freq;	QueryPerformanceCounter(&cur);	QueryPerformanceFrequency(&freq);	if(task!="")		cout<<task<<" took "<<(cur.QuadPart-prev.QuadPart)*1.0/freq.QuadPart<<endl;	prev=cur;
#endif
}

char src[10][10];
bool flip[10][10];
bool was[10][10];
int dx[256],dy[256];
int n,m;

bool check(){
	forn(i,n)
		forn(j,m)
			was[i][j]=false;
	forn(i,n){
		forn(j,m){
			int x=dx[src[i][j]];
			int y=dy[src[i][j]];
			if(flip[i][j])
				x=-x,y=-y;
			int a=(i+y+n)%n;
			int b=(j+x+m)%m;
			if(was[a][b])
				return false;
			was[a][b]=true;
		}
	}
	return true;
}

void solve(){
	dx['|']=0;
	dy['|']=1;

	dx['-']=1;
	dy['-']=0;

	dx['/']=1;
	dy['/']=-1;

	dx['\\']=1;
	dy['\\']=1;

	cin>>n>>m;
	gets(src[0]);
	forn(i,n)
		gets(src[i]);
	int res=0;
	forn(mm,1<<(n*m)){
		forn(i,n)
			forn(j,m)
				flip[i][j]=!!(mm&(1<<(m*i+j)));
		if(check())
			++res;
	}
	cout<<res<<endl;
}

int main(){
#ifdef __ASD__
    freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);
#endif

	int tc;
	cin>>tc;
	forn(qqq,tc){
		cout<<"Case #"<<qqq+1<<": ";
		solve();
	}

    return 0;
}
