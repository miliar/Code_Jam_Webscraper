#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <cstdio>
#include <string>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <string.h>
#include <cassert>

using namespace std;

#define GI ({int t;scanf("%d",&t);t;})
#define FOR(i,a,b) for(int i=a;i<b;i++)
#define REP(i,n) FOR(i,0,n)
#define pb push_back
#define sz size()
#define INF (int)1e9

typedef long long LL;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<vector<int> > VVI;
typedef pair<int,int> PII;

main()
{
	int testcases,n,l,h,i,j,mammy,m;
	long long a[10001];
	scanf("%d",&testcases);
    for(int tc=1;tc<=testcases;tc++)	{
		scanf("%d %d %d",&n,&h,&l);
        
		for(i=0;i<n;++i)
			cin>>a[i];
            for(i=l;i<=h;++i)
		{
			mammy=0;
			for(j=0;j<n;++j)
				if(i%a[j] && a[j]%i)
					mammy=1;
			if(!mammy)
				break;
		}
		
		printf("Case #%d: ",tc);

		if(!mammy)
			cout<<i<<endl;

		else
			cout<<"NO"<<endl;
	}
    return 0;
}
