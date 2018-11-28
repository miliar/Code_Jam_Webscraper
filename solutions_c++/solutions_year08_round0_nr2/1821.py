#include<iostream>

using namespace std;

struct Time{
   int h; int m; int AD;
   };
bool lessthan(Time t1,Time t2)
           {
	      if(t1.h*60+t1.m<t2.h*60+t2.m) return true;
             if(t1.h*60+t1.m==t2.h*60+t2.m && t1.AD==0 && t2.AD==1)return true;
             return false;
             };
void Addt(Time &T,int t)
   {int oh=T.h;int om=T.m;
      T.m=(om+t)%60;
      T.h=(oh+(om+t)/60)%24;}
                
void sort(Time *T,int SZ)
 {for(int i=0;i<SZ-1;i++)
   {for(int j=i+1;j<SZ;j++)
        if(lessthan(T[j],T[i]))
         {Time t=T[j];
                T[j]=T[i];
                T[i]=t;}}}
                               
                
int main()
{int Ntc;
 Time aD[105];Time aA[105];Time bD[105];Time bA[105];
 Time scha[210];
 Time schb[210];
 int ttt;
 int NA;
 int NB;
 int SZ;
 cin>>Ntc;
 for(int tc=1;tc<=Ntc;tc++)
 {
  cin>>ttt;
  cin>>NA;cin>>NB;SZ=NA+NB;
  int h1=0,m1=0,h2=0,m2=0;
 for(int i=0;i<NA;i++)
 {
  scanf("%d:%d %d:%d",&h1,&m1,&h2,&m2);
  
 aD[i].h=h1;aD[i].m=m1;aD[i].AD=1;
 bA[i].h=h2;bA[i].m=m2;bA[i].AD=0;
 }
 for(int i=0;i<NB;i++)
 {
  scanf("%d:%d %d:%d",&h1,&m1,&h2,&m2);
 
 bD[i].h=h1;bD[i].m=m1;bD[i].AD=1;
 aA[i].h=h2;aA[i].m=m2;aA[i].AD=0;

 }
 int resa=0;
 int resb=0;
 int ct=0;
 for(int i=0;i<NA;i++)
   scha[i]=aD[i];
 for(int i=NA;i<SZ;i++)
  scha[i]=aA[i-NA];
  
 for(int i=NA;i<SZ;i++)
  Addt(scha[i],ttt);
  sort(scha,SZ);

  for(int i=0;i<SZ;i++)
  {if(scha[i].AD==0)
      {ct++;}
      else{ct--;
                  resa=(ct<resa)?ct:resa;}}
  if(resa<0){resa=-resa;}else{resa=0;}
  ct=0;
   for(int i=0;i<NB;i++)
   schb[i]=bD[i];
 for(int i=NB;i<SZ;i++)
  schb[i]=bA[i-NB];
 for(int i=NB;i<SZ;i++)
  Addt(schb[i],ttt);
  sort(schb,SZ);
  for(int i=0;i<SZ;i++)
  {if(schb[i].AD==0)
      {ct++;}
      else{ct--;
                  resb=(ct<resb)?ct:resb;}}
  if(resb<0){resb=-resb;}else{resb=0;}
  printf("Case #%d: %d %d \n",tc,resa,resb);
  }
  }
  
 
