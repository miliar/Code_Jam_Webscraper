#include<cstdio>
int j_c(int total)
{
	return (total+2)/3;
}
int j_s(int total)
{
	if(total%3==0)return (total/3)+1;
	if(total%3==1)return (total/3)+1;
	if(total%3==2)return (total/3)+2;
}
int main()
{
	int tt,n,s,p,h_m;
	scanf("%d",&tt);
	for(int i=1;i<=tt;i++)
	{
		h_m=0;
		int t[31]={};
		scanf("%d %d %d", &n, &s, &p);
		for(int j=0;j<n;j++)
		{
			int r;
			scanf("%d",&r);
			t[r]++;
		}
		for(int j=0;j<=30;j++)
		{
			if(j==0||j==1)
				h_m+=(j_c(j)>=p)?(t[j]):0;
			else
			{
				if(s>0)
				{
					if(j_s(j)>=p)
					{
						if(s>=t[j]){s-=t[j];h_m+=t[j];}
						else{h_m+=s;s=0;}
					}
					else h_m+=(j_c(j)>=p)?(t[j]):0;
				}
				else h_m+=(j_c(j)>=p)?(t[j]):0;
			}
		}
		printf("Case #%d: %d\n",i,h_m);
	}
}
