#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cstdlib>
#include <string>

using namespace std;
fstream fin,fout;

class CList{
    protected:
      static CList * last;
      static bool isNULL;
    public:
      CList * next;
      int val;
      
      CList(){
        next = 0;
        //fout << this << endl;
        last = this;
        }
      
      void clear(){
        delete next;
        next = 0;
        isNULL = 1;
        }
      
      ~CList(){
        clear();
        }
      
      void push_back(int x){
      
        if(isNULL){
          last = this;
          last->val = x;
          }else{
          CList **l = &(last->next);
          (*l) = new CList();
          last->val = x;
          //fout <<last <<" "<< last->next << endl;
          }
        
        isNULL = 0;
        }
      
      void moveBack(CList * begin){
        last->next = begin;
        
        last = this;
        next = 0;
        }
      
      void dbg(){
        CList * l = this;
        fout << "list = {";
        while(l){
          fout << l->val <<" ";
          l = l->next;
          }
        fout << "}" << endl;
        }
    };

CList * CList::last = 0;
bool CList::isNULL = 1;

int tests,r,k,n, sum;
CList list, *top;


void getTest(){
    fin >> r >> k >> n;
    //fout << r <<endl << k<<endl << n << endl;
    for(int i=0;i<n;++i){
      int v;
      fin >> v;
      list.push_back(v);
      }
    }

void turn(){
    CList * l = top;
    int nk = l->val;
    while(l->next && nk+l->next->val <= k){
      nk+=l->next->val;
      l = l->next;
      }
    sum+=nk;
    //fout << "nk = " << nk << endl;
    
    CList *l1 = l->next;
    l->moveBack(top);
    if(l1){
      top = l1;
      //fout << "[1]" << endl;
      }
    }

void wrk(int id){
    getTest();
    //list.dbg();
    top = &list;
    
    sum = 0;
    for(int i=0;i<r;++i){
      turn();
      //top->dbg();
      }
    
    fout << "Case #"<<id<<": " <<sum << endl;
    
    list.clear();
    }

int main(void){
    fin.open ("./input.txt", fstream::in);
    fout.open("./output.txt",fstream::out);
    
    fin >> tests;
    for(int i=0;i<tests;++i){
      wrk(i+1);
      }
    
    fin.close();
    fout.close();
    return 0;
    }













