#include <iostream>
#include <vector>
#include <map>
#include <set>

#define fir first
#define sec second

using namespace std;

typedef pair<int,int> PII;

const int MOD=10007;
set<PII> rocks;
map<PII,int> mem;

bool ok(int y, int x){
    return y>0 && x>0;
}

int solve(int y, int x){
    if (!ok(y,x)) return 0;
    if (y==1 && x==1) return 1;
    PII cur=PII(y,x);
    if (rocks.count(cur)) return 0;
    if (mem.count(cur)) return mem[cur];
    return mem[cur]=(solve(y-1,x-2)+solve(y-2,x-1))%MOD;
}

int main(){
    int n;
    cin>>n;
    for (int cn=0;cn<n;++cn){
        int h,w,r;
        cin>>h>>w>>r;
        rocks.clear();
        for (int i=0;i<r;++i){
            int y,x;
            cin>>y>>x;
            rocks.insert(PII(y,x));
        }
        mem.clear();
        int ans=solve(h,w);
        cout<<"Case #"<<cn+1<<": "<<ans<<endl;
    }
}
