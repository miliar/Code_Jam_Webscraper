#include<stdio.h>
#include<string>
#include<list>
#include<queue>
#include<stdlib.h>
#include<iostream>
#include <fstream>
#include<map>

using namespace std;

int procesar(int i,vector<string> busq, int s, queue<string> query, int q, map<string, int> M){
     
     int arr[s];
     memset(arr, 0, sizeof(arr));
     int cont=0, sw=0;
     while(!query.empty()){
                        
              string temp = query.front(); query.pop();
              int ind = M[temp];
              if(!arr[ind]){
                       cont++;
                       arr[ind]=1;
                       if(cont==s){
                                   sw++;
                                   memset(arr, 0, sizeof(arr));
                                   arr[ind]=1;
                                   cont=1;            
                       } 
              }                               
                           
     }
     
     return sw;
}

int main(){
    FILE *fout;
    ifstream ent("A-large.in");
    fout = fopen("out.txt", "w");
    int n;
    ent >> n;
    for(int i=0; i<n; ++i){
            map<string, int> M;
            int s;
            queue<string> query;
            ent >> s;
            vector<string> l(s);
            char a;
                        for(int j=0; j<s; ++j){
                                string str;
                                ent >> a;
                                getline (ent,str);
                                str = a+str;
                                l[j] = str;
                                M[str]=j;
                        }
            int q;
            ent >> q;
                        for(int j=0; j<q; ++j){
                                string str;
                                ent >> a;
                                getline (ent,str);
                                str = a+str;
                                query.push(str);
                        }
            int k = procesar(i, l ,s, query , q, M);
            fprintf(fout, "Case #%d: %d\n", i+1, k);
                        
            
            
    }
}
