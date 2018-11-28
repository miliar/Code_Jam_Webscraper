#include<iostream>
#include<fstream>
using namespace std;

int main()
{   ifstream fin;
    fstream fout;
    fin.open("B-small-attempt2.in");
    fout.open("Output.txt");
    int i,j,k,n,t,s,p,total,count=0;
    int score[100];
    fin>>n;
    for(i=1;i<=n;i++)
    {
                     fin>>t>>s>>p;
                     
                     count = 0;
                     for(j=0;j<t;j++)
                                     {fin>>score[j];
                     
                                      }
                     for(j=0;j<t;j++)
                     {
                                     for(k=p;k<=10;k++)
                                     {
                                     if(score[j]>=k)
                                     {
                                                  total=score[j]-k;
                                                  if(s==0)
                                                  {
                                                          if(k!=0)
                                                          {        if(total==k+1 + k || total == k + 1 + k + 1 || total == k + k || total == k-1 + k-1 || total==k-1 + k )
                                                                       { count ++;
                                                          
                                                                         break;
                                                                       }
                                                          }
                                                          else if (k==0)
                                                          {       if(total==k+1 + k || total == k + 1 + k + 1 || total == k + k)
                                                                       { count ++;
                                                                       
                                                                         break;
                                                                       }
                                                          }
                                                          else if(k==10)
                                                          {        if( total == k + k || total == k-1 + k-1 || total==k-1 + k )
                                                                       { count ++;
                                                                       
                                                                         break;
                                                                       }           
                                                          } 
                                                           
                                                  }
                                                  else
                                                  {
                                                           if(k==0)
                                                           {
                                                           if(total==k+1 + k || total == k + 1 + k + 1 || total == k + k)
                                                                       { count ++;
                                                                         
                                                                         break;
                                                                       }
                                                           else if(total== k+1 + k+2 ||  total == k + 2+ k+2 || total ==k+2 + k)  
                                                                {
                                                                           count++;
                                                                           s--;
                                                                
                                                                           break;
                                                                }
                                                           }
                                                           else if(k==10)
                                                           {
                                                                if( total == k + k || total == k-1 + k-1 || total==k-1 + k )
                                                                       { count ++;
                                                           
                                                                         break;
                                                                       }
                                                                else if(total ==k-2+ k || total == k-2 + k-2 || total ==k-2 + k-1|| total==k-1 + k+1 )  
                                                                {
                                                                           count++;
                                                                           s--;
                                                  
                                                                           break;
                                                                }
                                                           }
                                                           else if(k==1)
                                                           {
                                                                if(total==k+1 + k || total == k + 1 + k + 1 || total == k + k || total == k-1 + k-1 || total==k-1 + k )
                                                                       { count ++;
                                                                         
                                                                         break;
                                                                       }
                                                           else if(total== k+1 + k+2 ||  total == k + 2+ k+2 || total ==k+2 + k|| total==k-1 + k+1 )  
                                                                {
                                                                           count++;
                                                                           s--;
                                                                
                                                                           break;
                                                                }
                                                           }
                                                           else if(k==9)
                                                           {
                                                                if(total==k+1 + k || total == k + 1 + k + 1 || total == k + k || total == k-1 + k-1 || total==k-1 + k )
                                                                       { count ++;
                                                                       
                                                                         break;
                                                                       }
                                                           else if( total ==k-2+ k || total == k-2 + k-2 || total ==k-2 + k-1|| total==k-1 + k+1 )  
                                                                {
                                                                           count++;
                                                                           s--;
                                                                           
                                                                           break;
                                                                }
                                                           }
                                                           else
                                                           {
                                                               if(total==k+1 + k || total == k + 1 + k + 1 || total == k + k || total == k-1 + k-1 || total==k-1 + k )
                                                                       { count ++;
                                                                       
                                                                         break;
                                                                       }
                                                           else if(total== k+1 + k+2 ||  total == k + 2+ k+2 || total ==k+2 + k|| total ==k-2+ k || total == k-2 + k-2 || total ==k-2 + k-1|| total==k-1 + k+1 )  
                                                                {
                                                                           count++;
                                                                           s--;
                                                                
                                                                           break;
                                                                }
                                                           }
                                                           
                                                  }
                                     }
                                     }
                     
                     }
                     
                     fout<<"Case #"<<i<<": "<<count<<"\n";
    }
    
    return 0;
}  
