#include <iostream>
#include <vector>
#include <string>
using namespace std;

const int BIT_MAX=32;

int T,n;
vector<int> pile;

int get2sum(int a,int b)
{
	int sum=0;
	
	for(int i=0 ;i<BIT_MAX ;i++)
	{
		int tmp=(a&(1<<i)) ^ (b&(1<<i));
		sum|=tmp;
	}

	return sum;
}

void process()
{
	int ans=-1;
	for(int i=1 ;i<(1<<n)-1 ;i++)
	{
		int tmp=0,tmp2=0;
		int real=0,real2=0;
		for(int j=0 ;j<n ;j++)
		{
			if(i&(1<<j))
			{
				tmp=get2sum(tmp,pile[j]);
				real+=pile[j];
			}
			else
			{
				tmp2=get2sum(tmp2,pile[j]);
				real2+=pile[j];
			}
		}
		//printf("tmp = %d, tmp2 = %d\n",tmp,tmp2);
		//printf("real = %d, real2 = %d\n",real,real2);
		if(tmp==tmp2)
		{
			ans=max(ans,max(real,real2));
		}
	}
	if(ans==-1) puts("NO");
	else printf("%d\n",ans);
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int cas=1;

	//printf("sum = %d\n",get2sum(50,10));

	cin>>T;
	while(T--)
	{
		pile.clear();
		cin>>n;
		for(int i=0 ;i<n ;i++)
		{
			int tmp;cin>>tmp;
			pile.push_back(tmp);
		}
		printf("Case #%d: ",cas++);
		process();
	}
}