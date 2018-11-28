#include<ctime>
#include<string>
#include<vector>
#include<sstream>
#include<iostream>
#include<algorithm>
#include<queue>
#include<stack>
#include<set>
#include<map>
#include<numeric>
#include<cmath>
#include<locale>
using namespace std;
#define all(x) (x).begin(),(x).end()
#define sz(a) (int((a).size()))
#define tr(c,it) for(typeof((c).begin()) it = (c).begin(); it != (c).end(); it++)
typedef istringstream iss; typedef ostringstream oss; typedef long long int lli;
const double TOLL=1e-9;

int main()
{
	int n,na,nb; 
	cin>>n; vector<int>  aready,bready; string st,end;
	vector<pair<int,int> > atime, btime; int T;
	for(int cn=1;cn<=n;cn++)
	{
		cin>>T;
		aready.clear(); bready.clear(); atime.clear(); btime.clear();
		cin>>na>>nb;
		int mint=1000000000; bool a=true;
		for(int i=0;i<na;i++)
		{
			cin>>st>>end;
			st[2]=end[2]=' ';
			int stime=((st[0]-'0')*10+(st[1]-'0'))*60+((st[3]-'0')*10+(st[4]-'0'));
			int etime=((end[0]-'0')*10+(end[1]-'0'))*60+((end[3]-'0')*10+(end[4]-'0'));
			atime.push_back(make_pair(stime,etime));
			if(stime<mint) mint=stime, a=true;
		}
		for(int i=0;i<nb;i++)
		{
			cin>>st>>end;
			st[2]=end[2]=' ';
			int stime=((st[0]-'0')*10+(st[1]-'0'))*60+((st[3]-'0')*10+(st[4]-'0'));
			int etime=((end[0]-'0')*10+(end[1]-'0'))*60+((end[3]-'0')*10+(end[4]-'0'));
			btime.push_back(make_pair(stime,etime));
			if(stime<mint) mint=stime, a=false;
		}
		sort(all(atime)); sort(all(btime));
		int atrain=0, btrain=0;
		if(a) atrain++; else btrain++;
		int ainit=atrain, binit=btrain;

		for(int time=0;time<=1440;time++)
		{
			for(int i=sz(aready)-1;i>=0;i--) if(aready[i]<=time) atrain++, aready.erase(aready.begin()+i);
			for(int i=sz(bready)-1;i>=0;i--) if(bready[i]<=time) btrain++, bready.erase(bready.begin()+i);
			bool YES=false;
			for(int i=0;i<sz(atime);i++) if(atime[i].first==time)
			{
				if(!atrain) ainit++;
				else atrain--;
				bready.push_back(atime[i].second+T);
			}
			for(int i=0;i<sz(btime);i++) if(btime[i].first==time)
			{
				if(!btrain) binit++;
				else btrain--;
				aready.push_back(btime[i].second+T);
			}

		}
		cout<<"Case #"<<cn<<": "<<ainit<<' '<<binit<<endl;

	}

	return 0;
}
