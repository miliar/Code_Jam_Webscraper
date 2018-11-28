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
int n,m,t,s,small,x;
int main(){
    //freopen("c-large.in","r",stdin);
    //freopen("c-large.out","w",stdout);
    cin>>m;
    for(int cs=1;cs<=m;++cs){
        cin>>n;
        s=t=0;small=10000000;
        for(int i=0;i<n;++i){
            cin>>x;
            t^=x;
            small=min(small,x);
            s+=x;
        }
        cout<<"Case #"<<cs<<": ";
        if(t!=0)cout<<"NO"<<endl;
            else cout<<s-small<<endl;
    }
    //fclose(stdout);
    return 0;
}
