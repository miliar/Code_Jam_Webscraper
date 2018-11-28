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

int doit(){
   int q,p;
   cin >> p >> q;
   VI lst;
   for(int i=0;i<q;i++){
       int in;
       cin >> in;
       in--;
       lst.push_back(in);
   }
   sort(lst.begin(),lst.end());
   for(int i=0;i<q;i++) cerr << lst[i] << " " ;
   cerr << endl;
   int mi = 1<<30;
   do{
       VI v(p,1);
       int cnt = 0;
       for(int i=0;i<q;i++){
           cerr << "out: " << lst[i] << endl;
           v[lst[i]]=0;
	   for(int j=lst[i]-1;j>=0 && v[j] ; j--) cnt++;
           for(int j=lst[i]+1;j<v.size() && v[j]; j++) cnt++;
       }
       cerr << "->cnt: " << cnt << endl;
       mi=min(mi,cnt);
   }while(next_permutation(lst.begin(),lst.end()));
   return mi;
}

int main(){
    int N;
    cin >> N;
    for(int kase=1;kase<=N;kase++){
        int e = doit();
	printf("Case #%d: %d\n",kase,e);
    }
    return 0;
}
