




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

void doit(string s){

    VI v(10);
    VI w;
    w.push_back(0);
    for(int i=0;i<s.size();i++){
    	v[s[i]-'0']++;
	w.push_back(s[i]-'0');
    }
    next_permutation(w.begin(),w.end());
    for(int i=0;i<w.size();i++) if(i||w[i]) printf("%d",w[i]);
    puts("");
    string out = s;
        

}

int main(){

    int N;
    cin >> N;
    for(int kase=1;kase<=N;kase++){
        printf("Case #%d: ",kase);
	string s;
	cin >> s;
	doit(s);
    }

    return 0;
}

