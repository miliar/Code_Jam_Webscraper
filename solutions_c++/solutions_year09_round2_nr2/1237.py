#include <iostream>
#include <cmath> 
#include <memory>
#include <list> 
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <bitset>
#include <string>
#include <cctype>
#include <algorithm> 
#include <sstream>
#include <iomanip>
#include <cstdlib>
#include <cstdio> 


using namespace std;

int compare(const void * a, const void *b){ //used qsort
      int aa=*(int*)a;
      int bb=*(int*)b;
      if(bb<aa) return 1;  //menor a mayor
      else return 0;
}

int main(){
    int t,i,j,tam,pos;
    bool ban;
    unsigned long long int num1,num2,num3;
    int ng1[100],ng2[100];
    string cad,let;
    int vec[50],ant[50];
    cin>>t;
    for(i=1; i<=t; i++){
        cin>>cad;
        //num1=atol(cad.c_str());
        
        tam=cad.size();
        for(j=0; j<tam; j++){
            let=cad[j];
            vec[j]=atoi(let.c_str());
            ant[j]=vec[j];
            ng1[j]=vec[j];
        }
        
        while(1){
            next_permutation(vec,vec+tam);
            for(j=0; j<tam; j++) ng2[j]=vec[j];
            //if(num2>num1 && num3<=num2) num3=num2;
            //if(num2=num1) break;
            //if(num2>=num1) break;
            break;
        }
        cout<<"Case #"<<i<<": ";
        
        ban=false;
        for(j=0; j<tam; j++)
            if(ng2[j]>ng1[j]){ban=true; break;}
            else if(ng2[j]<ng1[j]) {ban=false; break;}
        
        if(ban==false){
            qsort(ant,tam,sizeof(int),compare);
            //cout<<ant[0]<<"0";
            for(j=0; j<tam; j++) if(ant[j]!=0) {cout<<ant[j];pos=j;break;}
            cout<<"0";
            for(j=0; j<tam; j++) if(j!=pos) cout<<ant[j];
            
        }else{
            for(j=0; j<tam; j++) cout<<vec[j];
        }
        cout<<endl;
    }
   return 0;
}
