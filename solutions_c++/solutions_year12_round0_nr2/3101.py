//
//  P2.cpp
//  
//
//  Created by Jun Ma on 4/14/12.
//  Copyright (c) 2012 Michigan Technological University. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <strstream>
#include <string>
#include <cstring>
using namespace std;

int main(){
    int t, n, s, p, temp, count, result;
    cin>>t;
    for(int i=0; i<t; i++){
        count = 0;
        result = 0;
        cout<<"Case #"<<i+1<<": ";
        cin>>n>>s>>p;
        for(int j=0; j<n; j++){
            cin>>temp;
            if(p>1){
                if(p*3-2<=temp)
                    result++;
                else if(p*3-4 <=temp && count<s){
                    result++;
                    count++;
                }
            }
            else{
                if(p==0){
                    result = n;
                }
                else 
                    if(temp>=1)
                        result++;
            }
        }
        cout<<result<<endl;
    }
    return 0;
}