/*
 * File:   main.cpp
 * Author: Administrator
 *
 * Created on April 4, 2010, 2:19 AM
 */

#include <string>


#include <iostream>
#include <sstream>
#include <cstdio>
#include<set>
#include<cmath>
#define PI 3.14159265
using namespace std;

/*
 *
 */
int main()
{

    int a;
    cin>>a;
    int k,l;
    for(int i=0;i<a;i++)
    {


        cin>>k>>l;
        if((l%(1<<k))==((1<<k)-1))
            cout<<"Case #"<<i+1<<": "<<"ON"<<endl;
        else
            cout<<"Case #"<<i+1<<": "<<"OFF"<<endl;
    }
}

