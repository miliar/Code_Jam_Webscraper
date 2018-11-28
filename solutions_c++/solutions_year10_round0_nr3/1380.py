#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <math.h>
#pragma comment (linker,"/STACK:16000000")
using namespace std;
struct pnt{
	int w;
	int num;
};
const int maxn = 1010;
pnt mas[maxn*maxn];
long long calc(int n, int k, int R)
{
	int i,j,N = n;
	long long res = 0;
	int cnt = 0, tmp, add, myR = 0;
	i=1;
	while (i<=n)
	{
		if (i!=1 && mas[i].num==1)
			break;
		j = i;
		tmp = 0;
		while (j<=n && (tmp+mas[j].w)<=k)
		{
			tmp += mas[j].w;
			++j;
		}
		add = 0;
		for (int pos=i;pos<j;pos++)
		{
			++add;
			mas[n+add] = mas[pos];
		}
		n += add;
		++myR;
		res += (long long)tmp;
		if (myR==R)
			break;
		i = j;
	}
	if (myR==R)
		return res;
	int d;
	R -= myR;
	d = R / myR;
	R %= myR;
	res += res * d;
	if (R==0)
		return res;
	i=1;
	n = N;
	myR = 0;
	while (i<=n)
	{
		j = i;
		tmp = 0;
		while (j<=n && (tmp+mas[j].w)<=k)
		{
			tmp += mas[j].w;
			++j;
		}
		add = 0;
		for (int pos=i;pos<j;pos++)
		{
			++add;
			mas[n+add] = mas[pos];
		}
		n += add;
		++myR;
		res += (long long)tmp;
		if (myR==R)
			break;
		i = j;
	}
	return res;
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t,i,j;
	scanf("%d",&t);
	int R,k,n;
	for (int q=1;q<=t;++q)
	{
		printf("Case #%d: ",q);
		scanf("%d %d %d",&R,&k,&n);
		for (i=1;i<=n;i++)
		{
			scanf("%d",&mas[i].w);
			mas[i].num = i;
		}
		printf("%I64d\n",calc(n,k,R));
	}

	return 0;
}