// Author -Swarnaprakash.U
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

const bool debug=true;

#define SET(x,v)	memset(x,v,sizeof(x))
#define ALL(x) 		(x).begin() , (x).end()
#define PB 			push_back
#define SZ(x)		((int)((x).size()))
#define TR(i,x) 	for(i=0;i<(x).size();++i)
#define DB(x) 		if(debug) cout << #x << " : " << x <<endl;
#define HELLO		if(debug) puts("hello");
#define LL 			long long
#define INF			100000000
#define M			105


int main()
{
	LL t,a,b,c,d,m,n,tc;
	LL x[M],y[M];
	
	cin>>tc;
	for(t=1;t<=tc;++t)
	{
		cin>>n>>a>>b>>c>>d>>x[0]>>y[0]>>m;
		int i,j,k;
		for(i=1;i<n;++i)
		{
			x[i]=((LL)a*x[i-1]+b)%m;
			y[i]=((LL)c*y[i-1]+d)%m;
			
		}
		int ans=0;
		for(i=0;i<n;++i)
			for(j=i+1;j<n;++j)
				for(k=j+1;k<n;++k)
				{
					int cx,cy;
					cx=x[i]+x[j]+x[k];
					cy=y[i]+y[j]+y[k];
					if(cx%3==0 && cy%3==0)
						++ans;
				}
		cout<<"Case #"<<t<<": ";
		cout<<ans<<endl;
	}
	return 0;
}
