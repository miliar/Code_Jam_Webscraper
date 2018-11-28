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

int n;
pii mas[100000];
int len[100000];
int d;

void test(int t)
{
	memset(len,0,sizeof(len));
	scanf("%d",&n);
	for(int i=0; i<n; ++i)
		scanf("%d%d",&mas[i].first,&mas[i].second);
	scanf("%d",&d);
	len[0] = min(mas[0].first, mas[0].second);
	len[n] = -1;
	mas[n] = pii(d,0);
	for(int i=0; i<n; ++i)
		for(int j=i+1; j<=n; ++j)
			if(len[i]+mas[i].first >= mas[j].first)
				len[j] = max(len[j], min(min(len[i], mas[j].first-mas[i].first),mas[j].second));
			else
				break;
	if(len[n]!=-1)
		printf("Case #%d: YES\n",t);
	else
		printf("Case #%d: NO\n",t);
}

int main()
{
	freopen("a.in","r",stdin);freopen("a.out","w",stdout);
	int t;
	cin>>t;
	for(int i=0; i<t; ++i)
		test(i+1);
	return 0;
}