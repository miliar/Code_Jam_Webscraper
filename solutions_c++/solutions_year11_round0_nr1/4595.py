#include<iostream>
#include<stdlib.h>
using namespace std;
 
int main()
{
    long n;
    cin>>n;
    
    for(long k=0;k<n;k++)
    {
            long t;
            cin>>t;
            long a[100];
            char ch[100];
            long val[100];
            for(long i=0;i<t;i++)
            {
                    a[i]=0;
            }
            for(long l=0;l<t;l++)
            {
                    cin>>ch[l]>>val[l];
            }
            for(long i=0;i<t;i++)
            {
                    if(ch[i]=='O')
                    {
                                  long j=i-1;
                                  long steps=0;
                                  long count=val[i];
                                  long pos = 1;
                                  while(j>=0 && ch[j]=='B')
                                  {
                                             steps+=a[j];
                                             j--;
                                             }
                                  if(j>=0)
                                  {
                                          if(ch[j]=='O')
                                          {
                                                        count = (long)abs(val[i]-val[j]);
                                                        pos=0;
                                                        }
                                  }
                                  if(steps>=count)
                                                  a[i]=1;
                                                  else
                                                  a[i]=count-steps+1-pos;
                    }
                    if(ch[i]=='B')
                    {
                                  long j=i-1;
                                  long steps=0;
                                  long count=val[i];
                                  long pos=1;
                                  while(j>=0 && ch[j]=='O')
                                  {
                                             steps+=a[j];
                                             j--;
                                             }
                                  if(j>=0)
                                  {
                                          if(ch[j]=='B')
                                          {
                                                        count = (long)abs(val[i]-val[j]);
                                                        pos=0;
                                                        }
                                  }
                                  if(steps>=count)
                                                  a[i]=1;
                                                  else
                                                  a[i]=count-steps+1-pos;
                    }
            }
            long value=0;
            for(long i=0;i<t;i++)
            {
//                    cout<<"a="<<a[i]<<"\tval="<<val[i]<<"\tch="<<ch<<endl;
                      value+=a[i];
            }
            cout<<"Case #"<<k+1<<": "<<value<<endl;
    }
    return 0;
}