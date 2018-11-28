#include<iostream>
#include<string.h>
#include<cstdio>
#include<vector>
using namespace std;
int pos[1000000];
int main()
{
	//freopen("D:\\text.in","r",stdin);
	//freopen("D:\\text2.in","w",stdout);
	int R,K,a[1010],i,T,t,N,l;
	long long ans,j,sum;
	bool f[1010];
	scanf("%d",&T);
	for(t=1;t<=T;t++)
	{
		scanf("%d %d %d",&R,&K,&N);
		memset(pos,0,sizeof pos);
		vector<int> q;
		for(i=0;i<N;i++)
			scanf("%d",&a[i]);
		i=0;
		memset(f,0,sizeof f);
		f[0]=1;
		while(1)
		{
			j=0;l=0;
			int tt=i;
			while(j+a[i]<=K)
			{
				j+=a[i];
				i=(i+1)%N;
				l++;
				if(l==N)break;
			}
			q.push_back(j);
			pos[tt]=q.size()-1;
			if(f[i])
				break;
			f[i]=1;
		}
		sum=0;
		ans=0;
		l=i;
		for(i=pos[l];i<q.size();i++)
			sum+=q[i];
		for(i=0;i<pos[l] && R>0;i++,R--)
			ans+=q[i];
		j=R/(q.size()-pos[l]);
		ans+=j*sum;
		R=R%(q.size()-pos[l]);
		for(i=pos[l];i<q.size() && R>0;i++,R--)
			ans+=q[i];
		printf("Case #%d: ",t);
		cout<<ans<<endl;
	}
	return 0;
}