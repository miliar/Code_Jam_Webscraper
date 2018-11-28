#include <iostream>
#include <vector>
using namespace std;
struct trip
{
	int st,en,t;
};
int comp(const trip a,const trip b)
{
	if(a.st>b.st)
		return 0;
	else if(a.st<b.st)
		return 1;
	else
		if(a.en>b.st)
			return 0;
		else
			return 1;
}
int main()
{
	int n;
	scanf("%d\n",&n);
	for(int i=0;i<n;i++)
	{
		vector<trip> v;
		int t,na,nb,t1,t2,t3,t4;
		int ans[2]={0,0};
		scanf("%d\n%d %d\n",&t,&na,&nb);
		for(int j=0;j<na+nb;j++)
		{
			scanf("%d:%d %d:%d\n",&t1,&t2,&t3,&t4);
			trip tm;
			tm.st=t1*60+t2;
			tm.en=t3*60+t4;
			if(j<na)
				tm.t=-1;
			else
				tm.t=1;
			v.push_back(tm);
		}
		sort(v.begin(),v.end(),comp);
		while(v.size())
		{
			int rt=v[0].t,tt=v[0].st;
			ans[(rt+1)/2]++;
			for(int j=0;j<v.size();j++)
				if(tt<=v[j].st && v[j].t==rt)
				{
					rt*=-1;
					tt=v[j].en+t;
					v.erase(v.begin()+j);
					j=-1;
				}
		}
		cout<<"Case #"<<i+1<<": "<<ans[0]<<" "<<ans[1]<<endl;
	}
	return 0;
}
