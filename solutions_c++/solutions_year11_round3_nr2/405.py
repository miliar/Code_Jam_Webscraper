#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <map>

using namespace std;

#define REP(i,n) for(int i=0;i<(int)n;++i)
#define rep(i,s,n) for(int i=s;i<(int)n;++i)
#define FOR(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
typedef long long int ll;

namespace
{
}

struct Star{
    ll distance;
    ll n;
};

bool operator<(const Star &a, const Star &b){
    return a.distance < b.distance;
}
bool operator>(const Star &a, const Star &b){
    return a.distance > b.distance;
}

int main()
{
    int T;
    cin >> T;
    REP(i, T){
        ll L, t, N, C;
        bool boostAvailable=true;
        cin >> L >> t >> N >> C;
        vector<Star> a(C);
        ll aroundTime=0;
        ll remainTime;
        ll total, n;
        REP(j, C){
            cin >> a[j].distance;
            aroundTime+=a[j].distance;
            a[j].n=(j<N%C ? 1 : 0)+N/C;
        }
        // ブースター作成時間分、減らす
        aroundTime*=2;
        if(N/C < (t/aroundTime)){
            boostAvailable=false;
            goto withoutBoost;
        }
        FOR(it, a){
            (*it).n-=(t/aroundTime);
        }
        remainTime=t%aroundTime;
        //cout << aroundTime << ", " << remainTime << endl;
        FOR(it, a){
            //cout << remainTime << endl;
            if(remainTime<(*it).distance*2){
                (*it).n-=1;
                Star s;
                s.distance=(*it).distance-(remainTime/2);
                s.n=1;
                a.push_back(s);
                break;
            }else{
                (*it).n-=1;
                remainTime-=(*it).distance*2;
            }
        }

        sort(a.begin(), a.end(), greater<Star>());
/*
        FOR(it, a){
            cout << (*it).distance << ", " << (*it).n << endl;
        }
*/

        total=0;
        n=0;
        FOR(it, a){
            if((*it).n<=(L-n)){
                total+=((*it).distance*(*it).n);
                n+=(*it).n;
            }else{
                total+=((*it).distance*(L-n));
                n+=(L-n);
                break;
            }
        }
        //cout << total << ", " << n << endl;

        // 時短をせずに渡航した場合
      withoutBoost:
        ll noBoost=0;
        FOR(it, a){
            noBoost+=((*it).distance*(*it).n)*2;
        }
        ll withBoost=noBoost-total+t;

        //cout << "NoBoost: " << noBoost << endl;
        //cout << "WithBoost: " << withBoost << endl;
        if(boostAvailable){
            cout << "Case #" << (i+1) << ": " << withBoost << endl;
        }else{
            cout << "Case #" << (i+1) << ": " << noBoost << endl;
        }
    }
    return 0;
}
