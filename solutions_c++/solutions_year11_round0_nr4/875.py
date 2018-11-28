#include<cstdio>
#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
using namespace std;

int* nums;
bool* was;

int findcicle(int pos)
{
	if(nums[pos]==pos)
	{
		was[pos]=true;
		return 0;
	}
	int answ=0;
	while(!was[pos])
	{
		answ++;
		was[pos]=true;
		pos=nums[pos];
	}
	return answ;
}

void test(int num)
{
	int n;
	scanf("%d",&n);
	for(int i=0; i<n; ++i)
	{
		scanf("%d",nums+i);
		nums[i]--;
		was[i]=false;
	}
	int answ=0;
	for(int i=0; i<n; ++i)
		if(!was[i])
			answ+=findcicle(i);
	printf("Case #%d: %d.000000\n",num,answ);
}

int main()
{
	freopen("d.in","r",stdin);
	freopen("d.out","w",stdout);
	int t;
	nums=new int[10000];
	was=new bool[10000];
	scanf("%d",&t);
	for(int i=0; i<t; ++i)
		test(i+1);
	return 0;
}