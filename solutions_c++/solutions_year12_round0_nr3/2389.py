/*	SURENDRA KUMAR MEENA	*/
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <queue>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <ctime>
using namespace std;
typedef long long int LL;
#define FF(i,m,n)	for(int i=m;i<n;i++)
#define F(i,n)	FF(i,0,n)
#define R(i,n,k) for(int i=n;i>=k;i--)
#define CLR(s,v) memset(s,v,sizeof(s))
string to_str(LL x){ ostringstream o;o<<x;return o.str();}
LL to_int(string s){ istringstream st(s); LL i;	st>>i;return i;}

int a,b;

int fn(int k){
    string w = to_str(k);
    set<int> st;
    FF(i,1,w.size()){
        if(w[i]=='0')
            continue;
        string d = w.substr(i) + w.substr(0,i);
        int val = to_int(d);
        if(val>k && val<=b)
            st.insert(val);
    }
    return (int)st.size();
}

int main(){
    int t;
    cin>>t;
    FF(kase,1,t+1){
        cout<<"Case #"<<kase<<": ";
        cin>>a>>b;
        int ans = 0;
        while(a<=b){
            ans += fn(a++);
        }
        cout<<ans<<endl;
    }
}
