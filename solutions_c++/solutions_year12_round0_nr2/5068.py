#include<iostream>
#include<algorithm>

int foo(int* in,int N, int S,int p,int now,int added)
{
	if(now == N)
	{
		if(added > S) return S;
		return added;
	}

	if(in[now] == 0)
	{
		if(p == 0) return 1 + foo(in,N,S,p,++now,added);
		return foo(in,N,S,p,++now,added);
	}
	if(in[now] == 1)
	{
		if(p == 1) return 1 + foo(in,N,S,p,++now,added);
		return foo(in,N,S,p,++now,added);
	}
	int a,b,c;

	a = in[now]/3;
	b = in[now]/3;
	c = in[now]/3;

	if(in[now]%3 == 1)
	{
		c++;
		
		if(a >= p) return 1 + foo(in,N,S,p,++now,added);
		if(c >= p) return 1 + foo(in,N,S,p,++now,added);
		return foo(in,N,S,p,++now,added);
	}

	if(in[now]%3 == 2)
	{
		b++;
		c++;

		if(a >= p) return 1 + foo(in,N,S,p,++now,added);
		if(b >= p) return 1 + foo(in,N,S,p,++now,added);
		if(b == p - 1) return foo(in,N,S,p,++now,++added);
		return foo(in,N,S,p,++now,added);
	}

	if(a >= p) return 1 + foo(in,N,S,p,++now,added);
	if(a == p - 1) return foo(in,N,S,p,++now,++added);
	return foo(in,N,S,p,++now,added);
}

int main()
{
	int T,N,S,p;
	int lst[100];

	std::cin>>T;
	for(int i=1;i<=T;i++)
	{
		std::cin>>N>>S>>p;
		for(int j=0;j<N;j++)
		{
			std::cin>>lst[j];
		}
		std::cout<<"Case #"<<i<<": "<<foo(lst,N,S,p,0,0)<<std::endl;
	}
	return 0;
}