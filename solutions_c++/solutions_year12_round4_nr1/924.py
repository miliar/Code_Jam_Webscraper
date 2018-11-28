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

int main() {
    int T;
    cin>>T;
    for (int t=0;t<T;t++) {
        cout<<"Case #"<<t+1<<": ";
        int N; cin>>N;
        VI d = VI(N+1,0);
        VI l = VI(N+1,0);
        for (int i = 0; i <N;i++) cin>>d[i]>>l[i];
        cin>>d[N];
        l[N]=0;
        VI a = VI(N+1,-1);
        a[0] = d[0];
        for (int i =0; i <N;i++) {
            for (int j=i+1;j<N+1&&a[i]+d[i]>=d[j];j++) {
                int na = min(l[j], d[j]-d[i]);
                if (na>a[j]) a[j]=na;
            }
        }
        if (a[N]==0) cout<<"YES"; else cout<<"NO";
        cout<<endl;
    }
}
