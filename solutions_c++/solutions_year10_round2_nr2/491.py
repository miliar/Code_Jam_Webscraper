#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define _for(i,x,n) for(int i=x;i<n;i++)
#define _ifor(i,x,n) for(int i=(n);i>=x;i++)
#define _forv(it,v) for(typeof((v).begin()) it=(v).begin(); it!=(v).end(); it++)

#define _dv(var) cout<<"L"<<__LINE__<<": "<<#var<<": "<<var<<endl;
#define _dav(i,f) cout<<"L"<<__LINE__<<": "<<#i<<"-"<<#f<<": "; dav(i,f);
template<typename it> void dav(it i,it f)
	{ cout<<"[ "; while(i!=f) cout<<*(i++)	<<" "; cout<<"]"<<endl; }
#define _ln cout<<"_ln: "<<__LINE__<<endl;



int main()
{
	int C;
	cin>>C;
	for(int Z=1;Z<=C;Z++)
	{
		int N,K,B,T;
		cin>>N>>K>>B>>T;
		int pos[N];
		int vel[N];
		for(int i=0;i<N;i++)
			cin>>pos[i];
		for(int i=0;i<N;i++)
			cin>>vel[i];
		int res=0;
		int k=0;
		for(int j=N-1;j>=0 && k<K;j--)
			//si llega
			if(vel[j]*T + pos[j] >= B)
			{
				//se cuentan cuantos debe saltar
				for(int i=j+1;i<N;i++)
				{
					//no llega, hay q saltarlo
					if(vel[i]*T + pos[i] < B)
						res++;
				}
				k++;
			}
		if(k<K)
			cout<<"Case #"<<Z<<": IMPOSSIBLE"<<endl;
		else
			cout<<"Case #"<<Z<<": "<<res<<endl;
	}

	return 0;
}
