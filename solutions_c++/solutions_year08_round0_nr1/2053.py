#include <cstdio>
#include <string>
#include <iostream>
#include <map>
#include <algorithm>
#include <vector>
using namespace std;
int main()
{
	int N,S,Q;
	map <string, int> engine; //engine name to index
	int n,s,ss,q,ind;
	string name,query;
	int best[101],minimum;
	scanf("%d",&N);
	for (n=1;n<=N;n++)
	{
		scanf("%d\n",&S);
		for (s=1;s<=S;s++)
		{
			getline(cin,name);
			engine[name]=s;
			best[s]=0;
			//cout<<name<<endl;
		}
		scanf("%d\n",&Q);
		for (q=0;q<Q;q++)
		{
			getline(cin,query);
			ind=engine[query];
			minimum=2000;
			for (ss=1;ss<=S;ss++)
			if (ss!=ind)
			{
				if (best[ss]<minimum) minimum=best[ss];
			}
			minimum=minimum+1;
			best[ind]=minimum;
//			printf("%10s:",query.c_str(),ind,best[ind]);
//			for (ss=1;ss<=S;ss++)
//				printf("%2d ",best[ss]);
//			printf("\n");
		}
		minimum=2000;
		for (ss=1;ss<=S;ss++)
		if (best[ss]<minimum)
			minimum=best[ss];
		printf("Case #%d: %d\n",n,minimum);
	}
  	return 0;
}
