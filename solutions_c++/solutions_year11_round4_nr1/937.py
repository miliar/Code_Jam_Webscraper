#include<iostream>
#include<map>
#include<math.h>
#include<vector>
#include<string>
#include<string.h>
#include<queue>
#include<algorithm>
using namespace std;
typedef long long ll;
typedef vector<int>::iterator iv;
typedef map<string,int>::iterator im;
int cc=1,n,t,h1,h2,m1[1001];
bool m2[1001];
double x,s,r,tt,wm[1001],bm[1001],em[1001],ans;
bool cmp(int fh1,int fh2)
{
	return wm[fh1]<wm[fh2];
}

int main(){
	freopen("A-large (1).in","r",stdin);
	freopen("ans.txt","w",stdout);
	scanf("%d",&t);
	while(t--)
	{
		scanf("%lf%lf%lf%lf%d",&x,&s,&r,&tt,&n);
		double ss=x;
		for(h1=0;h1<n;h1++)
		{
			scanf("%lf%lf%lf",&bm[h1],&em[h1],&wm[h1]);
			m1[h1]=h1;
			//m3[h1]=h1;
			m2[h1]=true;
			ss-=em[h1]-bm[h1];
		}
		bm[n]=0;
		em[n]=ss;
		//cout<<ss<<endl;
		wm[n]=0;
		m1[n]=n;
		m2[n]=true;
		sort(m1,m1+n+1,cmp);
		ans=0;
		for(h1=0;h1<=n;h1++)
		{
			double ut=(em[m1[h1]]-bm[m1[h1]])/(wm[m1[h1]]+r);
			m2[m1[h1]]=false;
			if(ut>tt)
			{
				ans+=tt;
				ut-=tt;
				ut*=(wm[m1[h1]]+r);
				ans+=ut/(wm[m1[h1]]+s);
				break;
			}
			else
			{
				tt-=ut;
				ans+=ut;
			}
		}
		for(h1=0;h1<=n;h1++)
			if(m2[h1])
			{
				ans+=(em[h1]-bm[h1])/(wm[h1]+s);
			}
		printf("Case #%d: %.10lf\n",cc++,ans);
	}
}
