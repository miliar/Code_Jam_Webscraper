#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include <numeric>
#include <iostream>
#include <algorithm>
#include <functional>
using namespace std;

typedef vector<int> VI;
typedef vector<string> VS;
#define FORC(x) for(int i=0;i<(int)(x).size();++i)
#define SHOW(v,t,sep) copy((v).begin(),(v).end(),ostream_iterator<t>(cout,sep));cout << endl;
#define MSG(X) cout << #X << "=" << X << endl
#define COPY(s,v) copy((s),(s+sizeof(s)/sizeof(s[0])),back_inserter(v));

int main(int argc,char**argv){
	if(argc<=1){cout << "input arg\n";return 1;}
	ifstream ifs;
	ifs.open(argv[1],ios_base::in);
	if(!ifs){cout << "fstream error\n";return 1;}
	char str[1001];
	if(!ifs.eof())ifs.getline(str,1001);
	int n = atoi(str);
	for(int i=0;i<n;++i){
		VS e;
		VS q;
		e.clear();
		q.clear();
		if(!ifs.eof())ifs.getline(str,1001);
		int engine=atoi(str);
		for(int j=0;j<engine;++j){
			ifs.getline(str,1001);
			e.push_back(str);
		}
//		SHOW(e,string," ");
		if(!ifs.eof())ifs.getline(str,1001);
		int query=atoi(str);
		for(int j=0;j<query;++j){
			ifs.getline(str,1001);
			q.push_back(str);
		}
//		SHOW(q,string," ");

		int result=0;
		int pos=0;
		VI dist(e.size());
		while(1){
			for(int j=0;j<e.size();++j){
				VS::iterator qi = find(q.begin()+pos,q.end(),e[j]);
				if( qi ==q.end()){goto END;}
				dist[j]=qi - q.begin();
			}
//			SHOW(dist,int," ");
			pos=*max_element(dist.begin(),dist.end());
			result++;
		}
END:
		cout << "Case #" << i+1 << ": " << result << endl;
	}
	ifs.close();
	return 0;
}