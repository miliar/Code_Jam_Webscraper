#include<iostream>
#include<vector>
#include<map>
#include<queue>
#include<set>
#include<string>
#include<sstream>
#include<algorithm>
#include<numeric>
#include<cmath>
#include<cstdio>
#include<utility>
using namespace std;
typedef long long ll;
#define pi acos(-1.0)
#define INF 1000000000
#define LINF 1000000000000000000LL

int group[1000];
map<vector<int>,pair<ll,ll> > mp;
int main() 
{
    freopen("C-large.in","r",stdin);
 	freopen("output1.txt","w",stdout);
	int nTests;
	scanf("%d",&nTests);
	for(int cs=0;cs<nTests;cs++)
	{
		printf("Case #%d: ",cs+1);
		int R,k,N;
		scanf("%d %d %d",&R,&k,&N);
		for(int i=0;i<N;i++)
			scanf("%d",&group[i]);
		ll s=0,cnt=0;
		vector<int> people(group,group+N);
		vector<int> start=people;
		mp[people]=make_pair(0,0);
		bool f=false;ll sum=0;
		vector<int> next;
		map<vector<int>,pair<ll,ll> >::iterator it;
		ll cc;ll ss;
		do
		{
            ll K=0;
			int i,j;
			for(i=0;i<N;i++)
			{
				if(K+people[i]<=k)
				 {K+=people[i];j=i;}
				else break;
			}
			if(i==N&&(K<=k||K==0)) 
			{
				f=true;
				sum=K*R;
				break;
			}
			cnt++;s+=K;
			if(cnt==R) 
			{
				f=true;
				sum=s;
				break;
			}
			next.clear();
			for(i=j+1;i<N;i++)
				next.push_back(people[i]);
			for(i=0;i<=j;i++)
                next.push_back(people[i]);
			people.clear();
            people=next;
			it=mp.find(next);
			if(it!=mp.end())
			{
				cc=it->second.first;
				cnt=cnt-cc;
				ss=it->second.second;
				s=s-ss;
				break;
			}
			else mp[next]=make_pair(cnt,s);
		}while(1);
	    if(f) printf("%lld\n",sum);
		else
		{
            sum+=ss;
			R-=cc;
			if(R>0) sum+=R/cnt*s;
			R%=cnt;
			while(R--)
			{
		    ll K=0;
			int j;
			for(int i=0;i<N;i++)
			{
				if(K+people[i]<=k)
				 {K+=people[i];j=i;}
				else break;
			}
			sum+=K;
			next.clear();
			for(int i=j+1;i<N;i++)
				next.push_back(people[i]);
			for(int i=0;i<=j;i++)
                next.push_back(people[i]);
			people.clear();
            people=next;
			}
			printf("%lld\n",sum);
		}

	}
	return 0;
}