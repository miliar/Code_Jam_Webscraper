#include<iostream>
#include<algorithm>
#include<fstream>
#include<vector>
#include<stack>
#include<queue>
#include<cmath>
#include<set>
#include<string>
#include<stdio.h>
#include<stdlib.h>
#include<sstream>

using namespace std;

struct e{
    char robot;
    int button;
    
    e(char ro, int bu){
        robot = ro;
        button = bu;
    }
};

int test,n,resa,resb;

vector<e> a;

void solve(){
    int oPos,bPos,cP,cB;
    oPos = 1;
    bPos = 1;
    resa = 0;
    resb = 0;
    for(int i = 0;i<n;i++){
        if (a[i].robot == 'O'){
            if (abs(oPos - a[i].button) + resa<= resb) resa = resb + 1;
            else{
                resa += abs(oPos - a[i].button) + 1;
            }
            oPos = a[i].button;
        } else{
            if (abs(bPos - a[i].button) + resb<= resa) resb = resa + 1;
            else{
                resb += abs(bPos - a[i].button) + 1;
            }
            bPos = a[i].button;
        }
    }
}

int main(){
    cin>>test;
    char ro;
    int bu;
    for(int i = 1;i<=test;i++){
        a.clear();
        cin>>n;
        for(int j = 0;j<n;j++){
            cin>>ro>>bu;
            a.push_back(e(ro,bu));
        }
        solve();
        cout<<"Case #"<<i<<": "<<max(resa,resb)<<endl;
    }               
}
