#include <iostream>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <map>
using namespace std;

map<int,int> M;

bool can(double dist,double mD)
{
	double lim = -(1e8);
	for(map<int,int>::iterator it = M.begin(); it!= M.end() ; ++it)
	{
		//cout<<lim<<endl;
		double delta = (it->first) - lim;
		if(delta > 0)
		{
			double lowb = max(lim, double((it->first) - dist));
			double upb = (it->first) + dist;
			double midb = mD * (it->second - 1);
			//cout<<lowb<<" "<<upb<<" "<<(it->first)<<"    "<<dist<<"    People: "<<(it->second)<<" , "<<mD<<endl;
			if(midb<=upb-lowb){lim = lowb + midb + mD;}
			else return false;
		}else{
			double lowb = lim;
			double upb = (it->first) + dist;
			if(lowb > upb)return false;
			double midb = mD * (it->second - 1);
			if(midb<=upb-lowb)lim = lowb + midb + mD;
			else return false;
		}
	}
	return true;
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int TC;
	cin>>TC;
	for(int tc = 1; tc<=TC; ++tc)
	{
		int N,D;
		cin>>N>>D;
		M.clear();
		for(int i = 0; i < N; ++i)
		{
			int p,v;
			cin>>p>>v;
			M[p] = v;
		}
		double lo = 0, hi = int(1e8);
		while(hi - lo > 1e-8)
		{
			double mid = (lo+hi)/2;
			//cout<<endl<<endl;
			if(can(mid,double(D)))hi = mid;
			else lo = mid;
		}
		printf("Case #%d: %0.7lf\n",tc,lo);
	}
	return 0;
}