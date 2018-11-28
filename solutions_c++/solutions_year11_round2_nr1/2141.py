#include<iostream>
#include<string>

using namespace std;

int main()
    {
          long long t,i,n,j,k,l;
          double temp,temp1,count,count1;
          cin>>t;
          for(i=0;i<t;i++)
          {
               cin>>n;
               string a[n];
               double wp[n],owp[n],oowp[n],rpi[n];
               for(j=0;j<n;j++)
                    cin>>a[j];
               for(j=0;j<n;j++)
               {
                    temp=0.0; 
                    temp1=0.0;  
                    for(k=0;k<a[j].length();k++)
                    {
                         if(a[j][k]!='.')
                              temp+=1.0;
                         if(a[j][k]=='1')
                              temp1+=1.0;
                    }       
                    wp[j]=(double)(temp1/temp);   
               }
               for(j=0;j<n;j++)
               {
                    count=0.0;  
                    count1=0.0;                   
                    for(k=0;k<n;k++)
                    {
                         temp=0.0;
                         temp1=0.0;            
                         if(k==j)
                             continue;
                         if(a[j][k]!='.')
                         {
                              for(l=0;l<a[k].length();l++)
                              {
                                  if(l==j)
                                      continue;
                                  if(a[k][l]!='.')                        
                                      temp+=1;
                                  if(a[k][l]=='1')    
                                      temp1+=1;
                              }
                              count1+=(temp1/temp);
                              count+=1;
                         }
                         
                    }         
                    owp[j]=(count1/count);
               }
               
               
               
               for(j=0;j<n;j++)
               {
                    temp=0.0; 
                    temp1=0.0;          
                    for(k=0;k<a[j].length();k++)
                    {
                         if(a[j][k]!='.')
                         {
                              temp+=1;
                              temp1+=owp[k];
                         }
                    }           
                    oowp[j]=(temp1/temp);   
               }
               cout<<"Case #"<<i+1<<":"<<endl;
               for(j=0;j<n;j++)
               {
                    rpi[j]=0.25*wp[j]+0.5*owp[j]+0.25*oowp[j];
                    cout<<rpi[j]<<endl;
               }
               
          }
          return 0;
    }
