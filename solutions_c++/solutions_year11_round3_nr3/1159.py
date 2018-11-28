#include<map>
#include<set>
#include<vector>
#include<cstdio>
#include<iostream>
#include<algorithm>

#define MAX 101

using namespace std;

int main(){
    bool ok;
    set<int> Num;
    int N,L,H,T,V,div;
    set<int>::iterator it;

    cin>>T;
    for(int t = 1; t <= T; t++){
        ok = true;
        Num.clear();
        cin>>N>>L>>H;
        cout<<"Case #"<<t<<": ";

        for(int i = 0; i < N; i++){
            cin>>V;
            if(V != 1)
                Num.insert(V);
        }
        for(int i = L; i <= H; i++){
            ok = true;
            for(it = Num.begin(); it != Num.end(); ){
                if( (*it)%i != 0 && i%(*it) != 0){
                    ok = false;
                    break;
                }
                it++;
                if(it == Num.end()){
                    cout<<i<<endl;
                    goto VAZA;
                }
            }
        }
VAZA:
        if(ok == false) cout<<"NO"<<endl;
    }

    return 0;
}
