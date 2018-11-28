#include <cstdio>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

bool comp(queue <long long> a, queue <long long> b)
{
	while(!a.empty())
	{
		if(a.front() != b.front()) return false;
		a.pop();
		b.pop();
	}
	return true;
}


int main()
{
	freopen("park(in).txt","r",stdin);
	freopen("park(out).txt","w",stdout);
	int i,t,n;
	unsigned long long r,k,buf;;
	scanf("%d",&t);
	for(int c=1; c<=t; c++)
	{
		scanf("%llu%llu%d",&r,&k,&n);
		queue <long long> q,bq;
		for(i=0; i<n; i++)
		{
			scanf("%lld",&buf);
			q.push(buf);
		} 
		vector <queue <long long> > s;
		vector <long long> v;
		long long a,fr,res = 0;
		s.push_back(q);
		v.push_back(res);
		while(r)
		{
			fr = k;
			a = q.front();
			while(fr >= a)
			{
				fr -= a;
				res += a;
				bq.push(a);
				q.pop();
				if(!q.empty()) a = q.front(); 
				else break; 
			}
			while(!bq.empty())
			{
				q.push(bq.front());
				bq.pop();
			}
			if(--r == 0) break;
			for(i=0; i<s.size(); i++)
			{
				if(comp(s[i],q))
				{
					res += (res-v[i])*(r/((int)v.size()-i));
					res += v[r%((int)v.size()-i)+i]-v[i];
					r = 0;
					break;
				}
			}
			s.push_back(q);
			v.push_back(res);
		}
		printf("Case #%d: %lld\n",c,res);
	}
	return 0;
}