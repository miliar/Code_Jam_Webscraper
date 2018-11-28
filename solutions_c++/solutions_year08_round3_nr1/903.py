#include <string>
#include <vector>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <ctime>
using namespace std;

    struct Cmp {bool operator()(int a, int b){return a>b;}};



main () {
     int N,P,K,L,i,j,e,i1,j1,r,m;
     cin>>N;
     for (i=0;i<N;i++) {
	     vector <int> C;
         cin >>P>>K>>L;
         for (j=0;j<L;j++) {cin >>e;C.push_back(e);}
         sort(C.begin(), C.end(), Cmp());
         //for (j=0;j<L;j++)cout <<C[j];cout <<endl;getchar();
         m=-1;r=0;
         for (j1=0;j1<P;j1++) for (i1=0;i1<K;i1++){
             if (m+1>C.size()-1)break;
             m++;
             r+=C[m]*(j1+1);
         }
         cout <<"Case #"<<i+1<<": "<<r<<endl;
         
         
         
     }
}    
     
