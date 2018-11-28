#include<iostream>
#include<conio.h>
using namespace std;
int main()
{
    long int t;
    cin>>t;
    int i=0;
    while(i<t)
    {
              long int s=0;
              long int ocurrent=1;
              long int bcurrent=1;
              long int otime=0;
              long int btime=0;
              long int n;
              char a[500];
              long int pos[500];
              cin>>n;
              for(long int j=0;j<n;j++)
              {
                      cin>>a[j];
                      cin>>pos[j];
              }
              for(long int k=0;k<n;k++)
              {
                     
                      if(a[k]=='B')
                      {
                               if(bcurrent<pos[k])
                              {
                                  if(btime<(pos[k]-bcurrent))
                                  {
                                                         s=s+pos[k]-bcurrent+1-btime;
                                                         otime=otime + pos[k]-bcurrent+1-btime;
                                  }
                                  if(btime>=(pos[k]-bcurrent))
                                  {
                                                        s=s+1;
                                                        otime=otime+1;
                                  }
                                  
                                  btime=0;
                                  bcurrent=pos[k];           
                              }
                              else
                              {
                              if(bcurrent>pos[k])
                              {
                                      if(btime<(bcurrent-pos[k]))
                                  {
                                                         s=s+bcurrent-pos[k]+1-btime;
                                                         otime=otime + bcurrent-pos[k]+1-btime;
                                  }
                                  if(btime>=(bcurrent-pos[k]))
                                  {
                                                        s=s+1;
                                                        otime=otime+1;
                                  }
                                  btime=0;
                                  bcurrent=pos[k];
                              }
                              else             
                              {
                              if(bcurrent==pos[k])
                              {
                               s=s+1;
                               bcurrent=pos[k];
                               otime=otime+1;
                               btime=0;               
                              }
                              }
                              }              
                      }
                       if(a[k]=='O')
                      {
                              if(ocurrent<pos[k])
                              {
                                  if(otime<(pos[k]-ocurrent))
                                  {
                                                         s=s+pos[k]-ocurrent+1-otime;
                                                         btime=btime + pos[k]-ocurrent+1-otime;
                                  }
                                  if(otime>=(pos[k]-ocurrent))
                                  {
                                                        s=s+1;
                                                        btime=btime+1;
                                  }
                                  otime=0;
                                  ocurrent=pos[k];           
                              }
                              else
                              {
                              if(ocurrent>pos[k])
                              {
                                      if(otime<(ocurrent-pos[k]))
                                  {
                                                         s=s+ocurrent-pos[k]+1-otime;
                                                         btime=btime + ocurrent-pos[k]+1-otime;
                                  }
                                  if(otime>=(ocurrent-pos[k]))
                                  {
                                                        s=s+1;
                                                        btime=btime+1;
                                  }
                                  otime=0;
                                  ocurrent=pos[k];
                              }
                              else             
                              {
                              if(ocurrent==pos[k])
                              {
                               s=s+1;
                               ocurrent=pos[k];
                               btime=btime+1;
                               otime=0;               
                              }
                              }
                              }
                      }      
              }
              
              
    i++;
    
    cout<<"Case #"<<i<<": "<<s<<"\n";          
    }
    getch();
}
