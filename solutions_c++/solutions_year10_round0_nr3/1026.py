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
#include <queue>
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
        int R,K,N;
        queue<int>Q;
        cin>>R>>K>>N;
        LL sum=0;
        for(int i=0;i<N;i++){
            int x;
            cin>>x;
            sum+=(LL)x;
            Q.push(x);
        }
        //simple situaton..
        if(sum<=(LL)K){
            LL res=(LL)R*sum;
            cout<<res<<endl;
            continue;
        }
        
        //complex..
        vector<LL>earn;
        earn.push_back(0);
        int idx=0;
        LL coin=0;
        map< queue<int> ,int > mp;
        map< queue<int> ,int>::iterator it;
        while(1){
            it=mp.find(Q);
            if(it!=mp.end()){
                break;
            }
            idx++;
            mp[Q]=idx;
            int k=K;
            while(k>=Q.front()){
                int x=Q.front();
                k-=x;
                coin+=(LL)x;
                Q.pop();
                Q.push(x);
            }
            earn.push_back(coin);
        }        
        int s=it->second-1;
        int loop=(idx-s);
        LL res=0;
        if(R<=s){
            res=earn[s];
        }else{
            res=earn[s];
            R-=s;
            coin-=earn[s];
            res+=(R/loop)*coin+earn[R%loop+s]-earn[s];
        }
        cout<<res<<endl;
    }
    return 0;
}
