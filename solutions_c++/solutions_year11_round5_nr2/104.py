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

int ar[100000];

void solve(){
	memset(ar,0,sizeof(ar));
	int n;
	cin>>n;
	forn(i,n){
		int a;
		cin>>a;
		++ar[a];
	}
	vector<int> szs;
	int res=iinf;
	forn(i,11000){
		if(!ar[i]&&!szs.size())
			continue;
		vector<int> nu;
		if(ar[i]>=szs.size()){
			int t=ar[i]-szs.size();
			forn(j,t)
				szs.pb(0);
			sort(all(szs));
		}else{
			res=min(res,szs[ar[i]]);
			szs.erase(szs.begin()+ar[i],szs.end());
		}
		forv(j,szs)
				++szs[j];
	}

	if(res==iinf)
		cout<<0<<endl;
	else
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
