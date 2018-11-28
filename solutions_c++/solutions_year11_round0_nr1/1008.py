#include<iostream>
#include<fstream>
#include<queue>

using namespace std;



int main()
{
    int T,N;
    char c;
    ifstream in;
    in.open("large.in");
    ofstream out;
    out.open("Answer.txt");
    in>>T;
                  for(int i=0;i<T;i++)
                  {
                   in>>N;
                   int Ostep=1,Pstep=1;
                   char arr[N];
                   int Oarr[N],b[N];
                   for(int j=0,k=0,l=0;j<N;j++)
                   {
                    in>>c;
                    arr[j]=c; 
                    if(c=='O')
                    {
                     in>>Oarr[k];
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
                   int temp1=0,temp2=0;
                   for(int j=0,k=0,l=0;j<N;j++)
                   {
                    t=arr[j];
                    if(t=='O')
                    { 
                     temp1=Oarr[k];
                     k++;
                     temp2=b[l];
                     if(Ostep==temp1)
                     {
                      if(temp2==Pstep){}
                      else{if(temp2>Pstep){Pstep++;}else{Pstep--;}}
                      res++;      
                     }
                     if(Ostep<temp1)
                     {
                      while(Ostep!=temp1)
                      {
                       if(temp2==Pstep){}
                       else{if(temp2>Pstep){Pstep++;}else{Pstep--;}}  
                       res++;
                       Ostep++;            
                      } 
                      if(temp2==Pstep){}
                      else{if(temp2>Pstep){Pstep++;}else{Pstep--;}}
                      res++;      
                     }
                     if(Ostep>temp1)
                     {
                      while(Ostep!=temp1)
                      {
                       if(temp2==Pstep){}
                       else{if(temp2>Pstep){Pstep++;}else{Pstep--;}}  
                       res++;
                       Ostep--;            
                      } 
                      if(temp2==Pstep){}
                      else{if(temp2>Pstep){Pstep++;}else{Pstep--;}} 
                      res++;      
                     }      
                    } 
                    
                    else
                    { 
                     temp1=b[l];
                     l++;
                     temp2=Oarr[k];
                     if(Pstep==temp1)
                     {
                      if(temp2==Ostep){}
                      else{if(temp2>Ostep){Ostep++;}else{Ostep--;}}
                      res++;      
                     }
                     if(Pstep<temp1)
                     {
                      while(Pstep!=temp1)
                      {
                       if(temp2==Ostep){}
                       else{if(temp2>Ostep){Ostep++;}else{Ostep--;}}  
                       res++;
                       Pstep++;            
                      } 
                      if(temp2==Ostep){}
                      else{if(temp2>Ostep){Ostep++;}else{Ostep--;}}
                      res++;      
                     }
                     if(Pstep>temp1)
                     {
                      while(Pstep!=temp1)
                      {
                       if(temp2==Ostep){}
                       else{if(temp2>Ostep){Ostep++;}else{Ostep--;}}  
                       res++;
                       Pstep--;            
                      } 
                      if(temp2==Ostep){}
                      else{if(temp2>Ostep){Ostep++;}else{Ostep--;}} 
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
