#include<iostream>
#include<vector>
using namespace std;
int main()
{
freopen("A-small-attempt0.in","r",stdin);
freopen("A-small.out","w",stdout);
long N;
cin>>N;
for(int j=0;j<N;j++)
{
vector<long> v1,v2;
long n,sum=0,temp;
cin>>n;
for(int i=0;i<n;i++)
	{
	cin>>temp;
	v1.push_back(temp);
	}
for(int i=0;i<n;i++)
	{
	cin>>temp;
	v2.push_back(temp);
	}

for(int k=0;k<n;k++)
	{
	for(int l=k+1;l<n;l++)
		{
		if(v1[k]>v1[l])
			{
			temp=v1[k];
			v1[k]=v1[l];
			v1[l]=temp;
			}
		}
	}
for(int k=0;k<n;k++)
	{
	for(int l=k+1;l<n;l++)
		{
		if(v2[k]<v2[l])
			{
			temp=v2[k];
			v2[k]=v2[l];
			v2[l]=temp;
			}
		}
	}
for(int i=0;i<n;i++)
	sum+=(v1[i]*v2[i]);
cout<<"Case #"<<j+1<<": "<<sum<<endl;
}
return 0;
}
