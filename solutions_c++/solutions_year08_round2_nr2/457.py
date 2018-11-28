// A.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include "cstdio"
#include "cmath"

const int MAXN = 1001;

int prime[MAXN] = {0};
//set记录其代表元素，rank代表集合中的层数；
int set[MAXN],rank[MAXN];

//返回一个包含X的子集。
//返回一个包含X的子集。
int FindSet(int x)
{
	int p1 = x;
	int p2;

	while (set[p1] != p1)
	    p1 = set[p1];
	//压缩路径
	for (p2=x; p2!=p1; p2=set[p1])
		set[p2]=p1;
	return p1;
}

//生成一个单元素集合{X}。这个操作对集合S的每一个元素只能应用一次。
void MakeSet(int x)
{
    set[x]=x;
    rank[x]=0;
}

//
void Link(int a,int b)
{
    if(rank[a]>rank[b])
        set[b]=a;
    else if(rank[a]<rank[b])
        set[a]=b;
    else
    {
        set[a]=b;
        rank[b]++;
    }
}

//构造分别包含X和Y的不相交子集的并集，并把它添加到子集的集合中，以代替被删除的两个子集；
void Union(int a,int b)
{
    Link(FindSet(a),FindSet(b));
}

bool check(int a,int b,int l,int p)
{
	int i;

	for (i = p; i <= l; i++)
		if (prime[i] == 0 && a%i == 0 && b%i == 0)
			return true;
	return false;
}

int solve()
{
	int a,b,p;
	int ans = 0;
	int i,j;

	scanf("%d%d%d",&a,&b,&p);
	for (i = a; i <= b; i++)
		MakeSet(i);

	for (i = a; i <= b; i++)
		for (j = a; j <= b; j++)
			if (check(i,j,b,p))
				Union(i,j);

	for (i = a; i <= b; i++)
		if (set[i] == i)
			ans++;
	return ans;
}

int main()
{
	freopen("s.txt","r",stdin);
	freopen("a.txt","w",stdout);
	int t,i,j;
	int ans;

	for (i = 2; i < MAXN; i++)
		if (prime[i] == 0)
		{
			for (j = i+i; j < MAXN; j += i)
				prime[j] = 1;
		}

	scanf("%d",&t);
	for (i = 1; i <= t; i++)
	{
		ans = solve();
		printf("Case #%d: %d\n",i,ans);
	}
	return 0;
}

