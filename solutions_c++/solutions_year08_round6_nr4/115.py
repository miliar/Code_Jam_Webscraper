#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
using namespace std;
int main()
{
	int T,Ti=0;
	scanf("%d",&T);
	while(T--)
	{
		Ti++;
		set <pair<int,int> > small,large;
		set <pair<int,int> > ::iterator is;


		int n,m;
		scanf("%d",&n);
		for(int i=0;i<n-1;i++)
		{
			int t1,t2;
			scanf("%d%d",&t1,&t2);
			int mmin,mmax;
			mmin=min(t1,t2);
			mmax=max(t1,t2);
			t1=mmin;
			t2=mmax;
			large.insert(make_pair(t1,t2));

		}
		scanf("%d",&m);
		for(int i=0;i<m-1;i++)
		{
			int t1,t2;
			scanf("%d%d",&t1,&t2);
			int mmin,mmax;
			mmin=min(t1,t2);
			mmax=max(t1,t2);
			t1=mmin;
			t2=mmax;
			small.insert(make_pair(t1,t2));

		}

		int a[10];
		for(int i=0;i<n;i++)
			a[i]=i;

		int yes=0;
		while(1)
		{
			int flag=0;
			for(is=small.begin();is!=small.end();is++)
			{
				int t1=(*is).first;
				int t2=(*is).second;
				t1=a[t1-1]+1;
				t2=a[t2-1]+1;
				int mmin,mmax;
				mmin=min(t1,t2);
				mmax=max(t1,t2);
				t1=mmin;
				t2=mmax;
				if(large.find(make_pair(t1,t2))==large.end())
				{
					flag=1;
					break;
				}
			}
			
			if(flag==0) 
			{
				yes=1;
				break;
			}
			if(!next_permutation(a,a+n)) break;
		}

		if(yes)
			printf("Case #%d: YES\n",Ti);
		else
			printf("Case #%d: NO\n",Ti);
	}
}