#include<cstdio>
#include<iostream>
#include<string>
#include<vector>
using namespace std;
int temp;
int tc,n,query;
string s;
string ar[100];
vector<int> child[100005];
string dire[100005];
int nAr;
int num;


void visit (int node, int now){
     if (now > nAr){
        return;
     } else{
       bool tr = false;
       for (int i = 0; i < child[node].size(); i++){
           if ((dire[child[node][i]]) == ar[now]){
              visit(child[node][i],now+1);                           
              tr = true;
           } 
       }       
       if (!tr){
          num++;          
          child[node].push_back(num);
          dire[num] = ar[now];
          visit(num,now+1);
       }
     }
}
void perin (int node){
  cout<<node<<" "<<dire[node]<<endl;
  for (int i = 0; i < child[node].size(); i++){
      cout<<dire[child[node][i]]<<endl;    
  }
  for (int i = 0; i < child[node].size(); i++){
      perin(child[node][i]);    
  }
}
int main(){
 scanf("%d",&tc);
 for (int ti = 1; ti <= tc; ti++){

    scanf("%d %d\n",&n,&query);
    num = 0;
    for (int i = 1; i <= n; i++){
        getline(cin,s);
        nAr = 0;                
        for (int j = 0; j < s.length(); j++){
            if (s[j] == '/'){
               nAr++; ar[nAr] = "";         
            } else{
              ar[nAr] += s[j];        
            }
        }    
        visit(0,1);    
    }            
    temp = num;
    for (int i = 1; i <= query; i++){
        getline(cin,s);
        nAr = 0;                
        for (int j = 0; j < s.length(); j++){
            if (s[j] == '/'){
               nAr++; ar[nAr] = "";         
            } else{
              ar[nAr] += s[j];        
            }
        }    
        visit(0,1);    
    }            
//    perin(0);    
    for (int i = 0; i <= num; i++) child[i].clear();
    printf("Case #%d: %d\n",ti,num-temp);

 }   
}
