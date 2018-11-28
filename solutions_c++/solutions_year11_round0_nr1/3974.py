#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <ostream>
#include <cmath>
#include <string>
using namespace std;

int main(){
  int ncases,ccases=1;
  bool nbotB;
  size_t pB,pO;
  string* seq;
  char cSeq[200];
  int ttnB,ttnO;
  int posB,posO;
  int totalTime;
  
  scanf(" %d ",&ncases);
  for(ccases=1;ccases<=ncases;ccases++){
    cin.getline(cSeq,200);
    seq=new string(cSeq);
    pB=seq->find('B');
    //    std::cout<<pB;
    pO=seq->find('O');
    //    std::cout<<" "<<pO<<std::endl;

    if(pB!=string::npos){
      posB=atoi(seq->substr(pB+1).c_str());
      ttnB=posB;
      //      std::cout<<ttnB;
    }
    if(pO!=string::npos){
      posO=atoi(seq->substr(pO+1).c_str());
      ttnO=posO;
      //      std::cout<<" "<<ttnO;
    }

    //posB=posO=1;
    nbotB=pB<pO;
    totalTime=0;
    //    std::cout<<"ttnB "<<ttnB<<"ttnO "<<ttnO<<" "<<nbotB<<std::endl;
    //std::cout<<pB<<" "<<pO<<std::endl;
    while(pO!=string::npos || pB!=string::npos){      
      //std::cout<<"YAH\n";
      if(nbotB){
        (ttnO-ttnB)<1?ttnO=1:ttnO-=ttnB;
        totalTime+=ttnB;
        //std::cout<<"B "<<ttnB<<std::endl;
        pB=seq->find('B',pB+1);
        if(pB!=string::npos){
          ttnB=abs(atoi(seq->substr(pB+1).c_str())-posB)+1;
          posB=atoi(seq->substr(pB+1).c_str());
        }else{
          ttnB=0;
        }
      }else{
        (ttnB-ttnO)<1?ttnB=1:ttnB-=ttnO;
        totalTime+=ttnO;
        //std::cout<<"O "<<ttnO<<std::endl;
        pO=seq->find('O',pO+1);
        if(pO!=string::npos){
          ttnO=abs(atoi(seq->substr(pO+1).c_str())-posO)+1;
          posO=atoi(seq->substr(pO+1).c_str());
        }else{
          ttnO=0;
        }
      }
      nbotB=pB<pO;  
      //      std::cout<<totalTime<<std::endl;
    }    
    //totalTime+=(ttnB+ttnO);
    std::cout<<"Case #"<<ccases<<": "<<totalTime<<std::endl;//" | "<<*seq<<std::endl;
  }
}
