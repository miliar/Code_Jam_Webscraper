#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
#include <cstdio>
using namespace std;

int s,q;
vector<string> engs,qs;

int A[102][1002];

int Rec(int pos, int ind)
{
	if (pos==q)
		return 0;

	if (A[pos][ind]!=-1)
		return A[pos][ind];

	if (qs[pos]!=engs[ind])
		return A[pos][ind]=Rec(pos+1,ind);

	int ret = 1000000;
	for(int i=0;i<s;++i) if (i!=ind)
	{
		int tmp=Rec(pos+1,i)+1;
		if (tmp<ret)
			ret=tmp;
	}

	return A[pos][ind]=ret;
}

int main()
{
	int n;
	scanf(" %d ",&n);
	for(int qq=0;qq<n;++qq)
	{
		scanf(" %d ",&s);
		engs.clear();
		for(int i=0;i<s;++i)
		{
			char buf[2049];
			gets(buf);

			engs.push_back(buf);
		}

		scanf(" %d ",&q);
		qs.clear();
		for(int i=0;i<q;++i)
		{
			char buf[2049];
			gets(buf);

			qs.push_back(buf);
		}

		for(int i=0;i<102;++i)
			for(int j=0;j<1002;++j)
				A[i][j]=-1;

		int ret = 1000000;
		for(int i=0;i<s;++i)
		{
			int tmp=Rec(0,i);
			if (tmp<ret)
				ret=tmp;
		}

		printf("Case #%d: %d\n",qq+1,ret);
	}

	return 0;
}