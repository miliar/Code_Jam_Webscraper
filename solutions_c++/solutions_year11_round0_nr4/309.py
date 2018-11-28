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

int n,t,x;
int main(){
    //freopen("d-large.in","r",stdin);
    //freopen("d-large.out","w",stdout);
    cin>>t;
    for(int cs=1;cs<=t;++cs){
        cin>>n;
        int ans=n;
        for(int i=1;i<=n;++i){
            cin>>x;
            if(x==i)--ans;
        }
        cout<<"Case #"<<cs<<": "<<ans<<endl;
    }
    //fclose(stdout);
    return 0;
}
