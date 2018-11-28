#include<iostream>
#include<vector>



using namespace std;

typedef unsigned long UL;
typedef signed long SL;
typedef unsigned short US;
typedef signed short SS;

const UL max_B=1000;


class dsds
{
	mutable vector<UL> p;
	vector<UL> rank;
	UL nsets_;
	public:
	dsds(UL N) : p(N) , rank(N, 0) , nsets_(N)
	{
		for(UL i=0; i<N; ++i)
			p[i]=i;
	}
	
	UL rep(UL a) const
	{
		if(p[a] != a) 
			p[a] = rep(p[a]);
		return p[a];
	}
	
	dsds &merge(UL a, UL b)
	{
		a=rep(a);
		b=rep(b);
		if(a!=b)
		{
			if(rank[a] < rank[b])
				p[a]=b;
			else
				p[b]=a;
			if(rank[a]==rank[b])
				++rank[a];
			--nsets_;
		}
		return *this;
	}
	
	UL nsets() const {return nsets_;}
};

int main()
{
	vector<UL> pr;
	pr.push_back(2);
	for(UL z=3; z<=2*max_B; z+=2)
	{
		bool prime=true;
		for(UL i=0; i<pr.size() && pr[i]*pr[i]<=z; ++i)
			if(z%pr[i] == 0)
		{
			prime=false;
			break;
		}
		if(prime)
			pr.push_back(z);
	}
	UL tests;
	cin>>tests;
	for(UL tt=1; tt<=tests; ++tt)
	{
		UL A, B, P;
		cin>>A>>B>>P;
		UL startidx=0;
		for(UL i=0; i<pr.size(); ++i)
			if(pr[i]>=P)
			{
				startidx=i;
				break;
			}
		dsds d((B+1) - A);
		for(UL i=A; i<=B; ++i)
			for(UL j=i+1; j<=B; ++j)
				for(UL z=startidx; z<pr.size(); ++z)
					if(i%pr[z]==0 && j%pr[z]==0)
					{
						d.merge(i-A, j-A);
						break;
					}
		cout<<"Case #"<<tt<<": "<<d.nsets()<<'\n';
		
	}
	
}
