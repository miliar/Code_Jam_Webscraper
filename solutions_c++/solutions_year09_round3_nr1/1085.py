#include<iostream>
#include<map>
#include<string>
#include<vector>
#include<fstream>
using namespace std;
main(){
       ifstream fin("in.txt");
       ofstream fout("out.txt");
       int n;
       fin>>n;
       int j;
       for(j=1;j<=n;j++){
                  string s,s1;
                  int i;
                  fin>>s;
                  char count=0;
                  map<char,bool> m1;
                  map<char,char> m;
                  for(i=0;i<s.size();i++){
                                             if(m1[s[i]]==false){
                                                                if(count<10)
                                                                     m[s[i]]=char(count+48);
                                                                else
                                                                     m[s[i]]=char(count+87);
                                                                count++;
                                                                m1[s[i]]=true;
                                             }
                                             
                                             s1+=m[s[i]];
                  }
                  int z=count;
                  
                  for(i=0;i<s1.size();i++){
                                          if(s1[i]==48)
                                                       s1[i]=49;
                                          else if(s1[i]==49)
                                                       s1[i]=48;
                  }
                  int sum=0,mul=1;
                  for(i=s1.size()-1;i>=0;i--){
                                              if(s1[i]<90)
                                           sum+=(s1[i]-48)*mul;
                                           else
                                           sum+=(s1[i]-87)*mul;
                                           mul*=z;
                  }
                  cout<<"Case #"<<j<<": "<<sum<<endl;
       }
       system("pause");
}
