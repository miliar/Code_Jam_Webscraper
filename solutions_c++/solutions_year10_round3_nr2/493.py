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

int m[1001][1001][11]={0};

int solve(int l, int p, int c) {
//    cout<<"$"<<l<<" "<<p<<endl;
    if (l*c>=p) return 0;
    if (m[l][p][c]!=0) return m[l][p][c];
    int ret = 99999;
    for (int i=l+1;i<p;i++) {
        int val1=1+solve(i,p,c);
        int val2=1+solve(l,i,c);
        int val = val1>val2?val1:val2;    
        if (val<ret) ret=val;
    }    
    m[l][p][c]=ret;
    return ret;
}

int main() {
    int N, M, T;
    cin>>T;
    for (int t=0;t<T;t++) {
             //m=vector<VI>(1001,VI(1001,-1));
             int l,p,c;
             cin>>l>>p>>c;
             int ret = solve(l,p,c);             

            cout<<"Case #"<<t+1<<": "<<ret<<endl;
        
        
    } 
 
    
}
