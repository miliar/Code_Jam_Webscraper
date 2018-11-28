#include <iostream>
using namespace std;
int a[800];
int b[800];

int main()
{
	freopen("A-small-attempt0.in","r",stdin);	
	freopen("A-small-attempt0.out","w",stdout);
	int i,j,N,t,m,k,s,ans;
	cin>>N;
	for(i=1;i<=N;i++)
	{
		cin>>t;
		for(j=0;j<t;j++) cin>>a[j];		
		for(j=0;j<t;j++) cin>>b[j];	
		for(j=0;j<t-1;j++)
		{
			m=j;
			for(k=j+1;k<t;k++)
			{
				if(a[k]<a[m]) m=k;			
			}
			if(m!=j)
			{
				s=a[m];
				a[m]=a[j];
				a[j]=s;
			}
		}
		for(j=0;j<t-1;j++)
		{
			m=j;
			for(k=j+1;k<t;k++)
			{
				if(b[k]>b[m]) m=k;			
			}
			if(m!=j)
			{
				s=b[m];
				b[m]=b[j];
				b[j]=s;
			}
		}
		ans=0;
		for(j=0;j<t;j++) ans+=a[j]*b[j];
		cout<<"Case #"<<i<<": "<<ans<<endl;		
	}
	return 0;
}