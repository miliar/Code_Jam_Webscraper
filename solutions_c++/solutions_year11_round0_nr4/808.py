#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <cstdio>
#include <climits>
#include <cmath>
using namespace std;

int find(vector<int>& elems,int i,int v)
{
	for(int j=i;j<(int)elems.size();j++)
		if(elems[j]==v)
			return j;
	return -1;
}

int main()
{
	int T; cin>>T;
	for(int ds=1;ds<=T;ds++)
	{
		int N; cin>>N;
		
		vector<int> elems(N);
		for(int i=0;i<N;i++)
		{
			cin>>elems[i];
			elems[i]--;
			cerr<<elems[i]<<" ";
		}
		cerr<<endl;
		
		int num=N;
		for(int i=0;i<N;i++)
		{
			if(elems[i]==i)
				num--;
		}
		
		double ans=num;
		fprintf(stderr,"Case #%d: %.6f\n",ds,ans);
		printf("Case #%d: %.6f\n",ds,ans);
	}
	return 0;
}
