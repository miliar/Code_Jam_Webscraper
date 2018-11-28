#include<stdio.h>
#include<math.h>
#include<stdlib.h>
#include<string.h>

int numdigits (int a)
{
if (a>=1000) return 4;
if (a>=100) return 3;
if (a>=10) return 2;
return 1;
}

int power(int a,int b)
{
int l,retval;
for(l=0,retval=1;l<b;l++)
retval = retval*a;
return retval;
}
void main()
{
int cases,index_cases,possible,count,N[4],M[4],mo,di;
int A,B, i,j,k,nb;
freopen("C-small-attempt0.in" , "rt" , stdin ) ;
freopen("C-small-attempt0.out" , "wt" , stdout ) ;
//freopen("C-large.in" , "rt" , stdin ) ;
//freopen("C-large.out" , "wt" , stdout ) ;

//for (i=1;i<4;i++)
//{
//	printf("%d,%d\n",i,power(10,i));
//}

cases = 0;
//read the number of test cases 
scanf("%d",&cases);
//printf("Cases = %d\n",cases);


//Loop through all the cases
for (index_cases=0 ; index_cases<cases; index_cases++)
{
	scanf("%d",&A);
	scanf("%d",&B);
//    printf("%d,%d\n",A,B);

	count=0;
	for (i=A;i<B;i++)
	{
		for (j=i+1;j<=B;j++)
		{

			nb=numdigits(j);
			for (k=0;k<nb;k++)
			{
				mo = power(10,(nb-k));
				di = mo/10;
				N[k]=(i%mo)/di;
				M[k]=(j%mo)/di;
			}

			if(nb==2)
			{
				if(	(N[0]==M[1])&&(N[1]==M[0]))
				count++;
			}
			else if (nb==3)
			{
			if(
				((N[0]==M[1])&&(N[1]==M[2])&&(N[2]==M[0]))||
				((N[0]==M[2])&&(N[1]==M[0])&&(N[2]==M[1]))
			   )
				count++;
			}
			else if (nb==4)
			{
				if(
				((N[0]==M[1])&&(N[1]==M[2])&&(N[2]==M[3])&&(N[3]==M[0]))||
				((N[0]==M[2])&&(N[1]==M[3])&&(N[2]==M[0])&&(N[3]==M[1]))||
				((N[0]==M[3])&&(N[1]==M[0])&&(N[2]==M[1])&&(N[3]==M[2]))
				   )
				count++;
			
			}
		}
	}

	printf("Case #%d: %d\n",index_cases+1,count);
}
fclose(stdin) ;
fclose(stdout) ;
}