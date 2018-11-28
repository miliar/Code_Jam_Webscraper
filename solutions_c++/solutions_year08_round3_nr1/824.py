/* USE OF FREOPEN() */
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<dos.h>
#include<mem.h>
#include<ctype.h>
#include<alloc.h>
#include<math.h>
//using namespace std;
typedef long long int64;
#define For(i,l,u) for (int i(l),_u(u); i <= _u; ++i)
#define Ford(i,u,l) for (int i(u),_l(l); i >= _l; --i)
#define Rep(i,n) for (int i(0),_n(n); i < _n; ++i)
#define Repd(i,n) for (int i((n)-1); i >= 0; --i)
#define Fill(strarray,c) memset(strarray, c, strlen(strarray))
template<class T>
void bubblesort(T a[],T begin, T end)
//sorts in descending order
//call as bubblesort(a,0,4) To sort array like a[]={4,1,2,0,3}
{
 for(int i=begin;i<end;i++)
  for(int j=end;i<j;j--)
   if(a[j]>a[j-1])
   {
    swap(a[j],a[j-1]);
   }
}
template<class X>
void swap(X &a,X &b)
//this is a fn call by reference
// call as swap(i,j)
{
 X temp = a;
 a=b;
 b=temp;
}
int main()
{
 long int nocase=0,caseread=0,k=0,kread=0,l=0,lread=0,freq[1001],p,pread=0,maxpress=0;
 char *ifilename="c:\\input.in",*ofilename="c:\\output.in";
/* printf("enter the input filename along with path ad extension\n");
 scanf("%s",ifilename);
 printf("enter the output filename along with path ad extension\n");
 scanf("%s",ofilename);     */
 freopen(ifilename,"r", stdin);
 freopen(ofilename, "w", stdout);
 scanf("%ld",&nocase);
 caseread=0;
 while(caseread<nocase)
 {
  scanf("%ld%ld%ld",&p,&k,&l);
  lread=0;
  maxpress=0;
  while(lread<l)
  {
   scanf("%ld",&freq[lread++]);
  }
   bubblesort(freq,0L,lread-1);
   /*printf("\n%ld%ld%ld\n",p,k,l);
   for(int i=0;i<lread;i++)
    printf("%ld ",freq[i]);
    printf("\n");*/
   lread=0;
  //while(lread<l)
  //{
   pread=0;
   while(pread<p)
   {
    kread=0;
    while(kread<k)
    {
     if(lread<l)
     maxpress+=freq[lread++]*(pread+1);
     //printf("%d ",lread);
    kread++;
    }
   pread++;
   }
   //lread++;
  //}
  if(lread==l)
   printf("Case #%ld: %ld\n",caseread+1,maxpress);
  else
   printf("Case #%ld: %dIMPOSSIBLE\n",caseread+1,maxpress);
  caseread++;
 }
 return 1;
}

