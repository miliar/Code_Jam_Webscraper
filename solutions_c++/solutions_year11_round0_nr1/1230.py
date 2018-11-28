#include<iostream>
#include<fstream>

using namespace std;

int stay(int a){return a+1;}
int push(int a){return a+1;}
int walk(int a){return a+1;}

int main()
{
    int T,N;
    char c;
    ifstream in;
    in.open("A-large.in");
    ofstream out;
    out.open("output.txt");
    in>>T;
                  for(int i=0;i<T;i++)
                  {
                   in>>N;
                   int po=1,pb=1;
                   char arr[N];
                   int o[N],b[N];
                   for(int j=0,k=0,l=0;j<N;j++)
                   {
                    in>>c;
                    arr[j]=c; 
                    if(c=='O')
                    {
                     in>>o[k];
                     k++;         
                    }   
                    if(c=='B')
                    {
                     in>>b[l];
                     l++;         
                    }    
                   }
                   int res=0;
                   char t;
                   int t1=0,t2=0;
                   for(int j=0,k=0,l=0;j<N;j++)
                   {
                    t=arr[j];
                    if(t=='O')
                    { 
                     t1=o[k];
                     k++;
                     t2=b[l];
                     if(po==t1)
                     {
                      if(t2==pb){}
                      else{if(t2>pb){pb++;}else{pb--;}}
                      res++;      
                     }
                     if(po<t1)
                     {
                      while(po!=t1)
                      {
                       if(t2==pb){}
                       else{if(t2>pb){pb++;}else{pb--;}}  
                       res++;
                       po++;            
                      } 
                      if(t2==pb){}
                      else{if(t2>pb){pb++;}else{pb--;}}
                      res++;      
                     }
                     if(po>t1)
                     {
                      while(po!=t1)
                      {
                       if(t2==pb){}
                       else{if(t2>pb){pb++;}else{pb--;}}  
                       res++;
                       po--;            
                      } 
                      if(t2==pb){}
                      else{if(t2>pb){pb++;}else{pb--;}} 
                      res++;      
                     }      
                    } 
                    
                    else
                    { 
                     t1=b[l];
                     l++;
                     t2=o[k];
                     if(pb==t1)
                     {
                      if(t2==po){}
                      else{if(t2>po){po++;}else{po--;}}
                      res++;      
                     }
                     if(pb<t1)
                     {
                      while(pb!=t1)
                      {
                       if(t2==po){}
                       else{if(t2>po){po++;}else{po--;}}  
                       res++;
                       pb++;            
                      } 
                      if(t2==po){}
                      else{if(t2>po){po++;}else{po--;}}
                      res++;      
                     }
                     if(pb>t1)
                     {
                      while(pb!=t1)
                      {
                       if(t2==po){}
                       else{if(t2>po){po++;}else{po--;}}  
                       res++;
                       pb--;            
                      } 
                      if(t2==po){}
                      else{if(t2>po){po++;}else{po--;}} 
                      res++;      
                     }      
                    }
                    
                    }
                    out<<"Case #"<<i+1<<": "<<res<<endl;
                   }
                          in.close();
                          out.close();


    system("pause");
    return 0;
}
