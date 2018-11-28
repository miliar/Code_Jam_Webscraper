#include<iostream>
#include<sstream>
#include<string>
#include<vector>
using namespace std;

int foo(string t){
  istringstream iss(t);
  
  int res=0;
  int p=0;
  int S=0;
  int N;
  vector<int> g;
  iss >> N >> S >> p;
  int k;while(iss>>k)g.push_back(k);
  
  for(int i=0;i<g.size();i++){
    if(g[i]%3==0 && g[i]/3>=p)res++;// not surprise;
    else if(g[i]%3 != 0 && g[i]/3+1>=p)res++;//not surprise;
    else if(S>0 && g[i]>1 && g[i]<29){
      if(g[i]%3==0 && g[i]/3+1>=p){res++;S--;}//surprise;
      else if(g[i]%3==2 && g[i]/3+2>=p){res++;S--;}//surprise;
    }
  }
  
  return res;
}

int main(){
  int t=0;
  string s;
  getline(cin,s);// s <- T
  while(getline(cin,s)){//s<-input;
    t++;
    int r=foo(s);
    
    string g="Case #";
    if(t==100)g+="100";
    else if(t<10)g+=(char)(t+'0');
    else{g+=(char)(t/10+'0');g+=(char)(t%10+'0');}
    g+=": ";
    
      cout<<g<<r<<endl;
  }
  return 0;
}
