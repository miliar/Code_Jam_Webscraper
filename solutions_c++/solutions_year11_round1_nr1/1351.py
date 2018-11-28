#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <map>

using namespace std;

#define REP(i,n) for(int i=0;i<(int)n;++i)
#define rep(i,s,n) for(int i=s;i<(int)n;++i)
#define FOR(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)

namespace
{
}

int ucd(long long a, long long b)
{
    if(b>a){
        return ucd(b, a);
    }
    if(a%b==0){
        return b;
    }else{
        return ucd(b, a%b);
    }
}
int lcm(int a, int b)
{
    return (a*b)/ucd(a, b);
}

int main()
{
    int T;
    cin >> T;
    REP(i, T){
        long long N, Pd, Pg;
        cin >> N >> Pd >> Pg;
        
        if(Pd==0 && Pg==0){
            cout << "Case #" << (i+1) << ": Possible" << endl;
            continue;
        }
        if(Pd==0 || Pg==0){
            cout << "Case #" << (i+1) << ": Broken" << endl;
            continue;
        }

        long long dcandidate=ucd(Pd, 100);
        long long gcandidate=ucd(Pg, 100);
        long long lossDMin=(100-Pd)/dcandidate;
        long long totalDMin=100/dcandidate;
        long long lossGMin=(100-Pg)/gcandidate;
        long long totalGMin=100/gcandidate;

        if(lossGMin==0 && lossDMin==0){
            cout << "Case #" << (i+1) << ": Possible" << endl;
            continue;
        }

        if(lossGMin==0){
            cout << "Case #" << (i+1) << ": Broken" << endl;
            continue;
        }
        long long m=(lossDMin%lossGMin==0) ? lossDMin/lossGMin : (lossDMin/lossGMin)+1;
        if(m==0) m=1;
        long long totalD=totalDMin*m;
        //cout << totalD << endl;
        if(totalD<=N){
            cout << "Case #" << (i+1) << ": Possible" << endl;
        }else{
            cout << "Case #" << (i+1) << ": Broken" << endl;
        }
        
    }
    return 0;
}
