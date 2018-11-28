#include <iostream>
#include <fstream>
using namespace std;
char a[500][2][30],b[500][2][30];
int na,nb,t,i,j,k,n;
ifstream fin;
int ans[3],temp,size[500],all,flag[500],now;
int time1[500][3];
int find(int now)
 {
  int i,j,k,minb,mine,temp;
  temp=0;
  mine=32700 ;
  minb=32700;
  for (i=1;i<=all;i++)
  {   //cout<<time1[now][2]+t<<"  "<<time1[i][1]<<endl;
       if ((flag[i]==0) && ((time1[now][2]+t)<=time1[i][1]) && (size[now]!=size[i]) )
    {
        if ((time1[i][1])<minb) {minb=time1[i][1];mine=time1[i][2];temp=i; continue;}
        if (((time1[i][1])==minb) && (time1[i][2]<mine)) {mine=time1[i][2];temp=i; continue;}
    }
  }
  return temp;
 }
int main()
 {
     fin.open("b.in");
     fin>>n;
     ofstream fout;
     fout.open("b.out");
     for (k=1;k<=n;k++)
      { ans[1]=0;
        ans[2]=0;
        fin>>t;
        fin>>na>>nb;
        for(i=1;i<=500;i++)
         {
          flag[i]=0;
         };
        for (i=1;i<=na;i++)
          {fin>>a[i][1];
           fin>>a[i][2];
           time1[i][1]=int((a[i][1][0]-'0')*10*60+(a[i][1][1]-'0')*60+(a[i][1][3]-'0')*10
                          +(a[i][1][4]-'0'));
           time1[i][2]=int((a[i][2][0]-'0')*10*60+(a[i][2][1]-'0')*60+(a[i][2][3]-'0')*10
                          +(a[i][2][4]-'0'));                 
                      size[i]=1;
           };
        for (i=1;i<=nb;i++)
          {fin>>b[i][1];
           fin>>b[i][2];
           time1[i+na][1]=int((b[i][1][0]-'0')*10*60+(b[i][1][1]-'0')*60+(b[i][1][3]-'0')*10
                          +(b[i][1][4]-'0'));
           time1[i+na][2]=int((b[i][2][0]-'0')*10*60+(b[i][2][1]-'0')*60+(b[i][2][3]-'0')*10
                          +(b[i][2][4]-'0'));                 
           size[i+na]=2;     
          
          };      
          all=na+nb;
       for (i=1;i<=all-1;i++)
        for (j=i+1;j<=all;j++)
         {
           if (time1[i][1]>time1[j][1])
           {
            temp=size[i];
            size[i]=size[j];
            size[j]=temp;
            
            temp=time1[i][1];
            time1[i][1]=time1[j][1];
            time1[j][1]=temp;
            
            temp=time1[i][2];
            time1[i][2]=time1[j][2];
            time1[j][2]=temp;
            }
         };   
      for (i=1;i<=all;i++)
       {  if (flag[i]==0)
           {
             ans[size[i]]++;
                   flag[i]=1;
             now=i; 
             while (find(now)!=0)
              { 
                   temp=find(now);
                   flag[temp]=1;
                   now=temp;
              }
            }
       }
      fout<<"Case #"<<k<<":"<<" "<<ans[1]<<" "<<ans[2]<<endl;    
       } 
        fin.close();
       
 }

