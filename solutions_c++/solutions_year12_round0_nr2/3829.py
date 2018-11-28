#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

#define PB push_back
#define MP make_pair

#define REP(i,n) for(i=0;i<(n);++i)
#define FOR(i,l,h) for(i=(l);i<=(h);++i)
#define FORD(i,h,l) for(i=(h);i>=(l);--i)

typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef long long LL;
typedef pair<int,int> PII;
int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	int T,N,S,P;
	cin>>T;
	for(int i=1;i<=T;++i)	
	{
		printf("Case #%d: ",i);
		cin>>N>>S>>P;
		int ans=0;
		while(N--)
		{
			int temp;
			cin>>temp;
			int quo=temp/3,remain=temp%3;
			if(remain==0)
			{
				if(quo>=P) ans++;
				else
				{
					if(quo<P-1) continue;
					else
					{
						if(S>0&&quo>=1&&quo<=9)
						{
							S--;
							ans++;
						}
					}
				}
			}
			else if(remain==1)
			{
				if(quo+1>=P) ans++;
			}
			else
			{
				if(quo+1>=P) ans++;
				else
				{
					if(quo+1<P-1) continue;
					else
					{
						if(S>0&&quo+2<=10)
						{
							S--;
							ans++;
						}
					}
				}
			}
		}
		cout<<ans<<endl;
	}

	//system("pause");
	return 0;
}