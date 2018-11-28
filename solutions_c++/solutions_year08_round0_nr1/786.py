#include<cstdio>
#include<map>
#include<string>
#include<iostream>
#include<vector>
using namespace std;
int findmin(int *a,int size)
{
	int i;
	int nRes = a[0];
	for(i=1;i<size;++i)
	{
		if(a[i]<nRes)
			nRes=a[i];
	}
	return nRes;
}
int main(int argc,char* argv[])
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int N,S,Q;
	int nCase = 1;
	scanf("%d",&N);
	char name[101];
	map<string,int>mp;
	vector<int>vec;
	while(nCase <= N)
	{
		mp.clear();
		vec.clear();
		scanf("%d",&S);		
		getchar();

		int ts,tq;
		ts = 0;
		while(ts < S)
		{
			cin.getline(name,sizeof(name));
			if(mp.find(name) == mp.end())
				mp[name] = ts;
			ts++;
		}
		scanf("%d",&Q);
		getchar();

		tq= 0;
		while(tq < Q)
		{
			cin.getline(name,sizeof(name));
			vec.push_back(mp[name]);
			tq++;
		}
		
		int * npState = new int[S];
		int i,nMin,currentNum,j;
		for(i=0;i<S;++i)npState[i] = 0;
		if(vec.size() > 0)
		{
		npState[vec[0]] = 999999;
		for(i=1; i<Q; ++i)
		{
			nMin = findmin(npState,S);
			currentNum = vec[i];
			for(j=0;j<S;++j)
			{
				if(npState[j] == 999999)
				{
					npState[j] = nMin + 1;
				}
				else if(j == currentNum)
				{
					npState[j] = 999999;
				}
			}
		}
		}
		printf("Case #%d: %d\n",nCase++,findmin(npState,S));
	}
	return 0;
}