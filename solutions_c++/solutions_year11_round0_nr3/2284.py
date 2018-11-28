#include<iostream>
#include<fstream>
using namespace std;

int main()
{
	ifstream cin("in.txt");
	ofstream cout("out.txt");
	int a[1050];
	int sum[1050];
	int t[1050];
	int T;
	int k,kk;
	cin>>T;

	for(kk=1; kk<=T; kk++)
	{
		int n;
		cin>>n;
		int i,j;
		for(i=0; i<n; i++)
			cin>>a[i];
	//	sort(a);
		sum[0]=a[0];
		//s[n-1]=a[n-1];
		t[0]=a[0];
		for(k=1; k<n; k++)
		{
			t[k]=t[k-1]^a[k];
		//	s[i]=s[i+1]^a[i];
			sum[k]=sum[k-1]+a[k];
		}
	int max;
	max=-1;
	for(i=0; i<n; i++)
		for(j=i; j<n; j++)
		{
			if(i==0)
			{
				if(t[j]==(t[n-1]^t[j]))
				{
					if(sum[n-1]-sum[j]>max)
						max=sum[n-1]-sum[j];
				}
			}
			else
			{
				if((t[j]^t[i-1])==(t[n-1]^(t[j]^t[i-1])))
				{
					if(sum[n-1]-(sum[j]-sum[i-1])>max)
						max=sum[n-1]-(sum[j]-sum[i-1]);
				}
			}
		}
		if(max==-1)
			cout<<"Case #"<<kk<<": "<<"NO"<<endl;
		else
		cout<<"Case #"<<kk<<": "<<max<<endl;
	
	}	
	return 0;
}