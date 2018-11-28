#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;

int T,X,S,R,N;
double t;


int main()
{
	freopen("data.in","r",stdin);
	freopen("data.out","w",stdout);

	scanf("%d",&T);
	int tt;
	for(tt=1;tt<=T;++tt)
	{
		printf("Case #%d: ",tt);
		scanf("%d %d %d %lf %d",&X,&S,&R,&t,&N);
		int i;
		vector<pair<int,int> > vw;
		for(i=0;i<N;++i)
		{
			int b,e,w;
			scanf("%d %d %d",&b,&e,&w);
			vw.push_back(make_pair(w,e-b));
		}
		int x=X;
		for(i=0;i<N;++i)
			x-=vw[i].second;
		//vw.push_back(make_pair(S,x));
		sort(vw.begin(),vw.end());
		double ans=0;
		if(t*R>x)
		{
			ans+=(double)x/R;
			t-=ans;
			for(i=0;i<vw.size();++i)
			{
				//if(t>1e-9)
				//{
				if((R+vw[i].first)*t>vw[i].second)
				{
					double tmp=(double)vw[i].second/(R+vw[i].first+0.0);
					ans+=tmp;
					t-=tmp;
				}
				else
				{
					ans+=t;
					ans+=(vw[i].second-t*(R+vw[i].first)+0.0)/(vw[i].first+S+0.0);
					t=0;
				}
				//}
			}
		}
		else
		{
			ans+=t;
			ans+=(x-t*R+0.0)/(S+0.0);
			for(i=0;i<vw.size();++i)
				ans+=(double)vw[i].second/(vw[i].first+S+0.0);
		}
		/*for(i=0;i<vw.size();++i)
		{

			if(t>1e-9)
			{
				if(vw[i].first<R)
				{
					double tmp=(double)vw[i].second/(R+0.0);
					if(t>tmp)
					{
						t-=tmp;
						ans+=tmp;
					}
					else
					{
						ans+=t;
						
						ans+=(vw[i].second-t*R+0.0)/vw[i].first;
						t=0;
					}
				}
			}
			else
			{
				ans+=(double)vw[i].second/(vw[i].first+0.0);
			}
		}*/
		printf("%.7lf\n",ans);
		
	}
	return 0;
}
