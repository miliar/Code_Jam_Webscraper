#include<cstdio>
#include<map>
#include<vector>
#include<string>
#include<iostream>
using namespace std;
int getmin(int *a,int size)
{
	int res = a[0];
	for(int i=1;i<size;++i)
	{
		if(a[i]<res)
			res = a[i];
	}
	return res;
}
int main()
{
	int N,S,Q;
	int nCase = 1;
	scanf("%d",&N);
	char name[101];
	map<string,int>mp;
	vector<int>vec;
	while(nCase <= N)
	{		
		scanf("%d",&S);getchar();
		int ts=0,tq=0;
		while(ts < S)
		{
			cin.getline(name,sizeof(name));
			if(mp.find(name) == mp.end())
				mp[name] = ts;
			ts++;
		}
		scanf("%d",&Q);getchar();
		while(tq < Q)
		{
			cin.getline(name,sizeof(name));
			vec.push_back(mp[name]);
			tq++;
		}
		int * numbers = new int[S];
		int i,nMin,currentNum,j;
		for(i=0;i<S;++i)numbers[i] = 0;
		if(vec.size() > 0)
		{
			numbers[vec[0]] = 0xfffffff;
			for(i=1; i<Q; ++i)
			{
				nMin = getmin(numbers,S);
				numbers[vec[i-1]] = nMin +1;
				numbers[vec[i]] = 0xfffffff;
			}
		}
		printf("Case #%d: %d\n",nCase++,getmin(numbers,S));
		mp.clear();
		vec.clear();
	}
	return 0;
}