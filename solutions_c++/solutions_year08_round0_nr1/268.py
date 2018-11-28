#include <iostream>
#include <cstdio>
#include <vector>
#include <string>

using namespace std;

int cac[1010][110];

vector<string> names;
vector<string> queries;
// i know dp is overkill..

int go(int pos,int cur){
    if(pos == queries.size()) return 0;
    int &ret = cac[pos][cur];
    if(ret >= 0) return ret;
    ret = 100000;
    if(names[cur] != queries[pos]) ret = go(pos+1,cur);
    for(int i=0;i<names.size();++i){
	if(names[i] != queries[pos]) ret = min(ret,1+go(pos+1,i));
    }
    return ret;
}


int main(){
    int ncases;
    cin >> ncases;
    for(int cas=1;cas<=ncases;++cas){
	names.clear();
	queries.clear();
	memset(cac,-1,sizeof(cac));
	int ret=10000;
	int N,M;
	cin >> N;
	char buf[10000];
	cin.getline(buf,sizeof(buf));
	for(int i=0;i<N;++i){
	    cin.getline(buf,sizeof(buf));
	    names.push_back(buf);
	}
	cin >> M;
	cin.getline(buf,sizeof(buf));
	for(int i=0;i<M;++i){
	    cin.getline(buf,sizeof(buf));
	    queries.push_back(buf);
	}
	for(int i=0;i<names.size();++i) ret = min(ret,go(0,i));
	printf("Case #%d: %d\n",cas,ret);
    }
}
