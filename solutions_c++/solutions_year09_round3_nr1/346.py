#include<iostream>
#include<math.h>

using namespace std;
int main()
{
 char ch;
 int T,c=0,l,i,j;
 scanf("%d\n",&T);
 while(c++<T)
 {
  int flag[125]={0};i=0;int base=0;
  char A[10];
  while((ch=getchar())!='\n')
   {A[i++]=ch;
    j=ch-'0';//cout<<j<<" ";
    flag[j]=1;
    }
    l=i;
    //cout<<l<<" ";
   for(i=0;i<125;i++)
   {//cout<<flag[i]<<" ";
    if(flag[i]!=0) base++;
   }
   //base++;
   //cout<<base<<" ";
   if(base<2) base=2;
   int num[10];
   int flag1[l];
   for(i=0;i<l;i++) flag1[i]=0;
   num[0]=1;flag1[0]=1;
   //flag[A[0]-'0']=1;
   for(i=0;i<l;i++)
    {if(A[i]==A[0]) {num[i]=1;flag1[i]=1;}}
   int cnt=2;int flg=0;
   
   for(i=1;i<l;i++)
   {
    if(flag1[i]) continue;
    flag1[i]=1;
    if(flg)
     num[i]=cnt++;
    else
     { num[i]=0;flg=1;}
    for(j=2;j<l;j++)
    {if(A[j]==A[i]) {num[j]=num[i];flag1[j]=1;}}
   }
   
   long long sum=0;
   for(i=l-1,j=0;i>=0;i--,j++)
   { sum+=(long long) num[i]*pow(base,j);}
   cout<<"Case #"<<c<<": "<<sum<<endl;
  }
 return 0;
}   
