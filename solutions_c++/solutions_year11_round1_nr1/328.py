/*
    ID:
    PROG:
    LANG:C++
*/
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
using namespace std;
long long gcd(long long x,long long y){
    if(x<y){
        long long t=x;x=y;y=t;
    }
    if(y==0)return x;
    return gcd(y,x%y);
}
int T;
long long n,x,y;
long long u,v,w,d,g;
int main(){
    freopen("A-large.in","r",stdin);
    freopen("anslarge.out","w",stdout);
    cin>>T;
    for(int cs=1;cs<=T;++cs){
        cin>>n>>x>>y;
        cout<<"Case #"<<cs<<": ";
        u=100/gcd(x,100);
        d=u;
        if(d>n || (y==100 && x!=100) || (y==0 && x>0))cout<<"Broken";
            else cout<<"Possible";
        cout<<endl;
    }
    fclose(stdout);
    return 0;
}
