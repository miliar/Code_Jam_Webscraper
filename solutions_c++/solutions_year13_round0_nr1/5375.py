#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>
#include <stdio.h>
#include <set>
#include <math.h>
#include <map>
#include <stack>
#include <fstream>
using namespace std;

int main()
{
ifstream fin;
fin.open("input3.txt");
ofstream fout;
fout.open("output.txt");
    int t;
    int cas=0;
    fin>>t;
    
    
    while(t--){cas++;
                int flag=0;                
                set<char>s1;
              
                int flag1=0;                
                set<char>s2;
             vector<string>v;
             string s3;
           int ans=0;
             for(int i=0;i<4;i++)
             {fin>>s3;
             v.push_back(s3);}
             for(int i=0;i<v.size();i++){
                     set<char>s;
                     int flag=0;
                     for(int j=0;j<4;j++){
                             if(v[i][j]!='T' && v[i][j]!='.')
                             s.insert(v[i][j]);
                             if(v[i][j]=='.')
                             {flag=1;goto xy;}
                             }
                     xy:
                             if(flag==1 || s.size()==2){
                                         s.clear();
                                         
                                         }
                                         else{
                                           set<char>::iterator itr;
                                           
                                           for(itr=s.begin();itr!=s.end();itr++){
                                                  fout<<"Case #"<<cas<<": "<<*itr<<" "<<"won"<<endl;
                                                  
                                           
                                                  ans=1;                                                                               
                                                                                 }
                                           
                                              s.clear();
                                          //        goto ttt;
                                              }
                     }  
               
               
               if(ans==1)
               goto ttt;
               
               ans=0;
//               s.clear();
                  for(int i=0;i<v.size();i++){
                     set<char>s;
                     int flag=0;
                 set<char> ::iterator itr1;
                    
                     
                     for(int j=0;j<4;j++){
                             if(v[j][i]!='T' && v[j][i]!='.')
                            { s.insert(v[j][i]);}
                             if(v[j][i]=='.')
                             {flag=1;goto yz;}
                             }
                             
                     yz:
                              set<char>::iterator itr;
                   
                             if(flag==1 || s.size()==2){
                                         s.clear();
                                         
                                         }
                                         else{
                                              
                                          
                                           
                                           for(itr=s.begin();itr!=s.end();itr++){
                                                   fout<<"Case #"<<cas<<": "<<*itr<<" "<<"won"<<endl;
                                                                               
                                                           //goto ttt;
                                                           ans=1;                      }
                                           
                                              s.clear();
                                              }
                     }  
               if(ans==1)
               goto ttt;
               ans=0;
             
               
               
               
                 for(int i=0;i<v.size();i++){
                     //set<char>s;
                    // int flag=0;
                     
                             if(v[i][i]!='T' && v[i][i]!='.')
                             s1.insert(v[i][i]);
                             if(v[i][i]=='.')
                             {flag=1;goto xz;}
                             }
                     xz:
                             if(flag==1 || s1.size()==2){
                                         s1.clear();
                                         
                                         }
                                         else{
                                           set<char>::iterator itr;
                                           for(itr=s1.begin();itr!=s1.end();itr++){
                                                   fout<<"Case #"<<cas<<": "<<*itr<<" "<<"won"<<endl;                                           
                                                                              }
                                           
                                              s1.clear();
                                              ans=1;
                                            //  goto ttt;   
                                              }
                     if(ans==1)
                     goto ttt;
                     ans=0;
               
               
                  for(int i=0;i<v.size();i++){
                     //set<char>s;
                    // int flag=0;
                     
                             if(v[i][3-i]!='T' && v[i][3-i]!='.')
                             s2.insert(v[i][3-i]);
                             if(v[i][3-i]=='.' )
                             {flag=1;goto xzz;}
                             }
                     xzz:
                             if(flag1==1 || s2.size()==2){
                                         s2.clear();
                                         
                                         }
                                         else{
                                           set<char>::iterator itr;
                                           for(itr=s2.begin();itr!=s2.end();itr++){
                                                  fout<<"Case #"<<cas<<": "<<*itr<<" won"<<endl;
                                                                                
                                                           ans=1;
                                                                                 }
                                           
                                              s2.clear();
                                              //goto ttt;
                                              }
                     if(ans==1)
                     goto ttt;
               for(int i=0;i<4;i++)
               for(int j=0;j<4;j++)
               if(v[i][j]=='.')
               {  fout<<"Case #"<<cas<<": "<<"Game has not completed"<<endl;goto ttt;}
               cout<<endl;
               //goto ttt;
               fout<<"Case #"<<cas<<": "<<"Draw"<<endl;
              // system("pause");
               
               
               ttt:;
               v.clear();
               }
 //system("pause");
    return 0;

}


