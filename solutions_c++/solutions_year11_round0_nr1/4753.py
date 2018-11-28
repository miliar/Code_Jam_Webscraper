/* /* 
 * File:   main_gcj.cpp
 * Author: vijay
 *
 * Created on 7 May, 2011, 5:50 PM
 */
#include<sstream>
#include <cstdlib>
#include<cstdio>
#include<iostream>
#include<math.h>
using namespace std;
int timer=0;
int blue=1,orange=1;
int mintime();
/*
 * 
 */
int main() {
freopen("test.in", "r", stdin); 
freopen("file.out", "w", stdout); 

int notest,ii=1;
cin>>notest;
while(notest>0){
    cout<<"Case #"<<ii<<": "<<mintime();
    cout<<endl;
    notest--;
    ii++;
}

return 0;
}




int mintime(){
    timer=0;blue=1;orange=1;
    int nobutton,tb,nxto,nxtb;
    cin>>nobutton;
    tb=nobutton;
    int seq[nobutton];
    char seqb[nobutton];
    for(int i=0;i<nobutton;i++){
        cin>>seqb[i];
        cin>>seq[i];
    }
    while(nobutton){
        int fo=0,fb=0;
        for(int i=tb-nobutton;i<tb;i++){
            if(fo==0 && seqb[i]=='O'){
                nxto=seq[i];
                fo=1;
            }
            
            if(fb==0 && seqb[i]=='B'){
                nxtb=seq[i];
                fb=1;
            }
        }
        if(seqb[tb-nobutton]=='O'){
            int interval=fabs(seq[tb-nobutton]-orange) +1;
            timer+=(interval);
            orange=seq[tb-nobutton];
            if(fabs(nxtb-blue)>interval){
                if(nxtb>blue) blue+=interval;
                else blue-=interval;
            }
            else{
                blue=nxtb;
            }
        }
        else{
            int interval=fabs(seq[tb-nobutton]-blue)+1;
            timer+=interval;
            blue=seq[tb-nobutton];
            if(fabs(nxto-orange)>interval){
                if(nxto>orange) orange+=interval;
                else orange-=interval;
            }
            else{
                orange=nxto;
            }
        }
        nobutton--;
    }
    return timer;
    
}


