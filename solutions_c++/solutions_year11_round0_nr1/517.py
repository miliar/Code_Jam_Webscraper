#define mset(a) memset(a,0,sizeof(a))

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>

using namespace std;

int main()
{
int t;
cin>>t;
for(int tt=1;tt<=t;tt++)
{
	vector<int>o,b,r;
	int n;
	cin>>n;
	while(n--)
	{
		int m;char c;
		cin>>c>>m;
		if(c=='O')
		{o.push_back(m);
			r.push_back(1);
		}
		else{ b.push_back(m);
			r.push_back(0);}
	}
	int ans=0;
	int p1=1,p2=1,i=0,j=0,x=0;
	while(1)
	{
		ans++;
		int d1,d2;
		bool bbb=false;
		if(i<o.size())
		{
			if(p1<o[i])p1++;
			else if (p1>o[i])p1--;
			else if(r[x]){i++;x++;bbb=1;}
		}
		if(j<b.size())
		{
			if(p2<b[j])p2++;
			else if(p2>b[j])p2--;
			else if(!r[x]&&!bbb){j++;x++;}
		}
		//printf("round%d:%d,%d\n",ans,p1,p2);
		if(x>=r.size())
			break;
	}
	printf("Case #%d: %d\n",tt,ans);

}
return 0;
}
