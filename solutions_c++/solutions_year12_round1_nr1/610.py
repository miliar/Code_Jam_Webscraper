//
//  2A.cpp
//  GoogleCodeJam
//
//  Created by Bakhodir Ashirmatov on 4/28/12.
//  Copyright (c) 2012 __MyCompanyName__. All rights reserved.
//

#include <iostream>
using namespace std;

double p[100000], res[100000];

int main(){
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    
    int T;
    cin>>T;
    for (int t=0; t<T; t++){
        int a, b;
        cin>>a>>b;
        for (int i=0; i<a; i++)
            cin>>p[i];
        
        double akk=1;
        for (int i=0; i<a; i++){
            res[i]=akk;
            akk*=p[i];
        }
        res[a]=akk;
        
        double exp=b+2;
        for (int i=0; i<=a; i++){
            double cor=res[a-i];
            double temp=cor*(b-a+i+i+1)+(1-cor)*(b-a+i+i+b+2);
            exp=min(exp, temp);
        }
        
        printf("Case #%d: %0.8e\n", t+1, exp);
    }
}
