#include<stdio.h>
#include<string.h>

FILE *fp,*fpout;

int freq[100000];


//------------
int L[100000],R[100000];
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
//-------------
int main()
{
int t,i,count,crt_testcase,j;

int P,K,L;

int secount=0,se_index,max_se,cnt_checked,no_of_switch=0;

//clrscr();

if ((fp = fopen("d:\\san\\etc\\codejam\\3_1C\\input.txt", "rt"))
    == NULL)
{
   fprintf(stderr, "Cannot open input file.\n");
   getc(stdin);
   return 0;
}

if ((fpout = fopen("d:\\san\\etc\\codejam\\3_1C\\output.txt", "wt"))
    == NULL)
{
   fprintf(stderr, "Cannot open input file.\n");
      getc(stdin);
   return 0;
}

fscanf(fp,"%d",&t);
printf("Test cases %d",t);

crt_testcase=0;
while(crt_testcase++<t)
{
    fprintf(fpout,"Case #%d: ",crt_testcase);
    
    //----------------------------
    fscanf(fp,"%d %d %d\n",&P,&K,&L);
    printf("\nP K L = %d %d %d\n",P,K,L);

/*
    if(P*K<L)
    {
         fprintf(fpout,"Impossible\n");
         printf("Impossible");
         continue;
             
    }
    */
    
    count=0;

    for(i=0;i<L;i++)
    {
    fscanf(fp,"%d",&freq[i]);
    //printf("%d ",freq[i]);
    }

    Merge_Sort(freq,0,L-1);
    printf("\n");
    for(i=0,j=L-1;i<L;i++,j--)
    {

     count = count + ((i/K) + 1)*freq[j];
     //printf("\n%d %d %d",((i/K) + 1),freq[j], count);
    }

    fscanf(fp,"\n");

    printf("\nkey pressed %d",count);

    fprintf(fpout,"%d\n",count);

}
 getc(stdin);
}
