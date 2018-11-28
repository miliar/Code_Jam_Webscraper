



#include <string>
#include <iomanip>
#include <iostream>
#include <set>
#include <map>
#include <fstream>
#include <vector>
#include <limits>
using namespace std;

ofstream fout("SaveTheUnivOutputLarge.txt");
struct _X{
	_X(){
		cout.rdbuf(fout.rdbuf());
	}
}_x;

struct IDMan{
	IDMan():uid(0){}
	int Insert(const string&xstr)
	{
		int v = GetID(xstr);
		if( -1 == v )
		{
			v = uid++;
			id[xstr] = v;
		}
		return v;
	}
	int GetID(const string&xstr)const{
		map<string,int>::const_iterator it;
		it = id.find(xstr);
		if( id.end() == it )
			return -1;
		return it->second;
	}
	int uid;
	map<string,int> id;
};

const int inf = numeric_limits<int>::max();
const int MXQUERY = 1100;
const int MXSE= 110 ;
int qv[MXQUERY], dp[MXQUERY][MXSE];

int main()
{
	int n;
	cin>>n;
	for(int t=1;t<=n;++t)
	{
		int s;
		cin>>s;
		cin.ignore();
		IDMan im;
		for(int i=0;i<s;++i){
			string xstr;
			getline(cin,xstr);
			im.Insert(xstr);
		}
		int Q,qcnt=0;
		cin>>Q;
		cin.ignore();
		for(int i=0;i<Q;++i){
			string xstr;
			getline(cin,xstr);
			int tid = im.GetID(xstr);
			if(tid>=0)
				qv[qcnt++] = tid;
		}

		memset(dp,0,sizeof dp);
		for(int qc=0;qc<qcnt;++qc)
		{
			for(int z=0;z<s;++z){
				int &now = dp[qc+1][z];
				now = inf;
				if( qv[qc] == z )
					continue;
				if( dp[qc][z] != inf )
					now = dp[qc][z];

				for(int k=0;k<s;++k){
					if( k==z )
						continue;
					if( dp[qc][k] == inf )
						continue;
					if( now > dp[qc][k] + 1 )
						now = dp[qc][k] + 1;
				}
			}
		}
		int ans = inf;
		for(int z=0;z<s;++z){
			if( ans > dp[qcnt][z] )
				ans = dp[qcnt][z];
		}
		cout<<"Case #"<<t<<": "<<ans<<endl;
	}
}