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
	int t,tc,n,m,area;
	
	int a,b,c,d,e,f;
	int n1,n2;
	int z;
	scanf("%d",&tc);
	
	for(t=1;t<=tc;++t)
	{
		scanf("%d %d %d",&n,&m,&area);
		bool ok=true;
		
		printf("Case #%d: ",t);
		for(a=0;a<=n && ok;++a)
			for(b=0;b<=m && ok;++b)
				for(c=0;c<=n && ok;++c)
				{
					if((c-a)==0)
						continue;
					for(d=0;d<=m && ok;++d)
						for(e=0;e<=n && ok;++e)
						{
						
							z=(d-b)*(e-a);
							n1=area+z;
							n2=-area+z;
							if(n1%(c-a)==0)
							{
								f=n1/(c-a)+b;
								if(f>=0 && f<=m)
								{
									printf("%d %d %d %d %d %d\n",a,b,c,d,e,f);
									ok=false;
								}
							}
							if(!ok)
								break;
							if(n2%(c-a)==0)
							{
								f=n2/(c-a)+b;
								if(f>=0 && f<=m)
								{
									printf("%d %d %d %d %d %d\n",a,b,c,d,e,f);
									ok=false;
								}
							}
						}
				}		
		if(ok)
			puts("IMPOSSIBLE");
	}
	
	return 0;
}
