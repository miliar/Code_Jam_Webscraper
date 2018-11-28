#include <cstdio>
//#include <iostream>
using namespace std;

int g[1010];
int sg[1010];
int ig[1010];

int main ()
{
    FILE *fin=fopen ("Theme Park.in","r");
    FILE *fout=fopen ("Theme Park.out","w");
    
    int T,t;
    int r,k,n;
    int i;
    int j;
	long long sum,tsum;
    long long ans;
    
    fscanf (fin,"%d",&T);
    
    for(t=1;t<=T;t++)
    {
		fscanf (fin,"%d %d %d",&r,&k,&n);
		
		tsum=0;
		for(i=0;i<n;i++)
		{
			fscanf (fin,"%d",&g[i]);
			tsum+=g[i];
		}
		
		j=0;
		sum=0;
		for(i=0;i<n;i++)
		{
			while(sum+g[j]<=k && sum+g[j]<=tsum)
			{
				sum+=g[j];
				j=j+1<n ? j+1:0;
			}
			
			sg[i]=sum;
			ig[i]=j;
			sum-=g[i];
		}
		
		/*for(i=0;i<n;i++)
			cout<<sg[i]<<" ";
		cout<<endl;
		for(i=0;i<n;i++)
			cout<<ig[i]<<" ";
		cout<<endl;*/
		
		j=0;
		ans=0;
		for(i=0;i<r;i++)
		{
			ans+=sg[j];
			j=ig[j];
		}
		
		fprintf (fout,"Case #%d: %lld\n",t,ans);
	}
	
	//system ("pause");
	return 0;
}
