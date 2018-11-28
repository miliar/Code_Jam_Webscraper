#include<cstdio>
#include<cmath>
#include<vector>
using namespace std;
int main()
{
	int t;
	scanf("%d",&t);
	for(int k=1;k<=t;k++)
	{
		int a,b,p=0;
		scanf("%d %d",&a,&b);
		printf("Case #%d: ",k);
		vector<int>c;
		c.assign(b-a+1,0);
		for(int i=a;i<b;i++)
		{
			if(c[i-a]);
			else
			{
				
				int l=(int)(log((double)i)/log(10));
				int temp=1;
				int s=i;
				for(int j=1;j<=l;j++)
				{
					if(s%10==0)
					{
						s/=10;
					}
					else
					{
						int r;r=s%10;
						s/=10;
						s+=r*(int)pow(10,double(l));
						if((s>=a)&&(s<=b)&&(s!=i)&&(!c[s-a]))
						{
							c[s-a]=true;
							temp++;
						}
					}
				}
				p+=(temp*(temp-1)/2);
			}
		}
		printf("%d\n",p);
	}	
}
