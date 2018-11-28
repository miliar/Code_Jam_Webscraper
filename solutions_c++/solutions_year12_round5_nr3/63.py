#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <numeric>
#include <set>
#include <map>
#include <queue>
#include <cmath>
#include <cstdio>
#include <cstring>
using namespace std;

#define debug(x) cerr<<#x<<"="<<(x)<<endl;
#define ll long long

int F, N;
ll M;
pair<ll, ll> food[200];

typedef pair<ll, double> big;
bool good(big x){
    return x.second<2e18;
}

bool lt(big x, big y){
    if(good(x) && good(y)){
        return x.first<y.first;
    }
    return (x.second < y.second);
}

big cost(ll days){
    big res=make_pair(F, F);
    ll last=0;
    for(int i=0; i<N && last<days; i++){
        ll del=max(min(days, food[i].first)-last, 0ll);
        last+=del;
        res.first+=del*food[i].second;
        res.second+=(double)del*food[i].second;
    }
    if(last<days)
        res.second+=(days-last)*1e50;
    return res;
}

big e(ll days, ll deliv){
    int d1=days/deliv;
    int count2=days%deliv;
    int count1=deliv-count2;
    big res(0, 0.);
    big c1=cost(d1);
    res=make_pair(c1.first*count1, c1.second*count1);
    if(count2){
        c1=cost(d1+1);
        res=make_pair(res.first+c1.first*count2, res.second+c1.second*count2);
    }
    return res;
}

bool can(ll days){
    ll lo=0, hi=days+1;
#if 0
    while(lo+2<hi){
        ll m1=(2*lo+hi)/3;
        ll m2=(lo+2*hi)/3;
        big cost1=e(days, m1);
        big cost2=e(days, m2);
        if(good(cost1) && cost1.first<=M)
            return true;
        if(good(cost2) && cost2.first<=M)
            return true;
        if(lt(cost1, cost2)){
            hi=m2;
        }else
            lo=m1;
    }
#else
    for(ll d=1; d<=days; d++){
        big cost=e(days, d);
        if(good(cost) && cost.first<=M)
            return true;
    }
#endif
    return false;
}

void eval(){
    cin>>M>>F>>N;
    for(int i=0; i<N; i++){
        cin>>food[i].first>>food[i].second;
        food[i].second++;
    }
    sort(food, food+N);
    for(int i=0; i<N; i++){
        swap(food[i].first, food[i].second);
    }

    ll lo=0, hi=M+1;
    while(lo+1<hi){
        ll mid=(lo+hi)/2;
        if(can(mid))
            lo=mid;
        else
            hi=mid;
    }
    cout<<lo<<endl;
}

int main(){
	int cases;
	string line;
	getline(cin, line);
	istringstream(line)>>cases;
	for(int i=1; i<=cases; i++){
		cout<<"Case #"<<i<<": ";
		eval();
	}
	return 0;
}
