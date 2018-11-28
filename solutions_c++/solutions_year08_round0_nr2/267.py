#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <sstream>

using namespace std;

int calc(vector<pair<int,int> > events){
    sort(events.begin(), events.end());
    int ret = 0;
    int cur=0;
    for(int i=0;i<events.size();++i){
	cur += events[i].second;
	ret = max(ret,cur);
    }
    return ret;
}

int t(string s){
	    s[2]=' ';
	    istringstream ss(s);
	    int h,m;
	    ss >> h >> m;
	    return h*60+m;

}

int main(){
    int ncases;
    cin >> ncases;
    for(int cas=1;cas <= ncases;++cas){
	int T,NA,NB;
	string s;
	vector<pair<int,int> > va,vb;
	cin >>T >> NA >> NB;
	for(int i=0;i<NA;++i){
	    cin >> s;
	    va.push_back(make_pair(t(s), 1));
	    cin >> s;
	    vb.push_back(make_pair(t(s)+T, -1));	    
	}
	
	for(int i=0;i<NB;++i){
	    cin >> s;
	    vb.push_back(make_pair(t(s), 1));
	    cin >> s;
	    va.push_back(make_pair(t(s)+T, -1));	    
	}
	printf("Case #%d: %d %d\n",cas,calc(va),calc(vb));
	
    }
}
