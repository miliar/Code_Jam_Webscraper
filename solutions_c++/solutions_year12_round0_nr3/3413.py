#include <iostream>
#include <functional>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <map>
using namespace std;
int lnt(int x){
    if(x==0) return 0;
    return 1+lnt(x/10);
}
int rv(int x,int totl,int pi){
    int cur=x;
    int cur2=0;
    for(int i=0;i<(totl-pi);i++){
        cur2+= (cur%10)* pow(10,i);
        cur/=10;
    }
    //cout<<cur2;
    cur2*=pow(10,pi);
    return (cur2+cur);
}

int main(){
    freopen("c.in","r",stdin);
    freopen("c.out","w",stdout);

    int tc,n,m;
    cin>>tc;
    for(int run=1;run<=tc;run++){
        map< pair<int,int>,bool> mym;

        int ret=0;
        cin>>n>>m;
        for(int i=n;i<=m;i++){
            int l1,l2;
            l1= lnt(i);

            for(int j=1;j<l1;j++){
                int d= rv(i,l1,j);
                if(d<n || d>m) continue;
                l2= lnt(d);
                if(l1!=l2 || d==i ) continue;
                if(!mym[ make_pair(i,d)]){
                    mym[ make_pair(i,d) ]=1;
                    mym[ make_pair(d,i) ]=1;
                    ret++;
                }

            }


        }

        cout<<"Case #"<<run<<": "<<ret<<endl;
    }

    //cout<< rv(143,3,1)<<endl;

    return 0;
}
