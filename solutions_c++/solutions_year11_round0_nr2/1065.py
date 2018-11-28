#include<iostream>
#include<fstream>
#include<string>
#include<map>
#include<set>
#include<list>
using namespace std;
int main(){
    ifstream in("B-large.in");
    ofstream out("B-large.out");
    int T;
    in>>T;
    int cas=1;
    while(T--){
               int C,D,N;
               in>>C;
               char temp1[150],temp2[150],temp[150];
               char t;
               map<string,char> mpc;
               map<string,bool> mpo;
               list<char> el;
               while(C--){
                          in>>temp;
                          temp2[0]=temp1[1]=temp[1];
                          temp2[1]=temp1[0]=temp[0];
                          temp2[2]=temp1[2]='\0';   
                          t=temp[2];
                          mpc[(string)temp1]=mpc[(string)temp2]=t;
               }
               in>>D;
               while(D--){
                          in>>temp;
                          temp2[0]=temp1[1]=temp[1];
                          temp2[1]=temp1[0]=temp[0];
                          temp2[2]=temp1[2]='\0';               
                          mpo[(string)temp2]=mpo[(string)temp1]=1;
               }
               in>>N;
               in>>temp;
               int i=1;
               el.push_back(temp[0]);
               bool flag;
               while(--N){
                      flag = true;
                      if(!mpc.empty()&&!el.empty()){
                           char last = el.back();
                           temp1[0] = last;
                           temp1[1] = temp[i];
                           temp1[2] ='\0';
                           if(mpc.count((string)temp1)>0){
                                                 el.pop_back();
                                                 el.push_back(mpc[(string)temp1]);
                                                 flag = false;
                           }
                      }
                      if(flag&&!mpo.empty()&&!el.empty()){
                               temp1[1] = temp[i];
                               temp1[2] = '\0';
                               for(list<char>::iterator it = el.begin(); it!=el.end();++it){
                                               temp1[0] = (*it);
                                               if(mpo.count((string)temp1)>0){
                                                                      el.clear();
                                                                      flag = false;
                                                                      break;
                                               }
                               }
                      }
                      if(flag) el.push_back(temp[i]);
                      i++;
               }
               cout<<"Case #"<<cas<<": [";
               out<<"Case #"<<cas<<": [";
               size_t elsize = el.size();
               int eliter =1;
               if(elsize>0){
                            for(list<char>::iterator it = el.begin(); it!=el.end();++it){
                                   cout<<(*it); out<<(*it);
                                   if((eliter++)!=elsize){ cout<<", "; out<<", ";}  
                            }                          
               }
               cout<<"]\n";         
               out<<"]\n";         
               cas++;
    }
    system("pause");
    return 0;
}
