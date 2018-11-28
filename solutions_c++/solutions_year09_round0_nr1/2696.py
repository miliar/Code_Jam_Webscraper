#include <iostream>
#include <map>
#include <string>
#include <vector>
#include <fstream>
using namespace std;
int main(){
  ifstream cin("A-large.in");
  ofstream cout("Alien_large.txt");
  int L,D,N;
  string word;
  cin>>L>>D>>N;
  map<string,bool> dic;
  for(int i=0;i<D;i++){
    cin>>word;
    dic[word]=true;
  }

  for(int i=1;i<=N;i++){
    cin>>word;
    string p[L];
    int h=0;
    bool cmb=false;
    for(int j=0;j<word.length();j++){
      if(word[j]=='('){
           cmb=true;
           continue;
      }
      if(word[j]==')'){
          cmb=false;
          h++;
          continue;     
      }
      p[h] = p[h]+word[j];
      if(!cmb)h++;
    }
    int cnt=0;
    for(map<string,bool>::iterator it = dic.begin();it!=dic.end();it++){
       int completa = true;
       for(int k=0;k<L;k++){
        if(p[k].find( (it->first)[k]) !=  string::npos )continue;   
        completa = false;
        break;
       }   
       if(completa)
        cnt++;  
    }
    cout<<"Case #"<<i<<": "<<cnt<<endl;
  }
 return 0;   
}
