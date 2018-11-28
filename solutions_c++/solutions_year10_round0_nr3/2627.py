#include<iostream>
using namespace std;
int main(int argc,char* argv[])
{
int t,n;
long int r,k,a[1000];
int i=0,j,x,y,z,b;
long long int ans[50]={0};
long int sum[1000];
int pos[1000];
int visit[1000];
	cin>>t;
	while(i<t)
	{
		cin>>r>>k>>n;
		for(j=0;j<n;j++)
		cin>>a[j];
		for(j=0;j<1000;j++)
		{
		sum[j]=pos[j]=0;
		visit[j]=-i;
		}
			for(j=0;j<n;j++)
            {
                            y=0;
                            for(x=j;y<n;x++)
                            {
                             x=x%n;
                             if((sum[j]+a[x])<=k)
                             {
                             sum[j]+=a[x];
                             pos[j]=x;
                             y++;
                             }
                             else
                             break;
                            }
            }		
            x=0;
            ans[i]+=sum[x];
            visit[0]=x;
            x=(pos[x]+1)%n;			
            for(j=1;j<r;j++)
            {
             for(y=0;y<=j;y++)
             if(visit[j]=x)
             break;
             visit[j]=x;
             ans[i]+=sum[x];
             x=(pos[x]+1)%n;
            }
            ans[i]*=(r/j);
            r=r%j;
            for(j=0;j<r;j++)
            {
             ans[i]+=sum[x];
             x=(pos[x]+1)%n;
            }
		cout<<"Case #"<<i+1<<": "<<ans[i]<<"\n";
		i++;
	}
	return 0;
}
