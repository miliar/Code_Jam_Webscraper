#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <cstdio>
#define maximum(a,b) ((a)>(b) ? (a):(b))
using namespace std;
int nse;
int nq;
vector<string> SE;
vector<string> Q;

int res()
{
	int ret = 0 , next=0;
	while(next < Q.size())
	{
		int k=0;
		for(int i = 0 ; i<SE.size() ; i++)
		{
			int j;
			for(j=next ; j<Q.size() && Q[j]!=SE[i]; j++);
			k = maximum(k , j);
		}
		next = k;
		ret++;
	}
	if(ret-1 < 0)
	return 0;
	else return ret-1;
}


main()
{
	int t;
	scanf("%d\n",&t);
	for(int i=0;i<t;i++)
	{
		nse = nq = 0;
		SE.clear();
		Q.clear();
		
		char temp[100];

		scanf("%d\n",&nse);		
		for(int j=0 ; j<nse ; j++)
		{
			cin.getline(temp , 100);
 			SE.push_back(temp);
		}
		
		scanf("%d\n",&nq);
		for(int j=0 ; j<nq ; j++)
		{
			cin.getline(temp , 100);
			Q.push_back(temp);
		}
		/*cout<<nse<<" "<<nq<<"  "<<t<<endl;
		for(int j=0 ; j<nq ; j++)
			cout<<Q[j]<<endl;
		for(int j=0 ; j<nse ; j++)
			cout<<SE[j]<<endl;*/
		cout<<"Case #"<<i+1<<": "<<res()<<endl;
	}
	return 0;
}
