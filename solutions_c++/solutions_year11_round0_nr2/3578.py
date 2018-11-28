#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <ostream>
#include <cmath>
#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <ostream>
#include <cmath>
#include <string>
#include <map>
#include <vector>
//#include <pair>
//#include <stack>
using namespace std;

int main(){
  int ncases,ccases=1;
  char seq[200];
  map <char,vector<pair<char,char>* >* > combine;//= new map<char,char*>();
  map <char,vector<char>*> anihilate;
  char comb[10];
  int nComb;
  int N;
  
  scanf(" %d ",&ncases);
  for(ccases=1;ccases<=ncases;ccases++){
    combine['Q']=new vector<pair<char,char>* >();
    combine['W']=new vector<pair<char,char>* >();
    combine['E']=new vector<pair<char,char>* >();
    combine['R']=new vector<pair<char,char>* >();
    combine['A']=new vector<pair<char,char>* >();
    combine['S']=new vector<pair<char,char>* >();
    combine['D']=new vector<pair<char,char>* >();
    combine['F']=new vector<pair<char,char>* >();
    anihilate['Q']=new vector<char>();
    anihilate['W']=new vector<char>();
    anihilate['E']=new vector<char>();
    anihilate['R']=new vector<char>();
    anihilate['A']=new vector<char>();
    anihilate['S']=new vector<char>();
    anihilate['D']=new vector<char>();
    anihilate['F']=new vector<char>();
    scanf(" %d ",&nComb);
    for(int i=0; i<nComb; i++){
      scanf(" %s ",comb);
      pair<char,char>* p = new pair<char,char>(comb[1],comb[2]);
      combine.find(comb[0])->second->push_back(p);
      if(comb[0]!=comb[1]){
        p = new pair<char,char>(comb[0],comb[2]);
        combine.find(comb[1])->second->push_back(p);
      }
    }

    // std::cout<<"MUAHUAHUA\n";
    // if(combine['Q']->size()!=0) std::cout<<"Q: "<<combine['Q']->at(0)->first<<std::endl;
    // if(combine['W']->size()!=0) std::cout<<"W: "<<combine['W']->at(0)->first<<std::endl;
    // if(combine['E']->size()!=0) std::cout<<"E: "<<combine['E']->at(0)->first<<std::endl;
    // if(combine['R']->size()!=0) std::cout<<"R: "<<combine['R']->at(0)->first<<std::endl;
    // if(combine['A']->size()!=0) std::cout<<"A: "<<combine['A']->at(0)->first<<std::endl;
    // if(combine['S']->size()!=0) std::cout<<"S: "<<combine['S']->at(0)->first<<std::endl;
    // if(combine['D']->size()!=0) std::cout<<"D: "<<combine['D']->at(0)->first<<std::endl;
    // if(combine['F']->size()!=0) std::cout<<"F: "<<combine['F']->at(0)->first<<std::endl;

    scanf(" %d ",&nComb);
    for(int i=0; i<nComb; i++){
      scanf(" %s ",comb);
      //      std::cout<<comb<<std::endl;
      anihilate.find(comb[0])->second->push_back(comb[1]);
      anihilate.find(comb[1])->second->push_back(comb[0]);
      
    }


    // if(anihilate['Q']->size()!=0) std::cout<<"Q: "<<anihilate['Q']->at(0)<<std::endl;
    // if(anihilate['W']->size()!=0) std::cout<<"W: "<<anihilate['W']->at(0)<<std::endl;
    // if(anihilate['E']->size()!=0) std::cout<<"E: "<<anihilate['E']->at(0)<<std::endl;
    // if(anihilate['R']->size()!=0) std::cout<<"R: "<<anihilate['R']->at(0)<<std::endl;
    // if(anihilate['A']->size()!=0) std::cout<<"A: "<<anihilate['A']->at(0)<<std::endl;
    // if(anihilate['S']->size()!=0) std::cout<<"S: "<<anihilate['S']->at(0)<<std::endl;
    // if(anihilate['D']->size()!=0) std::cout<<"D: "<<anihilate['D']->at(0)<<std::endl;
    // if(anihilate['F']->size()!=0) std::cout<<"F: "<<anihilate['F']->at(0)<<std::endl;

    scanf(" %d ",&N);
    scanf(" %s ",seq);
    vector<char>* ans = new vector<char>();
    ans->push_back(seq[0]);
    
    for(int i=1;i<N;i++){
      //std::cout<<i<<std::endl;
      vector<pair<char,char>*>* v = combine.find(seq[i])->second;
      vector<pair<char,char>*>::iterator it;
      if(ans->size()==0){
        ans->push_back(seq[i]);
        continue;
      }
      char c=ans->back();
      bool flag=false;
      //std::cout<<c<<std::endl;
      for(it=v->begin(); it!=v->end(); it++){
        //std::cout<<"\t"<<(*it)->first<<std::endl;
        if((*it)->first==c){
          //std::cout<<"Par: "<<c<<" "<<seq[i]<<std::endl;
          ans->pop_back();
          ans->push_back((*it)->second);
          flag=true;
        }
      }
      if(!flag){
        for(int j=0; j<ans->size();j++){          
          vector<char>* vc = anihilate.find(seq[i])->second;
          vector<char>::iterator vcIt;
          for(vcIt=vc->begin(); vcIt!=vc->end();vcIt++){
            if((*vcIt)==(ans->at(j))){
              ans->clear();
              flag=true;
              break;
            }
          }
          if(flag) break;
        }          
      }

      if(!flag){
        ans->push_back(seq[i]);
      }
    }
    //    std::cout<<"Ans: ";
    //std::cout<<std::endl;
    std::cout<<"Case #"<<ccases<<": [";
    if(ans->size()>0){
      int it;
      for(it=0; it<ans->size()-1;it++){
        std::cout<<ans->at(it)<<", ";
      }
      if(ans->size()>it){
        std::cout<<ans->at(it);
      }
    }
    std::cout<<"]\n";

  }
}
