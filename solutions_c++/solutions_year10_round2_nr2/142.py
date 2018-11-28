#include<iostream>
#include<vector>
#include<algorithm>
#include<numeric>

using namespace std;

typedef unsigned long UL;
typedef unsigned long ULL;

const UL max_N=50;

int main()
{
	UL ntests;
	cin>>ntests;
	for(UL tt=1; tt<=ntests; ++tt)
	{
		UL N, K;
		ULL B, T;
		cin>>N>>K>>B>>T;
		ULL x[max_N], v[max_N];
		for(UL i=0; i<N; ++i)
			cin>>x[i];
		for(UL i=0; i<N; ++i)
			cin>>v[i];
		bool nt[max_N]; //assuming you're going alone, will you reach within T?
		for(UL i=0; i<N; ++i)
			nt[i]=((B-x[i]) <= T*v[i]);
		vector<UL> q;
		for(UL i=0; i<N; ++i)
			if(nt[i])
			{
				UL c=0;
				for(UL j=i+1; j<N; ++j)
					if(!nt[j])
						++c;
				q.push_back(c);
			}
		sort(q.begin(), q.end());
		if(q.size() >= K)
			cout<<"Case #"<<tt<<": "<<accumulate(q.begin(), q.begin()+K,0)<<'\n';
		else
			cout<<"Case #"<<tt<<": IMPOSSIBLE\n";
	}
}
