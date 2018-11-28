#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
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
#include <string>
#include <cstring>
#include <cctype>
#include <assert.h>
using namespace std;

#define forn(i,n) for(int i=1;i<=n;i++)
#define Min(a,b) ((a)<(b)?(a):(b))


int t,n;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	while(scanf("%d",&t)!=EOF)
	{
		forn(tcase,t)
		{
			scanf("%d",&n);
			int ans=0;
			int ol=1,or=1,bl=1,br=1;
			forn(i,n)
			{
				char c;
				int cc;
				cin>>c>>cc;
				int temp=0;
				if(c=='O')
				{
					if(ol<=cc && or>=cc)
					{
						ans++;
						ol=or=cc;
						bl--;
						br++;
					}
					else
					{
						temp=Min(abs(ol-cc),abs(or-cc))+1;
						ans+=temp;
						ol=or=cc;
						bl=bl-temp;
						br=br+temp;
						
					}
						if(bl<1)
							bl=1;
						if(br>100)
							br=100;
				}
				else
				{
					if(bl<=cc && br>=cc)
					{
						ans++;
						bl=br=cc;
						ol--;
						or++;
					}
					else
					{
						temp=Min(abs(bl-cc),abs(br-cc))+1;
						ans+=temp;
						bl=br=cc;
						ol=ol-temp;
						or=or+temp;
					}
					if(ol<1)
						ol=1;
					if(or>100)
						or=100;
				}
//				cout<<"ans= "<<ans<<"  bl= "<<bl<<"  br= "<<br<<"  ol= "<<ol<<"  or= "<<or<<"  temp= "<<temp<<endl;
			}
			printf("Case #%d: %d\n",tcase,ans);
		}
	}
	return 0;
}