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
#include <string.h>

using namespace std;

#define forn(i,n) for(int i=1;i<=n;i++)
#define Min(a,b) ((a)>(b)?(b):(a))
const int pi=acos(-1.0);
const int eps=1e-11;

int n,l,c;
int t;
int a[1000005],b[1000005],d[1000005];
int main()
{
	freopen("B-small-attempt1.in","r",stdin);
	freopen("B-small-attempt1.out","w",stdout);
	int tt;
	scanf("%d",&tt);
	forn(tcase,tt)
	{
		memset(a,0,sizeof(a));
		memset(b,0,sizeof(b));
		memset(d,0,sizeof(d));
		scanf("%d%d%d%d",&l,&t,&n,&c);
		int ans1=0;
		forn(i,c)
		{
			scanf("%d",&a[i-1]);
			b[i-1]=a[i-1];
			ans1+=a[i-1];
		}
		int x=c;
		int j=0;
		while(x<n)
		{
			b[x]=a[j];
			ans1+=b[x];
			x++;j++;
			if(j==c)
				j=0;
		}
//		cout<<"ans1= "<<ans1<<endl;
		int ans=0;
		int temp=0;
		int i;
		for(i=0;i<n;i++)
		{
			temp+=b[i];
			if(temp*2>=t)
			{
				ans=t;
				break;
			}
		}
//		cout<<"temp  "<<temp<<endl;
		d[0]=(temp*2-t)/2;
//		cout<<ans<<endl;
//		cout<<"      "<<d[0]<<endl;
		int kk=1;
		int cc=n-i;
		i++;
//		cout<<"Cc  "<<cc<<endl;
		while(i<n)
		{
			d[kk]=b[i];
//			cout<<"   "<<d[kk]<<endl;
			kk++;i++;
		}
		sort(d,d+kk);
		if(cc<=l)
			ans+=(ans1-temp);
		else
		{
			int y;
			for(y=kk-1;y>kk-1-l;y--)
				ans+=d[y];
			while(y>=0)
			{
				ans+=2*d[y];
				y--;
			}
		}
		if(l==0)
			ans=ans1*2;
		printf("Case #%d: ",tcase);
		printf("%d\n",ans);
	}
	return 0;
}