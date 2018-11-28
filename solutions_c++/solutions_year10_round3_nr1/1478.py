#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>

using namespace std;

#define PI 3.14159265358979323846264338327950288
#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)
     struct dif {
            int a;
            int b;
     };

void main2(int i){

          
     int N;
     int k;;
     vector <dif> piso;
     int sum=0;
     cin>>N;
     REP(k,N){
              dif entrada;
              cin>>entrada.a;
              cin>>entrada.b;
              int j;
              REP(j,k){
                       if((piso[j].b-piso[j].a)>0) {if ((entrada.a>piso[j].a) and (entrada.b<piso[j].b)) sum++;}
                       else {if ((entrada.a<piso[j].a) and (entrada.b>piso[j].b)) sum++;}
              }
              piso.push_back(entrada);   
     }  
     
     
     
     
     cout<<"Case #"<<i+1<<": "<< sum  <<endl;
     
}

main(){
	int number_of_test_cases,i;
	cin>>number_of_test_cases;
	REP(i,number_of_test_cases) main2(i);
}
