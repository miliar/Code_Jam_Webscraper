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
int h1,h2,h3,h4,h5,cc=1,t,r,c,d,m1[11][11],ans;
int main(){
	freopen("B-small-attempt0 (1).in","r",stdin);
	freopen("ans.txt","w",stdout);
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d%d%d",&r,&c,&d);
		for(h1=0;h1<r;h1++)
			for(getchar(),h2=0;h2<c;h2++)
			{
				char ccc;
				scanf("%c",&ccc);
				m1[h1][h2]=ccc-48;
			}
		ans=2;
		for(h1=0;h1+ans+1<=r;h1++)
		{
			for(h2=0;h2+ans+1<=c;h2++)
			{
				for(h3=ans+1;h1+h3<=r&&h2+h3<=c;h3++)
				{
					double ctx=0,cty=0;
					for(h4=h1;h4<h1+h3;h4++)
					{
						for(h5=h2;h5<h2+h3;h5++)
						{
							if((h4==h1)+(h5==h2)+(h4==h1+h3-1)+(h5==h2+h3-1)<2)
							{
								ctx+=m1[h4][h5]*(h1+h3*0.5-h4-0.5);
								cty+=m1[h4][h5]*(h2+h3*0.5-h5-0.5);
							}
						}
					}
					if(fabs(ctx)<1e-9&&fabs(cty)<1e-9)
					{
						ans=h3;
					}
				}
			}
		}
		if(ans==2)
			printf("Case #%d: IMPOSSIBLE\n",cc++);
		else
			printf("Case #%d: %d\n",cc++,ans);
	}
}
