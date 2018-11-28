#include<iostream>
using namespace std;
int main()
{
    int T,N,S,p,a,d=1;
    cin>>T;
    while(T--)
    {
              cin>>N>>S>>p;
              int count=0;
              if(p==0)
              {
                      for(int i=0;i<N;i++)
                      {
                              cin>>a;
                      }
                      cout<<"Case #"<<d<<": ";
                      cout<<N<<endl;
                      d++;
              }
              else
              {
              for(int i=0;i<N;i++)
              {
                      cin>>a;
                      if(a>0)
                      {
                      if(a%3==0)
                      {
                                if(a/3>=p)
                                {
                                          count++;
                                }
                                else if(a/3+1>=p && S>0)
                                {
                                     S--;
                                     count++;
                                }
                      }
                      else if(a%3==1)
                      {
                           int n=a/3;
                           if(n>=p)
                           {
                                   count++;
                           }
                           else if(a-2*n>=p)
                           {
                                count++;
                           }
                           else
                           {
                               n++;
                               if(n>=p)
                               {
                                       if(((a-2*n)-n>=2 || n-(a-2*n)>=2) && S>0)
                                       {
                                                       count++;
                                                       S--;
                                       }
                               }
                               else if(a-2*n>=p)
                               {
                                    if(((a-2*n)-n>=2 || n-(a-2*n)>=2) && S>0)
                                    {
                                                    count++;
                                                    S--;
                                    }
                               }
                           }
                      }
                      else if(a%3==2)
                      {
                           int n=a/3;
                           n++;
                           if(n>=p)
                           {
                                   count++;
                           }
                           else if(a-2*n>=p)
                           {
                                count++;
                           }
                           else
                           {
                               n--;
                               if(n>=p)
                               {
                                       if(((a-2*n)-n>=2 || n-(a-2*n)>=2) && S>0)
                                       {
                                                       count++;
                                                       S--;
                                       }
                               }
                               else if(a-2*n>=p)
                               {
                                    if(((a-2*n)-n>=2 || n-(a-2*n)>=2) && S>0)
                                    {
                                                    count++;
                                                    S--;
                                    }
                               }
                           }
                      }
                      }
              }
              cout<<"Case #"<<d<<": ";
              cout<<count<<endl;
              d++;
              }
    }
    return 0;
}
