//
//  main.cpp
//  codejam-recycle
//
//  Created by Rajat Kumar on 4/13/12.
//  Copyright 2012 __MyCompanyName__. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <cstdlib>
#include <sstream>
using namespace std;


string intToString(int i)
{
    stringstream ss;
    string s;
    ss << i;
    s = ss.str();
    
    return s;
}

int recycle(string a,string b){
    
    
    int low=atoi(a.c_str());
    int high=atoi(b.c_str());
    int ctr =0;
    
    for(int i=low; i<=high;i++){
        
        //int n=atoi(inp.c_str());
        int n=i;
        string inp = intToString(n);
        
        if(n<10)
        {
            //cout<<"none"<<endl;
        }
        
        else if(n<100)
        {
            string inp1="";
            inp1 = inp1+inp[1]+inp[0];
            int n1 = atoi(inp1.c_str());
            // cout<<"n1 is "<<inp1<<endl;
            if ((n1>n)&&(n1<=high)) {
                ctr++;
                cout<<n<<","<<n1<<endl;
            }
            
            
        }
        
        else if(n<1000)
        {
            string inp1="",inp2="";
            inp1 = inp1+inp[2]+inp[0]+inp[1];
            inp2 = inp2+inp[1]+inp[2]+inp[0];
            
            int n1 = atoi(inp1.c_str());
            int n2 = atoi(inp2.c_str());
            if ((n1>n)&&(n1<=high)) {
                ctr++;
                cout<<n<<","<<n1<<endl;
            }
            if ((n2>n)&&(n2<=high)) {
                ctr++;
                cout<<n<<","<<n2<<endl;
            }
            
        }
        
        else if(n<10000)
        {
            string inp1="",inp2="",inp3="";
            inp1 = inp1+inp[3]+inp[0]+inp[1]+inp[2];
            inp2 = inp2+inp[2]+inp[3]+inp[0]+inp[1];
            inp3 = inp3+inp[1]+inp[2]+inp[3]+inp[0];
            
            int n1 = atoi(inp1.c_str());
            int n2 = atoi(inp2.c_str());
            int n3 = atoi(inp3.c_str());
            if ((n1>n)&&(n1<=high)) {
                ctr++;
                cout<<n<<","<<n1<<endl;
            }
            if ((n2>n)&&(n2<=high)) {
                ctr++;
                cout<<n<<","<<n2<<endl;
            }
            if ((n3>n)&&(n3<=high)) {
                ctr++;
                cout<<n<<","<<n3<<endl;
            }
            
        }
        
    }
    cout<<"ctr = "<<ctr<<endl;
    return ctr;
}


int main (int argc, const char * argv[])
{
    int t;
    string n,a,b;
    int casectr=1;
    ifstream infile;
    int lineIn;
    infile.open("/Users/rajat/codejam/C-small-attempt0.in.txt");
    ofstream outfile;
    int lineOut,countmax;
    outfile.open("/Users/rajat/codejam/fileout-recycle-submit.txt");
    if (infile.is_open()){
        cout<<"**************************"<<"\n";
        
        
        int fl;
        /**    char temp[100];
         
         infile.getline(temp, 100);
         fl=strtof(temp,0);
         **/
        infile>>fl;
        
        
        //s fl=10;
        while(fl--)
        {
            infile>>a>>b;
            
            
            int countmax=recycle(a,b);
        
        
        lineOut = countmax;
        cout<<"Case #"<<casectr<<": "<<lineOut<<endl;
        
        outfile<<"Case #"<<casectr<<": "<<lineOut<<"\n";
        casectr++;
        }
    }
    
    return 0;
}

