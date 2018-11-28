#include<iostream>
#include<string.h>
#include<algorithm>
double w[110];
double ow[110];
double oow[110];
double ans[110];
char a[110][110];
double k[110][110];
//int w[110][110];
using namespace std;
int main()
{
	freopen("n.txt","w",stdout);
	int t,i,j,n;
	cin>>t;
	double sum;
	int num;
	int id;
	for(id=1;id<=t;id++)
	{
		printf("Case #%d:\n",id);
		scanf("%d",&n);
		for(i=0;i<n;i++)
		{
			scanf("%s",a[i]);
		}
        for(i=0;i<n;i++)
		{
			int win=0,lose=0;
			for(j=0;j<n;j++)
			{
				if(a[i][j]=='1')
					win++;
				else if(a[i][j]=='0')
					lose++;
			}
			w[i]=(double)win/(win+lose);
			for(j=0;j<n;j++)
			{
				if(a[i][j]=='1')
					k[i][j]=(double)(win-1)/(win+lose-1);
				else if(a[i][j]=='0')
					k[i][j]=(double)win/(win+lose-1);
				else
					k[i][j]=w[i];
			}
			//cout<<w[i]<<endl;
		}
		for(i=0;i<n;i++)
		{
            sum=0;
		    num=0;
			for(j=0;j<n;j++)
			{
                if(a[i][j]=='1'||a[i][j]=='0')
				{
					sum+=k[j][i];
				    num++;
				}
			}
			ow[i]=sum/num;
			//cout<<ow[i]<<endl;
		}
		for(i=0;i<n;i++)
		{
			 sum=0;
			 num=0;
			 for(j=0;j<n;j++)
			 {
				 if(i==j)
					 continue;
				 if(a[i][j]=='1'||a[i][j]=='0')
				 {
					 sum+=ow[j];
					 num++;
				 }
			 }
			 oow[i]=sum/num;
		}
		for(i=0;i<n;i++)
		{
			ans[i]=0.25*w[i]+0.5*ow[i]+0.25*oow[i];
			printf("%lf\n",ans[i]);
		}

	}
	return 0;
}