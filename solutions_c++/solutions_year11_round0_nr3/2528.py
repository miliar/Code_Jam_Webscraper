#include<iostream>
#include<cstdio>
using namespace std;
int a[1001];
void quicksort(int,int);
int main()
{
 FILE *fp1,*fp2;
 int t,i,n,j,u,s,s1,s2,s3,maxi,v;
 fp1=fopen("C-large.in","r");
 fp2=fopen("candysplittinglarge1.out","w");
 fscanf(fp1,"%d",&t);
 for(i=1;i<=t;i++)
 {
  fscanf(fp1,"%d",&n);
  for(j=0;j<n;j++)
  {
   fscanf(fp1,"%d",&a[j]);
  }
  quicksort(0,n-1); 
  maxi=-1;
  for(j=0;j<(n-1);j++)
  {
   s=0;
   s2=0;
   for(u=0;u<=j;u++)
   {
    s=s^a[u];
    s2=s2+a[u];
   }
   s1=0;
   s3=0;
   for(u=(j+1);u<n;u++)
   {
    s1=s1^a[u];
    s3=s3+a[u];
   }
   if(s==s1)
   {
    v=s2;
    if(v<s3)
    v=s3;
    if(maxi<v)
    maxi=v;
   }
  }
  if(maxi!=-1)
  fprintf(fp2,"Case #%d: %d\n",i,maxi);
  else
  fprintf(fp2,"Case #%d: NO\n",i);
 }
 fclose(fp1);
 fclose(fp2);
 return(0);
}
void quicksort(int left,int right)
{
 int pivot,i,j,temp;
 if(left<right)
 {
  i=left;
  j=right+1;
  pivot=a[left];
  do
  {
   do
   {
    i=i+1;
   }while((a[i]<pivot)&&(i<=right));
   do
   {
    j=j-1;
   }while((a[j]>pivot)&&(j>=0));
   if(i<j)
   {
    temp=a[i];
    a[i]=a[j];
    a[j]=temp;
   }
  }while(i<j);
  temp=a[left];
  a[left]=a[j];
  a[j]=temp;
  quicksort(left,j-1);
  quicksort(j+1,right);
 }
}
