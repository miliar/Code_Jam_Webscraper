#include <iostream>
#include <map>
using namespace std;
int data[21];
int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	int t,n,testid=1;
	scanf("%d",&t);
	while(t--)
	{
		printf("Case #%d:\n",testid++);
		scanf("%d",&n);
		multimap<int,int> im;
		for(int i=0;i<n;i++)scanf("%d",data+i);
		bool Find=false;
		for(int i=0;i<(1<<n)-1;i++)
		{
			int sum=0;
			for(int j=0;j<n;j++)
			{
				if(i&(1<<j))sum+=data[j];
			}
			pair<multimap<int,int>::iterator,multimap<int,int>::iterator> p;
			p=im.equal_range(sum);
			if(p.first==p.second){im.insert(make_pair(sum,i));continue;}
			for(multimap<int,int>::iterator iter=p.first;iter!=p.second;iter++)
			{
				if(((*iter).second & i)==0)
				{
					Find=true;
					for(int j=0;j<n;j++)if(i&(1<<j))printf("%d ",data[j]);
					printf("\n");
					for(int j=0;j<n;j++)if((*iter).second&(1<<j))printf("%d ",data[j]);
					printf("\n");
					break;
				}
			}
			if(Find)break;
		}
		if(!Find)printf("Impossible\n");
	}
	return 0;
}