#include<cstdio>
#include<iostream>
#include<string>
#include<vector>
#include<map>
using namespace std;

int main()
    {
          int N;
          char a[200];
          scanf("%d",&N);
          int Case=1;
          while(N--)
           {
              int S,Q;
              string tmp;
              map<string,bool> M;
              vector<string> Vq;
              scanf("%d\n",&S);
              //cout<<S<<endl;
              for(int i=0;i<S;i++)
               {
                      tmp="";
                      gets(a);
                      for(int j=0;j<strlen(a);j++)
                       tmp+=a[j];
                      M[tmp]=1;
                      //cout<<tmp<<endl;
               } 
              scanf("%d\n",&Q);
              // cout<<Q<<endl;
              for(int i=0;i<Q;i++)
                {
                    tmp="";
                    gets(a);
                    for(int j=0;j<strlen(a);j++)
                       tmp+=a[j];
                     //cout<<tmp<<endl;  
                    Vq.push_back(tmp);
                }
                
              int count=S;
              int swich=0;
              int c=0;
              /*map<string, bool>::iterator it;
              for(it=M.begin();it!=M.end();it++)
                    cout<<it->first<<" "<<it->second<<endl;*/  
              for(int i=0;i<Q;i++)
               {
                      tmp=Vq[i];
                      //cout<<tmp<<" "<<count<<" ";
                      if(M[tmp]==true && count>1)
                       {
                                      M[tmp]=false;
                                      count--;
                                      //cout<<count<<endl;
                                      continue;
                       }
                      else if(M[tmp]==false)
                        continue;
                       
                     swich++;
                     i--;
                     //cout<<"swich "<<swich<<endl;
                     map<string, bool>::iterator it;
                     for(it=M.begin();it!=M.end();it++)
                      it->second=true;  
                     count=S; 
              }
              printf("Case #%d: %d\n",Case++,swich);
                        
           }
    }
