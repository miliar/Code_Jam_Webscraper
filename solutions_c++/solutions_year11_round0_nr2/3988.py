#include <iostream>
#include <string>
#include <vector>

#define EMPTY ' ';
using namespace std;

typedef struct{
   char A;
   char B;
   char C;
}COMBINED;

typedef struct{
   char A;
   char B;
}OPPOSITE;


char dlist[28*2];
char clist[36*3];

COMBINED getCi(int i){
  COMBINED ret;
  ret.A = clist[i*3];
  ret.B = clist[i*3+1];
  ret.C = clist[i*3+2];
  return ret;
}

OPPOSITE getOi(int i){
  OPPOSITE ret;
  ret.A = dlist[i*2];
  ret.B = dlist[i*2+1];
  return ret;
}


int T=0,C=0,D=0,N=0;

char destList[100];

bool checkCombine(int endIndex){
  bool found = false;
  COMBINED comb;

  for(int c=0;c<C;c++){
     comb = getCi(c);
     if( (destList[endIndex-1] == comb.A && destList[endIndex] == comb.B) ||  
         (destList[endIndex-1] == comb.B && destList[endIndex] == comb.A)){
       //found
       found = true;
       destList[endIndex-1]= EMPTY;
       destList[endIndex]=comb.C;
       break;
    }  
  }  
  return found;  
}

void checkOpposite(int endIndex){
  
  OPPOSITE opp;
    
  for(int d=0;d<D;d++){
    opp = getOi(d);
    
    int aindex = -1;
    int bindex = -1;
    char toSearch;
    int i;

    for(i=0;i<=endIndex;i++){
      if( destList[i] == opp.A || destList[i] == opp.B){
        aindex = i;
        toSearch = destList[i]==opp.A?opp.B:opp.A;    
        break;
      }
    }                

    for(;i<=endIndex;i++){
      if( destList[i] == toSearch){
        bindex = i;
        break;
      }
    }                
/*
    if(aindex != -1 && bindex != -1){        
        for(int j=min(aindex,bindex);j<=max(aindex,bindex);j++){
          destList[j] = EMPTY;
        }
        return;
    }*/
    if(aindex != -1 && bindex != -1){        
        for(int j=0;j<=endIndex;j++){
          destList[j] = EMPTY;
        }
        return;
    }
          
  
  }
  

}
 
int main(int argc,char** argv){

  //vector<int> clist;
  int clindex  = 0;
  string cl;
  //vector<int> dlist;
  int dlindex = 0;  

  string dl;
  cin >> T;
  
  for(int t=0;t<T;t++){
    clindex = dlindex = 0;
    destList[0]=0;
    cin >> C;
    if(C > 0){
      for(int c=0;c<C;c++){
        cin >> cl;
        for(int i = 0;i<3;i++)
          clist[clindex++] = cl[i];
        //clist.push_back(cl);
      }
    }

    cin >> D;
    if(D > 0){
      for(int d=0;d<D;d++){
        cin >> dl;
        for(int i = 0;i<2;i++)
          dlist[dlindex++] = dl[i];
      }
    }

    cin >> N;  	
    cin >> destList;


    /*cout << "test:" << t << endl;
    cout << "C:" << C << endl;
    cout << "D:" << D << endl;
    cout << "N:" << N << endl;
    cout << "destList:" << destList << endl;

    for(int i=0;i<C;i++){
      COMBINED c;
      c = getCi(i);
      cout << "C" << i << ":" << c.A << c.B << c.C << endl;
    }

    for(int i=0;i<D;i++){
      OPPOSITE d;
      d = getOi(i);
      cout << "D" << i << ":" << d.A << d.B << endl;
    }*/

    char resCombine;
    for(int i = 1;i<N;i++){
      
      if(!checkCombine(i)){
        //check opposite
        checkOpposite(i);
      }

    }

    cout << "Case #" << (t+1) << ": [";
    bool  empty = true;
    for(int i = 0;i<N;i++){
     if(destList[i] != ' '){
        
        if(!empty)
          cout << ", ";

        cout << destList[i];
        empty = false;
      }
    }

    cout << "]" << endl;
  }

   
  

  return 0;

}
