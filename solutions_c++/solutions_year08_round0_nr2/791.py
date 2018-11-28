

#include <string>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <fstream>
using namespace std;


ofstream fout("TrainOutputLarge.txt");
struct _X{
	_X(){
		cout.rdbuf(fout.rdbuf());
	}
}_x;


const int MX = 200;

struct Train{
	bool operator<(const Train&rhs)const{
		if(start!=rhs.start)
			return start<rhs.start;
		return arrive<rhs.arrive;
	}
	int start,arrive;
	int dr;
};
Train train[MX*MX];


int GetTime(const string&str)
{
	istringstream is(str);
	int h,m;
	char x;
	is>>h>>x>>m;
	return h*60+m;
}

int gnc,gtat;
void dfs(int now)
{
	const int orgDr = train[now].dr;
	train[now].dr = 2;
	for(int i=now+1;i<gnc;++i){
		if( train[i].dr > 1 )
			continue;
		if( orgDr + train[i].dr != 1 )
			continue;
		if( train[now].arrive + gtat > train[i].start )
			continue;
		dfs(i);
		break;
	}
}


int main()
{
	int n;
	cin>>n;
	for(int t=1;t<=n;++t)
	{
		int na,nb;
		cin>>gtat>>na>>nb;
		int nc=0;
		for(int i=0;i<na;++i){
			string op,ed;
			cin>>op>>ed;
			train[nc].dr = 0;
			train[nc].start = GetTime(op);
			train[nc].arrive= GetTime(ed);
			++nc;
		}
		for(int i=0;i<nb;++i){
			string op,ed;
			cin>>op>>ed;
			train[nc].dr = 1;
			train[nc].start = GetTime(op);
			train[nc].arrive= GetTime(ed);
			++nc;
		}
		int ans[]={0,0};
		gnc = nc;
		sort(train,train+gnc);
		for(int i=0;i<nc;++i){
			if( train[i].dr > 1 )
				continue;
			++ans[train[i].dr];
			dfs(i);
		}
		cout<<"Case #"<<t<<": "<<ans[0]<<' '<<ans[1]<<endl;
	}
}