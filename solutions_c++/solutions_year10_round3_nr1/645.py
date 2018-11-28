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

map<string,int> m;

int main() {
    int N, M, T;
    cin>>T;
    for (int t=0;t<T;t++) {
             int n;
             cin>>n;
             VI a = VI(n,0);
             VI b = VI(n,0);
             int ret=0;
             
             for (int i=0;i<n;i++) cin>>a[i]>>b[i];
             for (int i=0;i<n;i++) for (int j=i+1;j<n;j++) {
                 if ((a[i]-a[j])*(b[i]-b[j])<0)    ret++;
             }

            cout<<"Case #"<<t+1<<": "<<ret<<endl;
        
        
    } 
 
    
}
