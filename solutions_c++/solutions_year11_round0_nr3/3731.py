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
int N;
int maxim;
vector<int>* nums;

void deep (int i, int nSumP,int nSumS, int xSumP, int xSumS);

int main(){
  int ncases,ccases;
  //bool put[1100];
  int nSumP, nSumS;
  int xSumP, xSumS;
  
  scanf(" %d ",&ncases);
  for(ccases=1;ccases<=ncases;ccases++){
    maxim=0;
    nSumP=nSumS=xSumP=xSumS=0;
    scanf(" %d ",&N);
    nums = new vector<int>();
    int numb;
    for(int i=0; i<N; i++){
      scanf(" %d ",&numb);
      nums->push_back(numb);
    }

    deep(0,nSumP,nSumS,xSumP,xSumS);

    cout<<"Case #"<<ccases<<": ";
    if(maxim>0){
      cout<<maxim<<endl;
    }else{
      cout<<"NO\n";
    }

  }
}

void deep (int i, int nSumP,int nSumS, int xSumP, int xSumS){
  int curr = nums->at(i);
  if(i==N-1){
    //cout<<nSumP<<" "<<nSumS<<" "<<xSumP<<" "<<xSumS<<" "<<curr<<endl;
    if( (xSumS^curr)==xSumP ){
      //cout<<"S\n";
      if(nSumS+curr>maxim && nSumS+curr>0 && nSumP>0){
        maxim=nSumS+curr;
      }
    }

    if( (xSumP^curr)==xSumS){
      //cout<<"P\n";
      if(nSumS>maxim && nSumS>0 && nSumP+curr>0){
        maxim=nSumS;
      }
    }

  }else{
    deep(i+1,nSumP+curr,nSumS,xSumP^curr,xSumS);
    deep(i+1,nSumP,nSumS+curr,xSumP,xSumS^curr);
  }
}

// for(int i=0; i<N; i++){
//   std::cout<<nums->at(i)<<" ";
// }
// cout<<endl;
// int n1,n2;
// scanf(" %d %d ",&n1,&n2);
// //std::cout<<n1<<" + "<<n2<<std::endl;
// int ans = n1^n2;
// std::cout<<n1<<" + "<<n2<<" = "<<ans<<std::endl;
    
