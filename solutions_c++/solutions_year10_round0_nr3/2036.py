#include <iostream>
using namespace std;

__int64 t,x,N,R,k,i,j,a[1005],b[1005][2],sum=0,cur,start;
int main()
{
	

	freopen("C-large.in","r",stdin);
	freopen("output.txt","w",stdout);

	cin>>t;
	for(x=1;x<=t;x++)
	{
		sum=0;
		for(i=0;i<N;i++)
			b[i][0]=0;
		cin>>R>>k>>N;
		for(i=0;i<N;i++)
			cin>>a[i];
		for(i=0;i<N;i++)
		{
			cur=0;
			j=i;
			start=j;
			while(cur<=k)
			{
				if(cur+a[j]>k)
					break;
				cur+=a[j];
				b[i][0]+=a[j];
				j++;
				if(j>=N)
					j-=N;
				if(j==start)
					break;
			}
			b[i][1]=j;
		}
		j=0;
		for(i=0;i<R;i++)
		{
			sum+=b[j][0];
			j=b[j][1];
		}
		cout<<"Case #"<<x<<": "<<sum<<"\n";
	}
	return 0;
}