#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <iomanip>
#include <cmath>
#include <vector>
using namespace std;


int main(){
    //ifstream patternfile("ResultData.txt");
    ifstream patternfile("B-small-attempt3.in");
    ofstream myfile("result.txt");
    int T,N,S,P;
    
    patternfile>>T;
    
    for(int i=0;i<T;i++){
            
            patternfile>>N>>S>>P;
            cout<<"Case #"<<i+1<<": "<<N<<" "<<S<<" "<<P<<" ";
            int number;
            int mark1,mark2;
            
            if(S==0){
               mark1 = 3*P-2;
               mark2 = 3*P-4;
            }else{
               if(P==0||P==1){
               mark1 =2;
               mark2 =2;
               }else{
                mark1 = 3*P-2;
               mark2 = 3*P-4;
               }
            }
            
            
            int n1=0,n2=0,n3=0;
            int validcasenumber=0;
            
            
            for(int j=0;j<N;j++){
                patternfile>>number;
                if(number>=mark1){
                  n3++;
                }else if(number<mark1&&number>=mark2){
                  n2++;
                }else{
                  n1++;
                }
                if(number<=28&&number>=2){
                   validcasenumber++;
                }
                
                cout<<number<<" ";
            } 
            cout<<endl;
      int answer=0;
      
      cout<<n1<<" "<<n2<<" "<<n3<<" "<<validcasenumber<<endl;
      
      if(validcasenumber<S){
          cout<<validcasenumber<<endl;
          myfile<<"Case #"<<i+1<<": 0"<<endl;
          continue;
      }
      
      if(S>=n2) answer=n2+n3;
      if(S<n2) answer=S+n3;
      myfile<<"Case #"<<i+1<<": "<<answer<<endl;
    
    }
    
    patternfile.close();
    myfile.close();
system("pause");

}




