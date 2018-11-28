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
    int tt=0;
    cin>>tt;
    for (int t=0;t<tt;t++) {
        ll n, d, g;
        cin>>n>>d>>g;
        cout<<"Case #"<<t+1<<": ";
        if (g==0) {
           if (d==0)  cout<<"Possible"<<endl;
           else cout<<"Broken"<<endl;
        } else  
        if (g==100) {
           if (d==100)  cout<<"Possible"<<endl;
           else cout<<"Broken"<<endl;            
        } else {
               ll pom = __gcd(d,100LL);
               if (n>=(100/pom)) cout<<"Possible"<<endl; else cout<<"Broken"<<endl;
                     
        }
        
    } 
}
