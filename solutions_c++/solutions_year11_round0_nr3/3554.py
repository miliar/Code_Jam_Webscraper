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
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define FOR(i,a,b) for(int i=(int)a;i<(int)b;++i)
#define REP(i,n) FOR(i,0,n)
#define IT(c) __typeof((c).begin())
#define FORIT(i,c) for(IT(c) i=(c).begin();i != (c).end();++i)
#define ALL(c) (c).begin() , (c).end()
#define CLEAR(a, b) memset(a, b, sizeof(a))
#define PB push_back
#define MP make_pair
#define TC int tt;scanf("%d",&tt);while(tt--)
#define scan(a) fscanf(in,"%d",&a)
using namespace std;
int main()
{
	freopen("j.in","r",stdin);
	freopen("out.out","w",stdout);
	int count=1;
	TC
	{
		int n;
		cin>>n;
		int a[n];
		REP(i,n)
		{
			cin >> a[i];
		}
		int k=0;
		int xo;
		int sum;
		int tot = a[0];
		int tsum= a[0];
		FOR(i,1,n)
		{
		  tot   = tot ^ a[i];
		  tsum  += a[i];
		 }
	//	 cout << tsum <<" ";
		 int mx=-9999;
		REP(i,n)
		{
			for(int l=1;l<=n/2;l++)
			{
				xo=0;
				sum=0;
				if(i+l<=n)
				{
					for(int k=i;k<i+l;k++)
					{
						xo   = xo ^ a[k];
						sum += a[k];
					}
					int temp = (tot ^ (xo));
					
					int tem2 = max(sum,tsum-sum);
					if(xo == temp)
					{
						mx = max(mx,tem2);
					}
				}

			}
		}
		if(mx==-9999)
		    cout <<"Case #"<<count <<": " <<"NO"<<"\n";
		else
		    cout <<"Case #"<<count <<": " <<mx<<"\n";
	count++;
	}
}
