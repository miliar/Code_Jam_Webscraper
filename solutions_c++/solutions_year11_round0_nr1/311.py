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

int a[200][2],n,t,x,y,ans,p,q,px,py;
char tt;
inline int next(int name,int po){
    for(;po<n;++po)
        if(a[po][1]==name)break;
    return po;
}
int main(){
    //freopen("A-large.in","r",stdin);
    //freopen("A-large.out","w",stdout);
    cin>>t;
    for(int cs=1;cs<=t;++cs){
        cin>>n;
        for(int i=0;i<n;++i){
            cin>>tt>>a[i][0];
            a[i][1]=tt;
        }
        ans=0;
        x=y=0;px=py=1;
        while(1){
            p=next('O',x);
            q=next('B',y);
            if(p==n && q==n)break;
            if(a[p][0]==px)
                if(p<q)x=p+1;else;
                else px+=(px<a[p][0]?1:-1);
            if(a[q][0]==py)
                if(q<p)y=q+1;else;
                else py+=(py<a[q][0]?1:-1);
            ++ans;
        }
        cout<<"Case #"<<cs<<": "<<ans<<endl;
    }
    //fclose(stdout);
    return 0;
}
