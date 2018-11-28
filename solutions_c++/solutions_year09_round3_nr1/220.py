#include <iostream> 
#include <queue>
#include <algorithm>
#include <vector>
#include <cassert>
#include <map>
#include <cmath>
#include <set>
#include <string>
#include <cstring>
#include <cstdio>

#ifdef D 
#define D 1
#else 
#define D 0
#endif

using namespace std; // insert push_back find size begin first second

typedef unsigned long long ULL;
typedef long long LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int,int> PII;
typedef map<int,int> MII;
typedef vector<PII> VPII;
typedef set<int> SI;

ULL doit(string s){
    VI mmap(128,-1);
    VI given(36);
    mmap[s[0]]=1;
    given[1] = 1;
    int giv_cnt = 0;
    for(int i=1;i<(int)s.size();i++){
        if(mmap[s[i]]==-1){
            while(given[giv_cnt]) giv_cnt++;
	    assert(given[giv_cnt]==0);
	    mmap[s[i]]=giv_cnt;
	    given[giv_cnt] = 1;
	}
    }
    for(int i=0;i<128;i++)
    	if(mmap[i]!=-1) cerr << i << " -> " << mmap[i] << endl;
    ULL base = max(giv_cnt+1,2);
    ULL ret = 0;
    ULL pw = 1;
    cerr << "base: "<< base << endl;
    reverse(s.begin(),s.end());
    for(int i=0;i<(int)s.size();i++){
        ret+=pw*mmap[s[i]];
	pw*=base;
	cerr << "pw: " << pw << endl;
    }
    return ret;
}

int main(){
    int N;
    cin >> N;
    for(int kase=1;kase<=N;kase++){
        string s;
        cin >> s;
        ULL e = doit(s);
	printf("Case #%d: %llu\n",kase,e);
    }
    return 0;
}
