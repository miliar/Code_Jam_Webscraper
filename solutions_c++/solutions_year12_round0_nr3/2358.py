#include<iostream>
#include <vector>
#include <set>
using namespace std;

int myshift(int n, int s,int s2)
{
	return (n%s)*s2+n/s;
}
int main()
{
	int T;
	cin>>T;
	for(int i=0;i<T;i++)
	{
	int A,B;
	cin>>A>>B;
	int ret=0;
	for(int n=A;n<B;n++)
	{
		int len=0;
		int nn=n;
		int s2=1;
		while(nn>0)
		{
			len++;
			nn=nn/10;
			s2*=10;
		}
		set<int> myset;
		s2/=10;
		int s=10;

		while(s2>0)
		{
			int tmp=myshift(n,s,s2);
			bool newval=myset.insert(tmp).second;
			if (tmp<=B&& tmp>n && newval)
				ret++;
			s2/=10;
			s*=10;
		}
	}

	
	cout<<"Case #"<<i+1<<": "<<ret<<endl;
	}
}
