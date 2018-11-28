#include<iostream>
#include<algorithm>
#include <iostream>
#include <fstream>

using namespace std;

int main(){
    int dlugosc, ile_slow, T;
    string tab[5555];
    
    ifstream input;
    input.open("a.in");
    input>>dlugosc>>ile_slow>>T;
    
    ofstream output;
    output.open("a.out");
    
    for(int i=1; i<=ile_slow; i++)
            input>>tab[i];
    
    
    for(int i=1; i<=T; i++){
                 int ile=0;
                 string s;
                 input>>s;
                 bool is[20][29];
                 for(int k=0; k<dlugosc; k++)
                 for(int s=0; s<29; s++)
                 is[k][s]=false;
                 
                 for(int j=0,k=0; j<s.size(); j++,k++){
                         if(s[j]=='(')
                                      for(j++; s[j]!=')'; j++)
                                               is[k][s[j]-'a']=true;
                         else
                             is[k][s[j]-'a']=true;
                         }
                 
                 for(int j=1; j<=ile_slow; j++){
                         int k=0;
                         
                         while(k<dlugosc && is[k][ tab[j][k]-'a' ])
                                         k++;
                         
                         if(k>=dlugosc)
                                       ile++;
                         }
                         
                
                 output<<"Case #"<<i<<": "<<ile<<endl;
                 }
  //  system("pause");                                                             
    
    return 0;
}

