#include<iostream>
#include<string>
#include<algorithm>
#include<cassert>

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
		UL k;
		cin>>k;
		string s;
		getline(cin, s);
		getline(cin, s);
		assert(s.size()%k==0);
		UL p[7]={0,1,2,3,4,5,6};
		UL ans=numeric_limits<UL>::max();
		do
		{
			string z;
			z.resize(s.size());
			for(UL b=0; b<s.size()/k; ++b)
			{
				for(UL i=0; i<k; ++i)
					z[k*b+i]=s[k*b+p[i]];
			}
			UL g=1;
			for(UL i=1; i<z.size(); ++i)
				if(z[i] != z[i-1])
					++g;
			ans=min(ans, g);
			
		}while(next_permutation(p, p+k));
		cout<<"Case #"<<tt<<": "<<ans<<'\n';
	}
}
