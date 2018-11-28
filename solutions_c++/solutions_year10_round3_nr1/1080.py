/* 
 * File:   main.cpp
 * Author: pavan
 *
 * Created on May 23, 2010, 2:48 PM
 */

#include <stdlib.h>
#include<iostream>


/*
 * 
 */

using namespace std;


class Rope{
    int a[1000],b[1000];
    int n;

public:
    void init();
    int cal();

};

void Rope::init(){

    cin>>n;

    for(int i=0;i<n;i++){
        cin>>a[i]>>b[i];
    }
}

int Rope::cal(){

    int count=0;
    for(int i=0;i<n-1;i++){
        for(int j=i+1;j<n;j++){
            if((a[i]>a[j] && b[i]>b[j]) || (a[i]<a[j] && b[i]<b[j]))
                ;
            else
                count++;
        }
    }
    return(count);
}



int main(int argc, char** argv) {


    int t;
    Rope r;
    cin>>t;

    for(int i=0;i<t;i++){
        r.init();
        cout<<"Case #"<<i+1<<": "<<r.cal()<<endl;
    }

    return (EXIT_SUCCESS);
}

