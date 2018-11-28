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
              long int ocur=1;
              long int bcur=1;
              long int otime=0;
              long int btime=0;
              long int n;
              char arr[300];
              long int pos[300];
              cin>>n;
              for(long int j=0;j<n;j++)
              {
                      cin>>arr[j];
                      cin>>pos[j];
              }
              for(long int k=0;k<n;k++)
              {
                      if(arr[k]=='O')
                      {
                              if(ocur<pos[k])
                              {
                                  if(otime<(pos[k]-ocur))
                                  {
                                                         s=s+pos[k]-ocur+1-otime;
                                                         btime=btime + pos[k]-ocur+1-otime;
                                  }
                                  if(otime>=(pos[k]-ocur))
                                  {
                                                        s=s+1;
                                                        btime=btime+1;
                                  }
                                  otime=0;
                                  ocur=pos[k];           
                              }
                              else
                              {
                              if(ocur>pos[k])
                              {
                                      if(otime<(ocur-pos[k]))
                                  {
                                                         s=s+ocur-pos[k]+1-otime;
                                                         btime=btime + ocur-pos[k]+1-otime;
                                  }
                                  if(otime>=(ocur-pos[k]))
                                  {
                                                        s=s+1;
                                                        btime=btime+1;
                                  }
                                  otime=0;
                                  ocur=pos[k];
                              }
                              else             
                              {
                              if(ocur==pos[k])
                              {
                               s=s+1;
                               ocur=pos[k];
                               btime=btime+1;
                               otime=0;               
                              }
                              }
                              }
                      }      
                      if(arr[k]=='B')
                      {
                               if(bcur<pos[k])
                              {
                                  if(btime<(pos[k]-bcur))
                                  {
                                                         s=s+pos[k]-bcur+1-btime;
                                                         otime=otime + pos[k]-bcur+1-btime;
                                  }
                                  if(btime>=(pos[k]-bcur))
                                  {
                                                        s=s+1;
                                                        otime=otime+1;
                                  }
                                  
                                  btime=0;
                                  bcur=pos[k];           
                              }
                              else
                              {
                              if(bcur>pos[k])
                              {
                                      if(btime<(bcur-pos[k]))
                                  {
                                                         s=s+bcur-pos[k]+1-btime;
                                                         otime=otime + bcur-pos[k]+1-btime;
                                  }
                                  if(btime>=(bcur-pos[k]))
                                  {
                                                        s=s+1;
                                                        otime=otime+1;
                                  }
                                  btime=0;
                                  bcur=pos[k];
                              }
                              else             
                              {
                              if(bcur==pos[k])
                              {
                               s=s+1;
                               bcur=pos[k];
                               otime=otime+1;
                               btime=0;               
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
