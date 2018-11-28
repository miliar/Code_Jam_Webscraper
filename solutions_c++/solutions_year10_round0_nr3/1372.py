#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <queue>
#include <map>

using namespace std;

struct test
{
	int g;
	int flag;
}que;
queue<test>io;
queue<test>ip;
map<int,int>mymap;
vector<long long>my;

int main()
{
	int t,cas;
	freopen("test.txt","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&t);
	for(cas=1;cas<=t;++cas)
	{
		mymap.clear();
		while(!io.empty())
			io.pop();
		while(!ip.empty())
			ip.pop();
		my.clear();
		int r,k,n,i,j;
		scanf("%d%d%d",&r,&k,&n);
		for(i=0;i<n;++i)
		{
			que.flag=i+1;
			scanf("%d",&que.g);
			io.push(que);
		}
		int p=0,sum,lun,first;
		long long sun=0,ans;
		my.push_back(0);
		while(1)
		{
			test temp=io.front();
			if(p!=0&&mymap[temp.flag]!=0)
			{
				lun=p-mymap[temp.flag]+1;
				sun=sun-my[mymap[temp.flag]-1];
				first=mymap[temp.flag]-1;
				break;
			}
			mymap[temp.flag]=p+1;
			sum=0;
			while(sum+temp.g<=k)
			{
				sum+=temp.g;
				ip.push(temp);io.pop();
				if(io.empty()) break;
				temp=io.front();
			}
			while(!ip.empty())
				io.push(ip.front()),ip.pop();
			p++;sun+=sum;
			my.push_back(sun);
		}
		int hj=(r-first)%lun;
		ans=my[first];
		ans+=(long long)(r-first)/lun*sun;
			ans+=my[hj+first]-my[first];
		printf("Case #%d: %lld\n",cas,ans);
	}
}