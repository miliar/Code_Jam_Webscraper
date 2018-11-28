#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
#include <conio.h>

using namespace std;

#define dv(vectName) for(int ii=0;ii<vectName.size();ii++) cout<<vectName[ii]<<' '; cout<<endl;
#define d1da(arrayName,size) for(int ii=0;ii<size;ii++) cout<<arrayName[ii]<<' '; cout<<endl;
#define d2da(arryName,row,col) for(int ii=0;ii<row;ii++){ for(int jj=0;jj<col;jj++) cout<<arryName[ii][jj]<<' '; cout<<endl; } cout<<endl; 

#define miii map<int,int>::iterator
#define mici map<int,char>::iterator
#define mcii map<char,int>::iterator
#define vii vector<int>::iterator

#define pb(vectName,value) vectName.push_back(value);
#define mi(mapName,keyType,valType,key,val) mapName.insert(pair<keyType,valType>(key,val));



//fstream inp("A-small.in",ios::in);
//fstream inp("a-large.in",ios::in);
fstream inp("A-Large.in",ios::in);
//fstream inp("test.in",ios::in);
fstream out("A-Large.out",ios::out);
vector<string> dic;
int L,D;




void solve(int testCaseNo){
     vector< vector<int> > work(L);
     vector<int> log(26,0);
     for(int i=0;i<L;i++) work[i] = log;     
     string word;
     inp>>word;     
     int index=0;
     bool inside=false;
     for(int i=0;i<word.length();i++){
             char c=word[i];
             if(c>='a' && c<='z'){
                       if(!inside){
                                   /*if(present(c,index)){
                                                        parts[index].push_back(c);
                                                        index++;             
                                   } */
                                   work[index][c-'a']=1;
                                   index++;                     
                       }
                       else{                            
                                                        //if(present(c,index))parts[index].push_back(c);                            
                                                        work[index][c-'a']=1;
                       }
             }
             else{                  
                  if(c=='('){ inside=true;}
                  else {inside=false;index++;}                  
             }
     }        
     int answer=0;
     for(int j=0;j<D;j++){
                      string cand = dic[j];
                      bool ok=true;
                      for(int k=0;k<L;k++)
                              if(work[k][cand[k]-'a']!=1) { ok=false;break; }
                      if(ok) answer++;
     }
     out<<"\nCase #"<<testCaseNo<<": "<<answer;  
                                            
                    
}


int main(void){
    int N;
    inp>>L>>D>>N;    
    for(int i=1;i<=D;i++){
            string word;
            inp>>word;
            pb(dic,word);
    }    
    for(int i=1;i<=N;i++)
            solve(i);
    getch();
    return 0;
}
