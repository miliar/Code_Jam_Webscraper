#include<iostream>
#include<vector>
#include<map>
#include<string>
#include<sstream>
#include<cmath>
#include<algorithm>
#include<queue>
#include<deque>
#include<set>
using namespace std;

//double PI =  3.14159265358979323846;
#define ll long long
#define VI vector<ll >
#define PI pair<int,int>
#define MP make_pair
#define PB push_back
#define VVI vector<VI >

int main() {
    int cas;
    cin>>cas;
    for (int t=0;t<cas;t++) {
        int n;cin>>n;
        VI a=VI(n,0);
        VI b=VI(n,0);
        for (int i=0;i<n;i++) cin>>a[i];
        for (int i=0;i<n;i++) cin>>b[i]; 
        sort(a.begin(),a.end());
        sort(b.begin(),b.end());   
        ll ret=0;
        for (int i=0;i<n;i++) ret+=a[i]*b[n-i-1];
        cout<<"Case #"<<t+1<<": "<<ret<<endl;
    }
}
