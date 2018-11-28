// a.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <vector>
#include <map>
#include <utility>
#include <algorithm>
//#include <cmath>
#include <cstdlib>

using namespace std;

#define fori(i_,f_,t_) for(int i_=f_;i_<t_;++i_)
#define fore(i_,c_) for(auto i_=c_.begin();i_!=c_.end();++i_)
#define pb	push_back

int ds[10001];
int ls[10001];
int ms[10000];

int main(int argc, char* argv[])
{
	int T;
	cin>>T;
	fori(t,0,T)
	{
		int N;
		cin>>N;
		
		fori(n,0,N)
		{
			cin>>ds[n]>>ls[n];
		}
		int D;
		cin>>D;

		ds[N]=D;
		ms[N]=0;
		ls[N]=D;

		for(int n=N-1;n>=0;--n)
		{
			int l = ls[n];
			int d = ds[n];

			int nn=n+1;
			int m=D+1;
			for(;ds[nn] <= d+l && nn<=N;++nn)
			{
				int ll =  ds[nn] - d;
				if (ll >= ms[nn])
				{
					m=ll;
					break;
				}
				
			}
			ms[n]=m;
		}

		cout<<"Case #"<<t+1<<": ";

        cout<<((ms[0]<=ds[0])?"YES":"NO")<<std::endl;
	}

	return 0;
}

