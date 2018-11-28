#include <vector>
#include <string>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;
char cad1[4],cad2[3],cad3[102];
int conta[28],caso=1;
map<string,char>M;
bool tabla[28][28];
map<string,char>:: iterator it;
string s1,s2,s3;

void doit(){
   //cout<<"entra"<<endl;
   
   int C,D,N;
   M.clear();
   memset(conta,0,sizeof(conta));
   memset(tabla,0,sizeof(tabla));
   scanf("%d",&C);
   for(int i=0;i<C;++i){
      scanf(" %s",cad1);
      s1=string(cad1);
     // cout<<" "<<s1;
      string aux1="";aux1+=s1[0];aux1+=s1[1];
      string aux2="";aux2+=s1[1];aux2+=s1[0];
      M[aux1]=s1[2];
      M[aux2]=s1[2];    
   }
   
   scanf(" %d",&D);
   for(int i=0;i<D;++i){
      scanf(" %s",cad2);
      s2=string(cad2);
      //cout<<" "<<s2;
      tabla[s2[0]-'A'][s2[1]-'A']=1;
      tabla[s2[1]-'A'][s2[0]-'A']=1;   
   }
  // cout<<"llega"<<endl;
   scanf(" %d",&N);
   scanf(" %s",cad3);
   s3=string(cad3);
  // cout<<" "<<s3;
   
   
   //debugeando
   
  // cout<<"cadenas: "<<s1<<" "<<s2<<" "<<s3<<endl;   
   
   
   
   
   deque<char>Q;
   for(int i=0;i<s3.length();++i){
       /* for(int j=0;j<Q.size();++j){
            cout<<" "<<Q[j];
         }*/
      
      if(Q.empty()){
         Q.push_back(s3[i]);
         conta[s3[i]-'A']++;
      }
      else{
         string aux="";aux+=Q[Q.size()-1];aux+=s3[i];
         if(M.find(aux)!=M.end()){
            char entra=M[aux];
            char sale=Q.back();
            conta[sale-'A']--;
            conta[entra-'A']++;
            Q.pop_back();
            Q.push_back(entra);
         }
         else{
            bool enc=0;
            for(int j=0;j<=27;++j){
               if(tabla[s3[i]-'A'][j]==1){
                  if(conta[j]>0){
                     enc=1;Q.clear();
                     memset(conta,0,sizeof(conta));
                     break;
                  }
               }
            }
            
            if(enc==0){
               Q.push_back(s3[i]);
               conta[s3[i]-'A']++;
            } 
         }
      }
      
     
   }
   
   
   //solucion:
   printf("Case #%d: [",caso++);   
   int x=Q.size()-1;
   for(int i=0;i<Q.size();++i){
      if(i==x){
         printf("%c",Q[i]);
      }
      else{
         printf("%c, ",Q[i]);
      }
      
   }
   printf("]\n");
   
}


int main(){
   int t;
   scanf("%d",&t);
   for(int i=0;i<t;++i){
      doit();
   }
}
