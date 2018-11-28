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
#define VI vector<int>
#define VS vector<string>
#define PI pair<int,int>
#define MP make_pair
#define PB push_back

int main() {

int T;
cin>>T;

for (int t=0;t<T;t++) {
    int N; cin>>N;
    VI a=VI(N,0);
    int ret=-1;
    for (int i=0;i<N;i++) cin>>a[i];
    for (int j=1;j<(1<<N)-1;j++) {
            int x=0;
            int y=0;
            int sum=0;
            for (int k=0;k<N;k++) if (((1<<k)&j)!=0) { x^=a[k]; sum+=a[k];}else y^=a[k];
            if (x==y&&sum>ret) ret=sum;
    }
    
    cout<<"Case #"<<t+1<<": "; if (ret==-1) cout<<"NO"<<endl;   else cout<<ret<<endl;
} 
    
}
