//
//  P3.cpp
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
#include <math.h>
using namespace std;

int main(){
    int t, a, b, result, array1[10], array2[10];
    cin>>t;
    for(int i=0; i<t; i++){
        result = 0;
        cout<<"Case #"<<i+1<<": ";
        cin>>a>>b;
        if(b<10)
            result = 0;
        else{
            for(int a1=a; a1<b; a1++){
                for(int a2=a1+1; a2<=b; a2++){
                    int a1c = a1;
                    if(a1==a2)
                    cout<<a1<<" "<<a2<<endl;
                    int ap=0;
                    while(a1c>0){
                        array1[ap] = a1c%10;
                        a1c/=10;
                        ap++;
                    }
                    
                    for(int s=0; s<ap; s++){
                        int newa=0;
                        int temp = array1[0];
                        for(int w=0; w<ap-1; w++){
                            array1[w] = array1[w+1];
                            newa += array1[w]*(int)pow(10, w);
                        }
                        array1[ap-1] = temp;
                        newa += temp*(int)pow(10,ap-1);
                        
                        if(newa == a2){
                            result++;
                            break;
                        }
                    }
                }
            }
        }
        cout<<result<<endl;
    }
    return 0;
}