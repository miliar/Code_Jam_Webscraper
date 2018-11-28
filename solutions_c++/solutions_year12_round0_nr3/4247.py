#include<iostream>
#include<vector>
#include<map>
#include<string>
#include<sstream>
#include<cmath>
#include<algorithm>
#include<deque>
#include<set>
using namespace std;
#define ll long long
#define VI vector<ll>
#define VS vector<string>
#define PI pair<int,int>
#define MP make_pair
#define PB push_back

VI recycled(int x) {
    VI ret= VI(0,0);
    if (x<10) return ret;
    if (x>=10 && x<100) { ret.PB((x%10)*10+(x/10)); return ret; }
    if (x>=100 && x<1000) {
        ret.PB((x%10)*100+(x/10));
        ret.PB((x%100)*10+(x/100));
    }
}

int main() {
vector<VI> all;
for (int i=0;i<1000;i++) all.PB(recycled(i));
VI a1000;
a1000.PB(1);a1000.PB(10);a1000.PB(100);
all.PB(a1000);

int T;
cin>>T;
int A,B;
for (int t=1;t<=T;t++) {
    cin>>A>>B;
    int res=0;
    for (int i=A;i<=B;i++) {
        for (int j=0;j<all[i].size();j++)
            if (all[i][j]>i && all[i][j]<=B) res++;
    }
    cout<<"Case #"<<t<<": "<<res<<endl;
}



}
