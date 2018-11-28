#include <iostream>
#include <vector>
#include <string>
#include <map>

using namespace std;

int tominutes(string s) {
    int ret=0;
    ret+=(s[0]-'0')*10*60;
    ret+=(s[1]-'0')*60;
    ret+=(s[3]-'0')*10;
    ret+=(s[4]-'0');
    return ret;    
}

int main() {
    int n;
    cin>>n;
    for (int i=1; i<=n; i++) {
       int t,na,nb;
       cin>>t>>na>>nb;
       
       map<int,int> trainsABdep; //time and number
       map<int,int> trainsABarr;
       map<int,int> trainsBAdep;
       map<int,int> trainsBAarr;
       
       string dep, arr;
       
       for (int j=0; j<na; j++) {
           cin>>dep>>arr;
           trainsABdep[tominutes(dep)]++;
           trainsABarr[tominutes(arr)+t]++;
       }
       
       for (int j=0; j<nb; j++) {
           cin>>dep>>arr;
           trainsBAdep[tominutes(dep)]++;
           trainsBAarr[tominutes(arr)+t]++;
       }
       
       int countA, countB;
       countA=countB=0;
       
       int minA,minB;
       minA=0;
       minB=0;
       
       int howMany;
       for (int j=0; j<2000; j++) {
           if ((howMany=trainsABarr[j])>0) {
              countB+=howMany;
              //cout << j << ": " << howMany << " arrival from A to B. Count B=" << countB << endl;
           }
           if ((howMany=trainsBAarr[j])>0) {
              countA+=howMany;
              //cout << j << ": " << howMany << " arrival from B to A. Count A=" << countA << endl;
           }
           if ((howMany=trainsABdep[j])>0) {
              countA-=howMany;
              if (countA<minA) minA=countA;
              
              //cout << j << ": " << howMany << " departure from A to B. Count A=" << countA << endl;
           }
           if ((howMany=trainsBAdep[j])>0) {
              countB-=howMany;
              if (countB<minB) minB=countB;
              //cout << j << ": " << howMany << " departure from B to A. Count B=" << countB << endl;
           }


       }
       
       
       /*if (na==0 or nb==0) {
          cout << "Case #" << i << ": " << na << " " << nb << endl; 
          continue;      
       }*/
       
       
       cout << "Case #" << i << ": " << abs(minA) << " " << abs(minB) << endl; 
    }
    
}
