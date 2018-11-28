#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<set>
using namespace std;
#define MAX 10000
const int BIG=0x3f3f3f3f;
bool is[MAX],in[MAX];
int b[MAX],p[MAX],q[MAX],q2[MAX],pp,a[11];
int X[7]={1,10,100,1000,10000,100000,1000000};
void init()
{
	int i,j;
	for(i=2;i<MAX;i++)
		if(!is[i])
		{
			p[pp++]=i;
			for(j=i*i;j<MAX;j+=i)
				is[j]=true;
		}
}
int main()
{
	int cs,i,j,k,l,r,r2,dd,K,D,mx;
	init();
	scanf("%d",&cs);
	set<int> st;
	for(dd=1;dd<=cs;dd++)
	{
		st.clear();
		scanf("%d%d",&D,&k);
		for(mx=i=0;i<k;i++)
		{
			scanf("%d",&a[i]);
			mx=max(mx,a[i]);
		}
		if(k==1)
		{
			printf("Case #%d: I don't know.\n",dd);
		}
		else
		{
			for(i=0;i<pp;i++)
			{
				if(p[i]>=X[D])
					break;
				if(p[i]<=mx)
					continue;
				for(l=r=j=0;j<p[i];j++)
				{
					q[r]=j;
					b[r++]=((a[1]-a[0]*j)%p[i]+p[i])%p[i];
				}
				for(K=1;K<k;K++)
				{
					if(K+1<k)
					{
						for(r2=l=0;l<r;l++)
							if(a[K+1]==(q[l]*a[K]+b[q[l]])%p[i])
								q2[r2++]=q[l];
					}
					else
					{
						for(l=0;l<r;l++)
							st.insert((a[K]*q[l]+b[q[l]])%p[i]);
					}
					memcpy(q,q2,sizeof(q));
					r=r2;
				}
				if(st.size()>1)
					break;
			}
			if(st.size()>1||st.size()==0)
				printf("Case #%d: I don't know.\n",dd);
			else
				printf("Case #%d: %d\n",dd,*(st.begin()));
		}
	}
}