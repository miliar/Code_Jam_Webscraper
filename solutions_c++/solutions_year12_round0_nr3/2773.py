//
//  1C.cpp
//  GoogleCodeJam
//
//  Created by Bakhodir Ashirmatov on 4/14/12.
//  Copyright (c) 2012 __MyCompanyName__. All rights reserved.
//

#include <iostream>
#include <string>
#include <vector>
#include <set>
using namespace std;

int main(){
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    
    int t;
    cin>>t;
    for (int i=0; i<t; i++){
        int a, b;
        cin>>a>>b;
        int cnt=0;
        for (int j=a; j<=b; j++){
            int len=1, tmp=j, pow=1;
            while (tmp>=10){
                tmp/=10;
                len++;
                pow*=10;
            }
            tmp=j;
            set<int> st;
            for (int k=0; k<len; k++){
                int rem=tmp%10;
                tmp=tmp/10+rem*pow;
                if (tmp>=a && tmp<=b && tmp>j && rem){
                   // cout<<j<<" "<<tmp<<endl;
                    st.insert(tmp);
                }
            }     
            cnt+=st.size();
        }
        cout<<"Case #"<<i+1<<": "<<cnt<<endl;
    }
}

