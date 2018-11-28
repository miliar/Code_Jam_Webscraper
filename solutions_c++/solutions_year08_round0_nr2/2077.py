#include <iostream>
#include <stdio.h>

using namespace std;

int main()

{
long x,wt,am,bm,ad[100],bd[100],aa[100],ba[100],temp1,temp2;
long ay=0,by=0,an=0,bn=0,o;
cin>>x;
for (int i=0;i<x;i++)
         {
              ay=0,by=0,an=0,bn=0;
              cin>>wt;
              cin>>am;
              cin>>bm;       
              for(int y=0;y<am;y++)
                      {cin>>temp1;cin>>temp2;
                       ad[y]=temp1*60+temp2;
                       cin>>temp1;cin>>temp2;
                       aa[y]=temp1*60+temp2;}
              for(int z=0;z<bm;z++)
                      {cin>>temp1;cin>>temp2;
                       bd[z]=temp1*60+temp2;
                       cin>>temp1;cin>>temp2;
                       ba[z]=temp1*60+temp2;}        
              for (int t=0;t<1440;t++)
                  {
                       for (int l=0;l<am;l++)                              
                                         if((aa[l]+wt)==t)by++;
                       for (int m=0;m<bm;m++)                  
                                         if((ba[m]+wt)==t)ay++;      
                       for (int j=0;j<am;j++)
                           {
                                         if(ad[j]==t)
                                                     {
                                                     if(ay>0)ay--;
                                                     else an++;
                                                     }
                           }
                       for (int k=0;k<bm;k++)
                           {                     
                                          if(bd[k]==t)
                                                     {
                                                     if(by>0)by--;
                                                     else bn++;
                                                     }           
                           }
                              
                           
                  }                                                       
         cout<<"Case #"<<i+1<<": "<<an<<" "<<bn<<endl;
         }
}                                     
                                                         
