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
void mytimer(string task){
#ifdef __ASD__
	static LARGE_INTEGER prev;	LARGE_INTEGER cur,freq;	QueryPerformanceCounter(&cur);	QueryPerformanceFrequency(&freq);	if(task!="")		cout<<task<<" took "<<(cur.QuadPart-prev.QuadPart)*1.0/freq.QuadPart<<endl;	prev=cur;
#endif
}

lng gcd(lng a,lng b){
	return a?gcd(b%a,a):b;
}

bool solve(lng n,lng pd,lng pg){
	if(!pg)
		if(pd)
			return false;
		else
			return true;
	if(pg==100)
		if(pd==100)
			return true;
		else
			return false;
	return n>=100/gcd(pd,100);
}

int main(){
#ifdef __ASD__
    freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);
#endif

	int tc;
	cin>>tc;
	forn(qq,tc){
		lng n,pd,pg;
		cin>>n>>pd>>pg;
		cout<<"Case #"<<qq+1<<": ";
		if(solve(n,pd,pg))
			cout<<"Possible\n";
		else
			cout<<"Broken\n";
	}

    return 0;
}
