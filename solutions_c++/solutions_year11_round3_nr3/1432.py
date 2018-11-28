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
#define LL  int
using namespace std;
int main()
{
 	freopen("in.i","r",stdin);
    freopen("out.out","w",stdout);
    int count=1;
    TC
    {
    	LL a,b,c;
    	cin >> a >> b >> c;
    	vector<LL>arr;
    	LL jj;
    	REP(i,a)
    	{
    		cin >> jj;
    		arr.PB(jj);
    	}
    	LL last=-1,las=0;
    	//REP(m,arr.size()) cout << arr[m]<<" ";
    	for(int i=b;i<=c;i++)
    	{
    		las=0;
    		for(int j=0;j<arr.size();j++)
    		{
    			if(arr[j]%i ==0 || i%arr[j] ==0)
    			{
    				las++;
    			}
    		}
    		if(las==a)
    		{
    			last=i;
    		  	break;
    		}
    	}
    	if(last>=b && last<=c)	
			cout <<"Case #"<<count <<": "<<last<<"\n";
		else
			cout <<"Case #"<<count <<": "<<"NO"<<"\n";
		count++;
			
	}
}
