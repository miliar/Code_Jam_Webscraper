#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>

#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T;cin>>T;
    for(int tc=1;tc<=T;tc++) {
        int N,K;cin>>N>>K;
        K++;
        cout<<"Case #"<<tc<<": ";
        if(K%(1<<N)==0)cout<<"ON"<<endl;
        else cout<<"OFF"<<endl;


    }
    return 0;
}
