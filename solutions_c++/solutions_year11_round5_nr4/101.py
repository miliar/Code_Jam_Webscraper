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

string src;
vector<lng> res;
vector<lng> bits;
int n;

bool square(lng v){
	lng s=(lng)sqrt((double)v);
	while(SQ(s)>v)
		--s;
	while(SQ(s)<v)
		++s;
	return SQ(s)==v;
}

void doit(int a,lng v){
	if(a==n){
		if(square(v))
			res.pb(v);
		return;
	}
	doit(a+1,v);
	doit(a+1,v+bits[a]);
}

void solve(){
	cin>>src;
	n=src.length();

	res.clear();
	bits.clear();

	lng val=0;
	forn(i,n){
		if(src[i]=='?')
			bits.pb(1LL<<(n-1-i)),
			val*=2;
		else
			val=val*2+src[i]-'0';
	}

	n=bits.size();

	doit(0,val);

	if(res.size()!=1)
		exit(123);
	lng r=res[0];
	forn(i,src.length())
		cout<<((res[0]&(1LL<<(src.length()-1-i)))!=0);
	cout<<endl;
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
