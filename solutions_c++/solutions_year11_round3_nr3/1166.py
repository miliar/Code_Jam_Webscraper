#include<iostream>
#include<vector>
using namespace std;
long long int gcd(long long int n1,long long int n2)
{
	//	cout<<"called";
	if(n1<n2)
	{
		long long int temp=n1;
		n1=n2;
		n2=temp;
	}
	if(n1%n2==0)
		return n2;
	else
		return gcd(n2,n1%n2);
}
int main()
{
	int note;
	cin>>note;
	for(int caseno=1;caseno<=note;caseno++)
	{
		cout<<"Case #"<<caseno<<": ";
//		cout<<100000000000000000000<<endl;
		long long int n,l,h;
		cin>>n>>l>>h;
		long long int inp;
		vector<int> freq;
		for(long long int i=1;i<=n;i++)
		{
			cin>>inp;
			freq.push_back(inp);
		}
		bool found=0;
                for(long long int i=l;i<=h;i++)
		{
			bool correct=1;
			for(int j=0;j<freq.size();j++)
				if(freq[j]%i!=0&&i%freq[j]!=0)
				{correct=0;break;}
			if(!correct)
				continue;
			else
			{cout<<i<<endl;found=1;break;}
		}
		if(!found)
			cout<<"NO"<<endl;
		


	}


}
