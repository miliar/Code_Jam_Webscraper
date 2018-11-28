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
	long long N,P,K,L,ans,tmp;
	VI v;
	cin>>N;
	FOR(kk,0,N)
	{
		cin>>P>>K>>L;
		ans=0;
		v.clear();
		FOR(i,0,L)
		{
			cin>>tmp;
			v.PB(tmp);
		}
		sort(ALL(v));
		long long k=0;
		long long mn=1;
		for(int i=L-1;i>=0;i--)
		{
			k++;
			ans+=(mn*v[i]);
			if(k==K)
			{
				k=0;
				mn++;
			}
			
		}
		
		cout<<"Case #"<<kk+1<<": "<<ans<<endl; 
	}

	return 0;
}
