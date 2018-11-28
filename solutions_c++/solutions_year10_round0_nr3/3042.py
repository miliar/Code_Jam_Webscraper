#include<stdio.h>

void rotate(int a[],int n,int j);
main()
{
 FILE *fp,*of;
 char inp[32];
 int r,i,j,t,s,sum,k,n,a[100],cost=0;
 scanf("%s",inp);
 fp=fopen(inp,"r");
 of=fopen("test.out","w");
 fscanf(fp,"%d",&t);
 
 for(s=1;s<=t;s++)
 { 
                  
  fscanf(fp,"%d%d%d",&r,&k,&n);
  for(i=0;i<n;i++) fscanf(fp,"%d",&a[i]);
  cost=0;
  for(i=0;i<r;i++)
  {
   sum=0; j=0;
   while(sum<k && j<n) { sum+=a[j]; j+=1; }
   if(sum>k) { j-=1; sum-=a[j]; }
   cost+=sum;
   rotate(a,n,j);
  }
  fprintf(of,"Case #%d: %d\n",s,cost);
 }
 fclose(fp);
 fclose(of);
 return 0;
}

void rotate(int a[],int n,int j)
{
 int i,temp,k;
 for(k=0;k<j;k++)
 {
  temp=a[0];
  for(i=0;i<n-1;i++) a[i]=a[i+1];
  a[n-1]=temp;
 }
}
 
