#include <cstdlib>
#include <vector>
#include <fstream>
#include <iostream>
#include <string>

using namespace std;
fstream fin,fout;

class CProvod{
    public:
      float a,b;
    };

bool isCol(CProvod &p1,CProvod &p2){
    if (p1.b > p2.b && p1.a > p2.a)
      return 0;
    if (p1.b < p2.b && p1.a < p2.a)
      return 0;
    return 1;
    }

void wrk(int testn){
    vector<CProvod> pr;
    int count;
    fin >> count;
    
    for(int i=0;i<count;++i){
      CProvod p;
      fin >> p.a >> p.b;
      pr.push_back(p);
      }/*
    
    for(int i=0;i<count;++i)
      for(int r=i+1;r<count;++r)
        if(pr[i].b < pr[r].b){
          CProvod p = pr[i];
          pr[i] = pr[r];
          pr[r] = p;
          }*/
    
    int re = 0;
    for(int i=0;i<count;++i)
      for(int r=i+1;r<count;++r)
        if(isCol(pr[i],pr[r]))
          re++;
    fout << "Case #" << testn <<": " << re << endl;
    }

int main(){
    fin. open("./input.txt", fstream::in);
    fout.open("./output.txt",fstream::out);

    int testC;
    fin >> testC;
    
    for(int i=0;i<testC;++i)
      wrk(i+1);
    
    fin.close();
    fout.close();
    return 0;
    }





