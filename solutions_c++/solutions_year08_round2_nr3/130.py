#include<iostream>
#include<vector>
#include<list>



using namespace std;

typedef unsigned long UL;
typedef signed long SL;
typedef unsigned short US;
typedef signed short SS;


int main()
{
	UL tests;
	cin>>tests;
	for(UL tt=1; tt<=tests; ++tt)
	{
		UL K;
		cin>>K;
		vector<UL> a(K);
		list<UL> z;
		for(UL i=0; i<K; ++i)
			z.push_back(i);
		list<UL>::iterator curpos=z.begin();
		for(UL n=1; n<=K; ++n)
		{
			for(UL ct=1; ct<n; ++ct)
			{
				++curpos;
				if(curpos==z.end())
					curpos=z.begin();
			}
			a[*curpos]=n;
			list<UL>::iterator tmp=curpos;
			++curpos;
			if(curpos==z.end())
				curpos=z.begin();
			z.erase(tmp);
		}
		cout<<"Case #"<<tt<<":";
		UL n;
		cin>>n;
		for(UL i=0; i<n; ++i)
		{
			UL idx;
			cin>>idx;
			--idx;
			cout<<' '<<a[idx];
		}
		cout<<'\n';
	}
}
