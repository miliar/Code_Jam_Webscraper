#include <set>
#include <iostream>
using namespace std;

#define _for(i,x,n) for(int i=x;i<n;i++)

int main(){
    int T;
    cin>>T;
    _for(tt,1,T+1){
        int n,m;
        cin>>n>>m;
        set< pair<int,int> > res;
        _for(i,n,m+1){
            int base=1,x=i;
            while(x>0)
                base*=10, x/=10;
            //_dv(base)_dv(i)
            for(int j=10;j<base;j*=10){
                x=i%j;
                if(x < j/10) continue;
                int y=x*(base/j) + i/j;
                //_dv(j)_dv(y)
                if(n<=y && y<=m && y>i) res.insert(make_pair(i,y));
            }
        }
        cout<<"Case #"<<tt<<": "<<res.size()<<endl;
    }
    return 0;
}
