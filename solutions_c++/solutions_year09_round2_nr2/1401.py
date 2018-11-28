#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
using namespace std;

int arr[100];
int arr2[100];
int size = 0;
set<int> S;
void perm(int msk,int cur,int gene)
{
	if(cur == size)
	{
		int cnt = 0;
		while(gene)
		{
			arr2[cnt++] = gene % 10 - 1;
			gene /= 10;
			int ans = 0;
			for(int i = 0;i < cnt;i++)
				ans = ans * 10 + arr[arr2[i]];
			S.insert(ans);
		}
		return;
	}
	for(int i = 0;i < size;i++)
	{
		if(msk&(1<<i))
			perm(msk^(1<<i),cur+1,gene*10 + i + 1);
	}
}
int get(int number)
{
	int arr[100];
	int size = 0;
	while(number)
	{
		arr[size++] = number % 10;
		number /= 10;
	}
	bool flg[100];
	memset(flg,0,sizeof flg);
	sort(arr,arr+size);
	int ans = 0;
	for(int i = 0;i < size;i++)
	{
		if(arr[i])
		{
			ans = arr[i];
			flg[i] = true;
			break;
		}
	}
	ans *= 10;
	for(int i = 0;i < size;i++)
		if(!flg[i])
		 ans = ans * 10 + arr[i];
		//else ans = ans * 10;
	return ans;
}
void func(int number)
{
	while(number)
	{
		arr[size++] = number % 10;
		number /= 10;
	}
	perm((1<<size)-1,0,0);
}
int main()
{
	int t;
	int cnt = 0;
	freopen("in.txt","r",stdin);
	freopen("out2.txt","w",stdout);
	scanf("%d",&t);
	while(t --)
	{
		int num;
		size = 0;
		S.clear();
		scanf("%d",&num);
		func(num);
		set<int>::iterator it = upper_bound(S.begin(),S.end(),num);
		int ans;
		if(it != S.end() )
		  ans = *it;
		else ans = get(num);
		printf("Case #%d: %d\n",++cnt,ans);
	}
	return 0;
}