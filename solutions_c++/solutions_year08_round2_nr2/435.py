#include<iostream>
#include<cmath>
#include<string>
#include<map>
#include<fstream>
using namespace std;
bool Prime[1000005];
void IsPrime()
{
	for(int i=2;i<1000000;i++)
		if(!Prime[i])
		for(int j=2;j*i<1000000;j++)
			Prime[i*j]=true;
}
map<long long,long long> Parent;
long long GetParent(long long P,map<long long,long long>&M)
{
	if(Parent[P]==P)
		return P;
	else
		GetParent(Parent[P],M);
}
int main()
{
	IsPrime();
	int C;
	long long A,B,P;
	cin>>C;
	int c=0;
	ofstream cout("c:\\prob2S.txt");
	while(C--)
	{
		
		cin>>A>>B>>P;
		for(long long i=A;i<=B;i++)
		{
			Parent[i]=i;
		}
		for(long long i=A;i<=B;i++)
		{
			for(long long j=i+1;j<=B;j++)
			{
				for(long long k=P;k<=j;k++)
					if(!Prime[k])
					if(i%k==0 && j%k==0)
					{
						if(GetParent(j,Parent)!=GetParent(i,Parent))
						{
					//		cout<<GetParent(i,Parent)<<" "<<j<<endl;
							Parent[GetParent(i,Parent)]=GetParent(j,Parent);
						}
					}
			}
		}
		int Count=0;
		for(long long i=A;i<=B;i++)
		{
		//	cout<<i<<" "<<GetParent(i,Parent)<<endl;
			if(GetParent(i,Parent)==i)
			{
				//cout<<i<<endl;
				Count++;
			}
		}
		c++;
		cout<<"Case #"<<c<<": "<<Count<<endl;

	}
	return 0;
}