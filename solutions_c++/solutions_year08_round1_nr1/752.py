#include<stdio.h>
#include<stdlib.h>
int A[1000],B[1000];

int compare(const void *A, const void *B)
{   int p = *(int*)A;
    int q = *(int*)B;
    return p-q;
}
int compare2(const void *A, const void *B)
{   int p = *(int*)A;
    int q = *(int*)B;
    return q-p;
}
int main ()
{  int n,i,j,k,z,temp;
   scanf("%d",&n);
   for(i=1;i<=n;i++)
   {   scanf ("%d",&z);
       for(j=0;j<z;j++)
       {   scanf("%d",&A[j]);
       }
        for(j=0;j<z;j++)
       {   scanf("%d",&B[j]);
       }
       qsort(A,z,sizeof(int),compare);
       qsort(B,z,sizeof(int),compare2);
       temp=0;
        for(j=0;j<z;j++)
       {   temp+=A[j]*B[j];
       }
       printf ("Case #%d: %d\n",i,temp);
      
   }
  
  return 0;
}
