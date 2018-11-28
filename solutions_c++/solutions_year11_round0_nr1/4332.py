#include<iostream>
#include<queue>
#include<algorithm>
#include<cstdio>

using namespace std;

int main()
{
	int t,iter=1,p;
	char c;
	cin>>t;
	while(iter<=t)
	{
		vector< pair<char,int> > vp;
		queue<int> p1;
		queue<int> p2;
		int nc;
		cin>>nc;

		for(int i=0;i<nc;i++)
		{
			cin>>c;
			cin>>p;
			vp.push_back(make_pair(c,p));
			if(c=='O')
				p1.push(p);
			if(c=='B')
				p2.push(p);
		}

	int t=0,pos1=1,pos2=1;
	for(int i=0;i<vp.size();i++)
	{
		if(vp[i].first=='O')
		{
			p1.pop();
			int tmax=abs(vp[i].second-pos1)+1;
			t+=tmax;					
			if(!p2.empty())
			{
				if(p2.front()!=pos2)
				{
					int dist=abs(p2.front()-pos2);
					if(dist>tmax)
					{
						if(p2.front()>pos2)
							pos2=pos2+tmax;
						else
							pos2=pos2-tmax;
					}
					else
						pos2=p2.front();
				}
			}
			pos1=vp[i].second;
		}
		
		
		if(vp[i].first=='B')
		{
			p2.pop();
			int tmax=abs(vp[i].second-pos2)+1;
			t+=tmax;						
			if(!p1.empty())
			{
				if(p1.front()!=pos1)
				{
					int dist=abs(p1.front()-pos1);
					if(dist>tmax)
					{
						if(p1.front()>pos1)
							pos1=pos1+tmax;
						else
							pos1=pos1-tmax;
					}
					else
						pos1=p1.front();
				}
			}
			pos2=vp[i].second;
		}		
	}
	
	printf("Case #%d: %d\n",iter,t);
	iter++;	
	}
}
