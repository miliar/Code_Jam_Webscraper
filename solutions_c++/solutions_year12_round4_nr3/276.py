#pragma comment(linker, "/STACK:65000000")
#include<cstdio>
#include<iostream>
#include<algorithm>
#include<vector>
#include<stack>
#include<queue>
#include<set>
#include<map>
#include<cstring>
#include<string>
#include<cmath>
#include<ctime>

using namespace std;

#define ll long long
#define pii pair<int,int>
#define vi vector<int>
#define vit vi::iterator
#define vpi vector<pii >
#define sq(x) (x)*(x)

int mas[2000];
int hei[2000];
int n;

void test(int t)
{
	scanf("%d",&n);
	for(int i=0; i<n-1; ++i)
	{
		scanf("%d",mas+i);
		--mas[i];
	}
	printf("Case #%d: ",t);
	for(int i=0;i<n;++i)
		hei[i]=1;
	bool corr = false;
	for(int kkk=0; !corr && kkk<2000; ++kkk)
	{
		for(int i=n-2; i>=0; --i)
		{
			double mx = -1e9;
			for(int j=i+1; j<n; ++j)
				if(j!=mas[i])
					mx = max(mx, (hei[j]-hei[i])/double(j-i));
			if(mx> -1e9)
			hei[mas[i]]=max((int)(mx*(mas[i]-i)+1+hei[i]),hei[mas[i]]);
		}
		corr = true;
		for(int i=0; i<n-1; ++i)
		{
			double mx = -1e9;
			int pos = i;
			for(int j=i+1; j<n; ++j)
				if(mx < (hei[j]-hei[i])/double(j-i)-1e-9)
				{
					mx = (hei[j]-hei[i])/double(j-i);
					pos = j;
				}
			if(pos!=mas[i])
			{
				//printf("Impossible\n");
				//return;
				corr = false;
			}
		}
	}
	if(!corr)
	{
		printf("Impossible\n");
		return;
	}
	for(int i=0; i<n; ++i)
		printf("%d%c",hei[i]+1,i==n-1?'\n':' ');
}

int main()
{
	freopen("c.in","r",stdin);freopen("c.out","w",stdout);
	int t;
	cin>>t;
	for(int i=0; i<t; ++i)
		test(i+1);
	return 0;
}