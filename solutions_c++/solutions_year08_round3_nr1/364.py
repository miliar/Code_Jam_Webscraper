#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cmath>
#include<vector>

using namespace std;

int main()
{
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	int N;
	int nCase =1,i,temp,j;
	int P,K,L;
	vector<long long> vList;
	scanf("%d",&N);
	while(nCase <= N)
	{
		scanf("%d %d %d",&P,&K,&L);
		for(i=0;i<L;++i)
		{
			scanf("%d",&temp);
			vList.push_back(temp);
		}
		sort(vList.begin(),vList.end());
		long long res = 0 ,num =0 ;
		int pos =1;
		for(i=L-1 ; i >= 0 ; i-=K)
		{
			num = 0;
			for(j=i;j>i-K&&j>=0;--j)
				num+=vList[j];
			res += num * pos;
			pos ++;
		}
		printf("Case #%d: ",nCase++);
		cout<<res<<endl;
		vList.clear();

	}
	return 0;
}