#include <stdio.h>
#include <stdlib.h>
#include <stdio.h>

int N=0,T=0,NA=0,NB=0;
int i=1,j=1,Result[101][2];
int temp1,temp2;
int deptA[101],arrvA[101],deptB[101],arrvB[101];
    
int Calculate_Trains();

int main()
{
    
    scanf("%d",&N);// test Cases
    
    //read data 
    for(i=1;i<=N;i++)
    {
    
        scanf("%d",&T);// turn around time
        scanf("%d %d",&NA,&NB);
        
        for(j=1;j<=NA;j++)
        {
           scanf("%d:%d %d:%d",&deptA[j],&temp1,&arrvB[j],&temp2);
           deptA[j]=deptA[j]*60+temp1;
           arrvB[j]=arrvB[j]*60+temp2+T;             
        }
        for(j=1;j<=NB;j++)
        {
           scanf("%d:%d %d:%d",&deptB[j],&temp1,&arrvA[j],&temp2);
           deptB[j]=deptB[j]*60+temp1;
           arrvA[j]=arrvA[j]*60+temp2+T;
        }
        
        Result[i][0]=Calculate_Trains();
        Result[i][1]=temp1; // Assign second value to temp1
    }
    
    for(i=1;i<=N;i++)
    {
       printf("Case #%d: %d %d\n",i,Result[i][0],Result[i][1]);               
    }  
    system("pause");
    return 0;
}

int L[100],R[100];

void Merge(int A[],int p,int q,int r);

void Merge_Sort(int A[],int p, int r)
{
if(p<r)
  {
  int q=(p+r)/2;
  Merge_Sort(A,p,q);
  Merge_Sort(A,q+1,r);
  Merge(A,p,q,r);
  }
}


void Merge(int A[],int p,int q,int r)
{
int n1=q-p+1;
int n2=r-q;
int i,j,k;

for(i=0;i<n1;i++)
   L[i]=A[p+i];

for(j=0;j<n2;j++)
   R[j]=A[q+j+1];

i=j=0;

for(k=p;k<=r;k++)
   {
   if(L[i] <= R[j])
     {
     A[k]=L[i];
     i++;
     }
   else
     {
     A[k]=R[j];
     j++;
     }

     if(i==n1)
     {
     k++;
     for(;j<n2;j++)
	A[k++]=R[j];
     break;
     }
     if(j==n2)
     {
     k++;
     for(;i<n1;i++)
	A[k++]=L[i];
     break;
     }
   }

}

int Calculate_Trains()
{
 
    int trainsFromA=0,trainsFromB=0,i,j;
    int countA=0,countB=0;
    
     Merge_Sort(deptA,1,NA);
     Merge_Sort(arrvB,1,NA);
     Merge_Sort(deptB,1,NB);
     Merge_Sort(arrvA,1,NB); 
     
     i=j=1;
     // i -- A
     // j -- B
     
    while ( (i<=NA) && (j<=NB) )
    { 
             if( arrvA[j] <= deptA[i])
             {
                i++; 
                j++;          
             }
             else
             {
                 i++;
                 trainsFromA++;
             }
        
    }
    if( i <= NA)
      trainsFromA += NA - i +1;
    
    
    i=j=1;
    
    while ( (i<=NB) && (j<=NA) )
    { 
             if( arrvB[j] <= deptB[i])
             {
                i++; 
                j++;          
             }
             else
             {
                 i++;
                 trainsFromB++;
             }
        
    }
    if( i <= NB)
    trainsFromB += NB - i +1;
    
    temp1=trainsFromB;
    
    return trainsFromA; 
     
}
