#include<iostream>
using namespace std;

int main()
{
	int T,k=0,N,S,p,t[200];
	cin>>T;
	while(T--)
	{
		cin>>N>>S>>p;
		for(int i=0;i<N;i++)
			cin>>t[i];
		int sc1=p*3;
		int sc2=sc1-2;
		int sc3=sc1-4;
		//if(sc3<=0)
			//sc3=1;
		int sur=0,max=0;
		for(int i=0;i<N;i++)
		{
			if(t[i]>=sc2)
			{
				max++;
				//cout<<t[i]<<" is a SC2"<<endl;
			}
			
			if(sur<S && t[i]<=sc2&&t[i]>=sc3&&t[i]!=0)
			{
				max++;
				sur++;
				//cout<<t[i]<<" is a SC3"<<endl;
			}
		}
		cout<<"Case #"<<++k<<": "<<max<<endl;
		
		
	}
	return 0;
}
