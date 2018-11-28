#include<iostream>
#include<algorithm>
#include <iostream>
#include <fstream>

using namespace std;

int main(){
    ifstream input;
    input.open("c.in");
    ofstream output;
    output.open("c.out");
  
    int T;     
    input>>T;
    string ten(" welcome to code jam");
    string s;
    getline(input,s);
    
    for(int i=1; i<=T; i++){
                 getline(input,s);

                 int tab[22];   
                 for(int i=1; i<22; i++)
                         tab[i]=0;
                 tab[0]=1;

                         
                                 
                 for(int j=0; j<s.size(); j++)
                         for(int k=1; k<ten.size(); k++)
                                 if(s[j]==ten[k])
                                                 tab[k]=(tab[k]+tab[k-1])%10000;
                                                       
                 int res=tab[ten.size()-1];
                
                 output<<"Case #"<<i<<": ";
                 
                 if(           res<10)  output<<"000";
                 else if(      res<100) output<<"00";
                 else if(      res<1000)output<<"0";
                 
                 output<<res<<endl;
                 }
  //  system("pause");                                                             
    
    return 0;
}

