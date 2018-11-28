#include<cstdio>
#include<iostream>
#include<algorithm>
#include<vector>
#include<utility>
#include<cstdlib>
#include<limits>
#include<set>
#include<cassert>

using namespace std;

typedef unsigned long UL;
typedef signed long SL;
typedef unsigned short US;
typedef signed short SS;

typedef pair<UL, UL> an;

const UL inv=numeric_limits<UL>::max();

/*inline bool order(UL a, UL b, UL c)
{
	return ( incr(a,b,c) || decr(a,b,c) );
}*/

inline bool incr(UL a, UL b, UL c)
{
	return( a<=b && b<=c);
}

inline bool decr(UL a, UL b, UL c)
{
	return( a>=b && b>=c);
}

inline bool mmrange(UL min, UL max, UL a, UL b)
{
	assert(min<=max);
	return(incr(max,a,b) || decr(min,a,b));
}

int main()
{
	UL tests;
	cin>>tests;
	for(UL tt=1; tt<=tests; ++tt)
	{
		UL N;
		cin>>N;
		set<an> nonbs;
		vector<an> nonbv;
		UL hmin=inv, hmax=0, wmin=inv, wmax=0;
		bool birdexist=false;
		for(UL i=0; i<N; ++i)
		{
			UL H,W;
			cin>>H>>W;
			string s;
			cin>>s;
			if(s=="BIRD")
			{
				hmin=min(hmin, H);
				hmax=max(hmax, H);
				wmin=min(wmin, W);
				wmax=max(wmax, W);
				birdexist=true;
			}
			else
			{
				cin>>s;
				nonbs.insert(an(H,W));
				nonbv.push_back(an(H,W));
			}
		}
		cout<<"Case #"<<tt<<":\n";
		const string UN="UNKNOWN\n", BR="BIRD\n", NB="NOT BIRD\n";
		UL M;
		cin>>M;
		if(birdexist)
		{
			for(UL i=0; i<M; ++i)
			{
				UL H,W;
				cin>>H>>W;
				if(hmin <= H && H <= hmax && wmin <= W && W <= wmax)
				{
					cout<<BR;
					continue;
				}
				bool pos=true;
				for(UL j=0; j<nonbv.size(); ++j)
				{
					const UL nbH=nonbv[j].first, nbW=nonbv[j].second;
					/*if(hmin<=H && H<=hmax)
						if(incr(wmax, nbW, W) || decr(wmin, nbW, W))
						{
							cout<<NB;
							goto NEXTBIRD;
						}
					if(wmin<=W && W<=wmax)
						if(incr(hmax, nbH, H) || decr(hmin, nbH, H))
						{
							cout<<NB;
							goto NEXTBIRD;
						}
					if(*/
					if(incr(hmin, nbH, hmax) && mmrange(wmin, wmax, nbW, W) )
					{
						pos=false;
						break;
					}
					if(incr(wmin, nbW, wmax) && mmrange(hmin, hmax, nbH, H) )
					{
						pos=false;
						break;
					}
					if(mmrange(wmin, wmax, nbW, W) && mmrange(hmin, hmax, nbH, H))
					{
						pos=false;
						break;
					}
				}
				cout<<(pos?UN:NB);
			}
		}
		else
		{
			for(UL i=0;i<M;++i)
			{
				UL H,W;
				cin>>H>>W;
				cout<<((nonbs.find(an(H,W))==nonbs.end())?UN:NB);
			}
		}
	}

}
