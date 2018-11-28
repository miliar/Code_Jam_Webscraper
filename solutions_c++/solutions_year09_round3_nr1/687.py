#include<iostream>
#include<string>
#include<sstream>
#include<map>
using namespace std;
long long A[1000];
long long B(string s,long long base)
{
	long long a=0,b=1;
	long long N=s.size();
	for(long long i=0;i<N;++i)
	{
		a+=b*A[s[N-i-1]];
		b=b*base;
	}
	return a;
}



int main()
{
	long long test;
	string s;
	cin>>test;
	for(long long i=0;i<test;++i)
	{
		cin>>s;
		printf("Case #%i: ",i+1);
		memset(A,-1,sizeof(A));
		A[s[0]]=1;
		long long T=0,base=1;
		for(long long i=1;i<s.size();++i)
		{
			if(A[s[i]]==-1)
			{
				if(T==1)
					T+=1;
				A[s[i]]=T;
				T+=1;
				base+=1;
			}
		}
		if(base==1)
			base=2;
		cout<<B(s,base)<<"\n";
	}
}