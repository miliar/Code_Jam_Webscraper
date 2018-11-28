#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
using namespace std;
//int reduc[11][11];
/*int fac[11];
double ex[11];
double tmp;
bool tck[11];
int ans[11];*/
int n;
int t;
int cnt;
int A[1001];
int B[1001];
/*double t1,t2,t3;
double rat;
double val;*/
/*inline void gen(int a)
{
 if(a==n+1)
 {
  reduc[a-1][a-1-cnt]++;
  //if(n<=2){printf("%d %d true = %d\n",ans[1],ans[2],cnt);}
 }
 else
 {
  for(int i=1;i<=n;i++)
  {
   if(tck[i]==false)
   {
    tck[i]=true;
    ans[a]=i;
    if(a==i){cnt++;gen(a+1);cnt--;}
    else{gen(a+1);}
    tck[i]=false;
   }
  }
 }
}*/
main()
{
 freopen("D-large.in","r",stdin);
 freopen("D-large.out","w",stdout);
 /*ex[1]=0;
 ex[0]=0;
 fac[1]=1;
 for(int i=2;i<=10;i++)
 {
  n=i;
  gen(1);
  fac[i]=fac[i-1]*i;
  //printf("complete %d\n",i);
  t1=reduc[i][i];
  t2=fac[i];
  rat=t1/t2;
  for(int j=0;j<i;j++)
  {
   t1=ex[j];
   t1=t1+1;
   t2=fac[i];
   t3=t1/t2;
   t1=reduc[i][j];
   //printf("reduc %d %d = %d\n",i,j,reduc[i][j]);
   t3=t3*t1;
   ex[i]+=t3;
   val=ex[i];
   val=val+1;
   //printf("ex 2 = %lf\n",ex[i]);
  }
  rat=reduc[i][i]/t2;
     for(int k=1;k<=100;k++)
   {
    //if(k<=10){printf("+ %lf\n",val*rat);}
    ex[i]+=val*rat;
    val=val*rat;
   }
  //printf("ex %.10lf\n",ex[i]);
 }*/
 //observation here expected value of gorosort = miss places
 scanf("%d\n",&t);
 for(int i=1;i<=t;i++)
 {
  scanf("%d",&n);
  for(int j=1;j<=n;j++)
  {
   scanf("%d",&A[j]);
   B[j]=A[j];
  }
  sort(&B[1],&B[n+1]);
  cnt=0;
    for(int j=1;j<=n;j++)
  {
   if(A[j]==B[j]){cnt++;}
  }
  //printf("%d\n",n-cnt);
  printf("Case #%d: %d.000000\n",i,n-cnt);
 }
 //system("pause");
 return 0;
}
