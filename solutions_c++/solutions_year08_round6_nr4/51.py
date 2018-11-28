#include<cstdio>
#include<iostream>
#include<algorithm>
#include<vector>
#include<utility>
#include<cstdlib>

using namespace std;

typedef unsigned long UL;
typedef signed long SL;
typedef unsigned short US;
typedef signed short SS;

typedef unsigned char UC;




int main()
{
	UL tests;
	cin>>tests;
	for(UL tt=1; tt<=tests; ++tt)
	{
		UL N, M;
		cin>>N;
		vector<vector<UC> > adbig(N,vector<UC>(N, false));
		for(UL i=0; i<N-1; ++i)
		{
			UL a,b;
			cin>>a>>b;
			--a;--b;
			adbig[a][b]=adbig[b][a]=true;
		}
		cin>>M;
		vector<vector<UC> > adsm(M,vector<UC>(M, false));
		for(UL i=0; i<M-1; ++i)
		{
			UL a,b;
			cin>>a>>b;
			--a;--b;
			adsm[a][b]=adsm[b][a]=true;
		}
		vector<UL> p(N);
		for(UL i=0; i<N; ++i)
			p[i]=i;
		bool pos=false;
		do
		{
			bool thispos=true;
			for(UL i=0; i<M; ++i)
				for(UL j=i; j<M; ++j)
					if(adsm[i][j] != adbig[p[i]][p[j]])
					{
						thispos=false;
						goto notthispos;
					}
			notthispos:
			if(thispos)
			{
				pos=true;
				break;
			}
		}
		while(next_permutation(p.begin(), p.end()));
		cout<<"Case #"<<tt<<": "<<(pos?"YES\n":"NO\n");
	}
}
