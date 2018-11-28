#include<iostream>
#include<vector>
using namespace std;
int main()

{
freopen("A-small-attempt0.in","r",stdin);
freopen("A-small.out","w",stdout);
long N;
cin>>N;
for(int f=0;f<N;f++)
{
vector<long> v;
long p,k,l,temp,sum=0;
cin>>p>>k>>l;
for(long i=0;i<l;i++)
	{
	cin>>temp;
	v.push_back(temp);
	}
for(long i=0;i<l;i++)
	{
	for(long j=i;j<l;j++)
		{
		if(v[i]<v[j])
			{
			temp=v[i];
			v[i]=v[j];	
			v[j]=temp;
			}
		}
	}
/*for(long i=0;i<l;i++)
cout<<v[i]<<" ";*/
for(long i=0;i<l;i++)
	{
	sum=sum+(((i/k)+1)*v[i]);
	}
cout<<"Case #"<<f+1<<": "<<sum<<endl;
}
return 0;
}

