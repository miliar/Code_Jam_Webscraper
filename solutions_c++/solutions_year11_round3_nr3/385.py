#pragma comment(linker,"/STACK:16777216")
#include<cstdio>
#include<iostream>
#include<algorithm>
#include<vector>
#include<stack>
#include<queue>
#include<set>
#include<map>
#include<string>
#include<cstring>
#include<ctime>
#include<cmath>
#include<functional>

using namespace std;

#define ll long long
#define ld long double
#define si short int
#define pii pair<int,int>
#define vi vector<int>
#define vit vector<int>::iterator
#define sq(x) (x)*(x)

ll* mas=new ll[10000];

void test(int T)
{
	int n,l,h;
	scanf("%d%d%d",&n,&l,&h);
	for(int i=0; i<n; ++i)
		scanf("%lld",&mas[i]);
	for(int i=l; i<=h; ++i)
	{
		bool b=true;
		for(int j=0; j<n; ++j)
			if(i%mas[j]!=0 && mas[j]%i!=0)
			{
				b=false;
				break;
			}
		if(b)
		{
			printf("Case #%d: %d\n",T+1,i);
			return;
		}
	}
	printf("Case #%d: NO\n",T+1);
}

int main()
{
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	int T;
	cin>>T;
	for(int i=0; i<T; ++i)
		test(i);
	return 0;
}