//
//  1И.cpp
//  GoogleCodeJam
//
//  Created by Bakhodir Ashirmatov on 4/14/12.
//  Copyright (c) 2012 __MyCompanyName__. All rights reserved.
//

#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main(){
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    
    int t;
    cin>>t;
    string s;
    getline(cin, s);
    for (int i=0; i<t; i++){
        int n;
        cin>>n;
        int s;
        cin>>s;
        int p;
        cin>>p;
        vector<int> v;
        for (int i=0; i<n; i++){
            int temp;
            cin>>temp;
            v.push_back(temp);
        }
        sort(v.begin(), v.end());
        reverse(v.begin(), v.end());
        int cnt=0;
        for (int i=0; i<n; i++){
            if (v[i]/3>=p || v[i]%3!=0 && v[i]/3==p-1)
                cnt++;
            else if ((v[i]-p)/2==p-2 && s>0){
                s--;
                cnt++;
            }                
        }
        cout<<"Case #"<<i+1<<": "<<cnt<<endl;
    }
}

