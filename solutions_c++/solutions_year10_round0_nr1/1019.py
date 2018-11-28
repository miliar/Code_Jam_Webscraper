/* -*- c++ -*-
   ID: dirtysalt
   PROG: ???
   LANG: C++
   copy[write] by dirlt(dirtysalt1987@gmail.com) */
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <ctime>
#include <cassert>
#include <cstring>

#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <list>
#include <deque>
#include <set>
#include <map>
#include <algorithm>
using namespace std;
typedef long long LL;
int main()
{
    int casn;
    cin>>casn;
    for(int cas=1;cas<=casn;cas++){
        cout<<"Case #"<<cas<<": ";
        int N,K;
        cin>>N>>K;
        int mod=(1<<N);
        LL res=(K+1)%mod;
        if(res==0){
            cout<<"ON"<<endl;
        }else{
            cout<<"OFF"<<endl;
        }
    }
    return 0;
}
