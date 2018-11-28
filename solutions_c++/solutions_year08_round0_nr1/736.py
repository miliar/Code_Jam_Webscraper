#include<iostream>
#include<fstream>
#include<stdlib.h>
#include<string>
#include<vector>
#include<math.h>

using namespace std;

int max(vector<int> v){
  int s=v[0];
  for(int i=0;i<v.size();i++){
    if(v[i]>s) s=v[i];
  }
  return s;
}

bool exist(vector<int> v){
  for(int i=0; i<v.size();i++) if(v[i]==0) return 1;
  return 0;
}

int trovamax(vector<string> query, vector<string> motori){
  vector<int> numerolont(motori.size());
  for(int i=0;i<motori.size();i++){
    for(int j=0;j<query.size();j++){
      if(query[j].compare(motori[i])==0){
        numerolont[i]=j+1;
        break;
        }
    }
  }
  for(int i=0;i<numerolont.size();i++) cout<<numerolont[i]<<" ";
  cout<<endl;
  if(exist(numerolont)) return 0;
  int s=max(numerolont);
  return s;
}

void megataglione(vector<string> & query, vector<string> motori){
  int i=trovamax(query, motori);
  query.erase(query.begin(),query.begin()+i-1);
}

 int nostrafun(vector<string> & query, vector<string> motori){
   if(query.size()==0) return 0;
   if(trovamax(query,motori)==0) return 0;
   megataglione(query,motori);
   return (nostrafun(query,motori)+1);
 }



main(){

ifstream f("input.txt");
ofstream o("output.txt");
vector<string> motori;
vector<string> query;

int num_casi;

f>>num_casi;
for(int zum=1;zum<=num_casi;zum++){
  
int num_motori=0;
int num_query=0;
f>>num_motori;
cout<<num_motori<<endl;
char* s;
f.getline(s,100);
for(int i=0;i<num_motori;i++){
  f.getline(s,100);
  motori.push_back(s);
}

f>>num_query;
if(num_query==0){ o<<"Case #"<<zum<<": "<<0<<endl; motori.erase(motori.begin(),motori.end()); query.erase(query.begin(),query.end()); continue;}
cout<<num_query<<endl;
f.getline(s,100);
for(int i=0;i<num_query;i++){
  f.getline(s,100);
  query.push_back(s);}

for(int i=0;i<motori.size();i++) cout<<motori[i]<<" ";
  cout<<endl;

for(int i=0;i<query.size();i++) cout<<query[i]<<" ";
  cout<<endl;

int k=nostrafun(query,motori);
cout<<k<<endl;
o<<"Case #"<<zum<<": "<<k<<endl;
motori.erase(motori.begin(),motori.end()); query.erase(query.begin(),query.end());
}
}
