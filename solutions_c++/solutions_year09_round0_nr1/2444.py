#include<iostream>
#include <fstream>
#include<string>
#include<set>
using namespace std;
    ofstream fout ("file.out");
    ifstream fin ("file.in");
    set<string> q;
    string ss,ss1;
    int l,d,n,t=0;
    bool aa(string s){
         bool mark=true;
         int num=0;
         for(int i=0;i<s.length();i++)
           if(s[i]=='('){
             mark=false;
             num++;
           }
           else if(s[i]==')')
             mark=true;
           else if(mark)
                  num++;
         return l==num;
    }
    void pri(int i,int j){
         fout<<"Case #"<<i+1<<": "<<j<<endl;
    }
    void bb(int i,int j){
         if(i==l)
           t++;
          else
               if(ss[j]=='('){
                 int kk=j+1;
                 while(ss[j]!=')')
                   j++;
                 for(int u=kk;u<j;u++){
                    ss1+=ss[u];
                    if(q.count(ss1)==1)
                      bb(i+1,j+1);
                    ss1=ss1.substr(0,ss1.length()-1);
                 }
               }
               else{ 
                     ss1+=ss[j];
                     if(q.count(ss1)==1)
                      bb(i+1,j+1);
                    ss1.substr(0,ss1.length()-1);
                    }
    }
int main(){
    fin>>l>>d>>n;
    string s;
    char c;
    for(int i=0;i<d;i++){
      s="";
      for(int j=0;j<l;j++){
        fin>>c;
        while(c>'z'||c<'a')
          fin>>c;
        s+=c;
        q.insert(s);
      }
    }
    for(int i=0;i<n;i++){
      getline(fin,ss);
      while(ss=="")
        getline(fin,ss);
      if(!aa(ss))
        pri(i,0);
      else{
           t=0;
           ss1="";
           bb(0,0);
           pri(i,t);
           }
    }
    return 0;
}
