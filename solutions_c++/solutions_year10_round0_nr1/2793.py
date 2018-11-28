/* 
 * File:   main.cpp
 * Author: pavan
 *
 * Created on May 8, 2010, 7:13 AM
 */

#include <stdlib.h>
#include<iostream>
#include<math.h>

/*
 * 
 */

using namespace std;

class Snap{
    int n;
    long k;
    int snapper[30];

public:

    void init();
    void calculateState();
    int isOn();

};

void Snap::init(){
    cin>>n;
    cin>>k;

    for(int i=0;i<n;i++){
        snapper[i]=0;
    }
}

void Snap::calculateState(){
    for(int i=0;i<n;i++){
        int x=pow( 2, i);
        int y=pow(2,i+1);
        int z;

        if(k-x<0)
            z= y - (abs(k-x)%y);
        else
            z= (k-x)%y;

        if(  x > z )
            snapper[i]=1;
    }
}

int Snap::isOn(){
    int flag=1;

    for(int i=0;i<n;i++){
        if(snapper[i]==0)
            flag=0;
    }
    return(flag);
}


int main(int argc, char** argv) {

    int t;

    Snap s;

    cin>>t;

    for(int a=0;a<t;a++){
        s.init();
        s.calculateState();
        if(s.isOn()){
            cout<<"Case #"<<a+1<<" : "<<"ON"<<endl;
        }
        else{
            cout<<"Case #"<<a+1<<" : "<<"OFF"<<endl;
        }
    }

    return 0 ;
}

