#include<iostream>
#include<limits>
#include<algorithm>

using namespace std;

typedef unsigned long UL;

//final is match 0, the left and right children of match i are 2*i+1 and 2*i+2 respectively

const UL inv=numeric_limits<UL>::max();

const UL max_P = 10;
const UL max_N = (1UL<<max_P)-1; //number of matches
const UL max_T = 1UL<<max_P; //number of teams

struct D
{
	UL d[max_P]; //d[i] = min cost for a certain subtree, if I'm buying i tickets strictly on the path to the root
	UL &operator[](const size_t z){return d[z];}
};

UL P,N,T;
UL prices[max_N];
UL M[max_T];

UL add(UL a, UL b)
{
	if(a==inv || b==inv)
		return inv;
	else return a+b;
}

UL add(UL a, UL b, UL c)
{
	if(a==inv || b==inv || c==inv)
		return inv;
	else return a+b+c;
}

D f(UL z) //match no z
{
	//cerr<<"aa"<<z<<'\n';
	if(2*z + 1 < N) //not a leaf
	{
		//cerr<<"bb"<<z<<'\n';
		D ret;
		D a1 = f(2*z+1), a2 = f(2*z+2);
 		//cerr<<"cc"<<z<<'\n';
		for(UL j=0; j<P-1; ++j)
			ret[j] = min(add(a1[j], a2[j]), add(prices[z], a1[j+1], a2[j+1]));
		ret[P-1] = add(a1[P-1], a2[P-1]);
		return ret;
	}
	else //leaf
	{
		//cerr<<"xx"<<z<<'\n';
		const UL c = z - ( (1UL<<(P-1))-1);
		const UL mustwatch = P - min(M[2*c], M[2*c+1]);
		D ret;
		for(UL i=0; i+2<=mustwatch; ++i)
			ret[i] = inv;
		if(mustwatch != 0)
			ret[mustwatch-1] = prices[z];
		for(UL i=mustwatch; i<P; ++i)
			ret[i]=0;
		return ret;
	}
}

int main()
{
	UL ntests;
	cin>>ntests;
	for(UL tt=1; tt<=ntests; ++tt)
	{
		cin>>P;
		N=(1UL<<P)-1;
		T=1UL<<P;
		for(UL i=0; i<T; ++i)
			cin>>M[i];
		for(UL i=P; i>0; --i)
			for(UL j=(1UL<<(i-1))-1; j<(1UL<<i)-1;++j)
				cin>>prices[j];
		
		cout<<"Case #"<<tt<<": "<<f(0)[0]<<'\n';
	}
}
