#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <ctime>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <sstream>
using namespace std;





int main() 
{ 
//    freopen("..\\A.in","r",stdin); 
//    freopen("A-small-attempt0.in","r",stdin);freopen("A-small-attempt0.out","w",stdout); 
//   freopen("A-small-practice.in","r",stdin);freopen("A-small-practice.out","w",stdout); 
    freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout); 
//    freopen("..\\A-small.in","r",stdin);freopen("..\\A-small.out","w",stdout);
    int T;
    int N,M;
    while (scanf ("%d",&T)!=EOF)
    {
          for (int count=1;count<=T;count++)
          {
                cin>>N>>M;
                vector<string> s;
                for (int i=0;i<N;i++)
                {
                    string temp;
                    cin>>temp;
                    s.push_back(temp);
                    for (int j=temp.size()-1;j>0;j--)
                    {
                        bool flag=false;
                        if (temp[j]=='/')
                        {
                            string  t(temp,0,j);
                            //cout<<t<<endl;
                            for (int k=0;k<s.size();k++)
                            {
                                if (t==s[k])
                                {
                                    flag=true;
                                    break; 
                                }   
                            }   
                            if (flag==false)
                                s.push_back(t);
                        }    
                    }    
                }
                int res=0;
                for (int i=0;i<M;i++)
                {
                    string temp;
                    cin>>temp;
                    bool flag=false;
                    for (int j=0;j<s.size();j++)
                    {
                        if (temp==s[j])
                        {
                            flag=true;
                            break;    
                        }
                    }
                    if (flag==false)
                    {
                        s.push_back(temp);
                        res++;
                        for (int k=temp.size()-1;k>0;k--)
                        {
                            if (temp[k]=='/')
                            {
                                string  t(temp,0,k);
                                //cout<<t<<endl;
                                for (int l=0;l<s.size();l++)
                                {
                                    if (t==s[l])
                                    {
                                        flag=true;
                                        break; 
                                    }   
                                }   
                                if (flag==false)
                                {
                                    s.push_back(t);
                                    res++;
                                }
                            }   
                        }
                    }
                }
                //int res=0;
                
              cout<<"Case #"<<count<<": "<<res<<endl;
          }      
    }
    return 0; 
} 



                 
