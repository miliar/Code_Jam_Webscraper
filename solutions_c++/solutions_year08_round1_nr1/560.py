#include "stdafx.h"
#include <iostream>
#include <cstdio>
#include <vector>
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
#include <iomanip>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <string>
using namespace std;

#define FOR(i,a,b) for(int i=(a);i<int(b);++i)
#define SZ(v) ((int)v.size())
#define FORSZ(i,a,v) FOR(i,a,SZ(v))
#define REPSZ(i,v) FORSZ(i,0,v)
#define ALL(v) (v).begin(),(v).end()
#define SS stringstream
#define VI vector<int>
#define VS vector<string>
#define PB push_back
#define SQR(x) (x)*(x)
#define FILL(A,x) memset((A),(x),sizeof(A))

int main()
{
freopen ("A-large.in","r",stdin);
freopen ("out.txt","w",stdout);
	__int64 T,N,t;
	cin>>T;
	vector<__int64> A;
	vector<__int64> B;
	__int64 ans;
	FOR(kk,0,T)
	{
		A.clear();
		B.clear();
		ans=0;
		cin>>N;
		FOR(i,0,N)
		{
			cin>>t;
			A.PB(t);
		}
		FOR(i,0,N)
		{
			cin>>t;
			B.PB(t);
		}

		sort(ALL(A));
		sort(ALL(B));
		REPSZ(i,A)
			ans+=(A[i]*B[SZ(B)-i-1]);
		cout<<"Case #"<<kk+1<<": "<<ans<<endl; 

	}
	return 0;
}
