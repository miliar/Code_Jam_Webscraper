#include<iostream>
#include<vector>
#include<cstdio>

using namespace std;

int main()
{
     char c;
    int val;
    int n,size;
    cin>>n;
    for(int q=0;q<n;q++)
    {
            cin>>size;
            int cpo=1,cpb=1,time=0;
            vector<char> m;
            vector<int> o;
            vector<int> b;
            for(int w=0;w<size;w++)
            {
                    cin>>c;
                    m.push_back(c);
                    cin>>val;
                    if(c=='B')
                              b.push_back(val);
                    else
                              o.push_back(val);
            }
            int val;
           
            for(int i=0;i<size;i++)
            {
                     if(o.size()<1)
                                     cpo=-1;
                     if(b.size()<1)
                                     cpb=-1;   
                    if(m[i]=='B')
                     {                     
                                 val=abs(b[0]-cpb);
                                 val++;
                                 time+=val;
                                 
                                 if(cpo>0)
                                 if(val>abs(o[0]-cpo))
                                    cpo=o[0];
                                  else
                                        if(abs(o[0]-(cpo+1))<abs(o[0]-cpo))
                                              cpo+=val;
                                        else
                                               cpo-=val;
                                  cpb=b[0];
                                  b.erase(b.begin());
                      }
                      else
                      {
                                  val=abs(o[0]-cpo);
                                 val++;
                                 time+=val;
                                 
                                 if(cpb>0)
                                 if(val>abs(b[0]-cpb))
                                    cpb=b[0];
                                  else
                                        if(abs(b[0]-(cpb+1))<abs(b[0]-cpb))
                                              cpb+=val;
                                        else
                                               cpb-=val;
                                  cpo=o[0];
                                  o.erase(o.begin());
                      }           
            }
            cout<<"Case #"<<q+1<<": "<<time<<endl;
    }
    return 0;
}                  
    
