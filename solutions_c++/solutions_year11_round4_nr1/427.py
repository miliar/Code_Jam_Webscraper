#include <stdio.h>
#include <algorithm>

using namespace std;

#define MAX 1100
#define EPS 1e-7

pair<pair<int,int>, int> esteiras[MAX];

bool cmp(pair<pair<int,int>,int> a, pair<pair<int,int>, int> b)
{
		if(a.second!=b.second)
				return a.second<b.second;
		return a<b;
}

int main()
{
		int i,j;
		int n;
		int T,ccnt;
		int x,s,r;
		double t;
		double tresp;
		int pos;
		
		scanf("%d",&T);

		for(ccnt=1;ccnt<=T;++ccnt)
		{
				scanf("%d %d %d %lf %d",&x,&s,&r,&t,&n);

				double out =0;

				for(i=0;i<n;++i)
				{
						scanf("%d %d %d",&esteiras[i].first.first,&esteiras[i].first.second,&esteiras[i].second);
						out+=esteiras[i].first.second-esteiras[i].first.first;
				}

				sort(esteiras, esteiras+n,cmp);
				tresp=0;
				pos=0;

				double dleft,tt;
				dleft = x-out;
				tt = dleft/(double) r;
				if(tt>t)
						tt=t;
				dleft-=r*tt;
				t-=tt;
				tresp+=tt;
				tt = dleft/(double)s;
				dleft-=s*tt;
				tresp+=tt;

				for(i=0;i<n;++i)
				{
						dleft=esteiras[i].first.second-esteiras[i].first.first;
						tt = dleft/(double)(r+esteiras[i].second);
						if(tt>t)
								tt=t;
						dleft-=(r+esteiras[i].second)*tt;
						t-=tt;
						tresp+=tt;
						tt = dleft/(double)(s+esteiras[i].second);
						dleft-=(s+esteiras[i].second)*tt;
						tresp+=tt;


				}


				printf("Case #%d: %f\n",ccnt,tresp);
		}

		return 0;
}

				




