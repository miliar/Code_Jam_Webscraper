#include <cstdio>
#include <cstdlib>
#include <string>
#include <list>
#include <set>
#include <map>
#include <algorithm>
#include <vector>
#include <cmath>
#include <queue>
#include <cctype>
#include <iostream>
using namespace std;

long ans;
long M,V;

//vector <int> a,b;

int a[10000];
int b[10000];
int d[10000];
int c[100];

int Fand(int a,int b)
{
	return a*b;
}

int For(int a,int b)
{
	if (a+b>0) return 1;
	return 0;
}

void go(int n,int now)
{
	if (n<0) return;
	if (b[n]==1)
	{
		a[n]=Fand(a[n*2+1],a[n*2+2]);
	}
	else
	{
		a[n]=For(a[n*2+1],a[n*2+2]);
	}
	go(n-1,now);

	if (n==0)
	{
		if (a[0]==V)
		{
			if (now<ans)
			{
				ans=now;
//				cout<<"+0 "<<ans<<endl;
			}
		}
	}

	if (d[n]==0)
	{
		return;
	}
	if (b[n]==0)
	{
		a[n]=Fand(a[n*2+1],a[n*2+2]);
	}
	else
	{
		a[n]=For(a[n*2+1],a[n*2+2]);
	}
	go(n-1,now+1);
	if (n==0)
	{
		if (a[0]==V)
		{
			if (now+1<ans)
			{
				ans=now+1;
//				cout<<"+1 "<<ans<<endl;
			}
		}
	}
}

int main()
{
	long long i,j,k,l,N=0,Case=0;

/*	a.insert(1);

	b.push_back("abc");
	b.push_back("def");
	b.push_back("012");

	for (i=0;i<b.size() ;i++ )
	{
		cout<<b[i]<<endl;
	}
	sort(b.begin(),b.end());
	reverse(b.begin(),b.end());
	for (i=0;i<b.size() ;i++ )
	{
		cout<<b[i]<<endl;
	}
	
*/

/*	j=1;
	for (i=0;i<16;i++)
	{
		c[i]=j;
		j*=2;
	}
*/	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	scanf("%ld",&N);
//	cout<<N<<endl;
//	cin<<N;
//	printf("%lld\n",N);
	for (Case=1;Case<=N;Case++)
	{
		scanf("%d %d",&M,&V);
//		a.clear();b.clear();
		for (i=0;i<(M-1)/2;i++)
		{
			scanf("%d %d",&j,&k);
			b[i]=j;
			d[i]=k;
//			a.push_back(j);
//			b.push_back(k);
		}
		l=i;
		for (;i<M;i++)
		{
			scanf("%d",&j);
			a[i]=j;
//			a.push_back(j);
		}
/*		for (k=0;k<16;k++)
		{
			if (c[k+1]>j)
			{
				break;
			}
		}
*/
		ans=9999;
		go((M-1)/2-1,0);


//		printf("Case #%d: ", Case);
//		printf("%lld\n",ans);
		if (ans<9999)
		{
			cout<<"Case #"<<Case<<": "<<ans<<endl;
		}
		else
			cout<<"Case #"<<Case<<": IMPOSSIBLE"<<endl;
	}
   return 0;
}
