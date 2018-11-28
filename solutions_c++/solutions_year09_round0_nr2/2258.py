#include<stdio.h>
#include<stdlib.h>

int count;
int p;
int q;

int populate(int ** mat,char ** matc,int i,int j)
{
 int val;
if(matc[i][j]!=0)
{

return matc[i][j];
}
else
{
 //printf("Sgdfg");
 int min=mat[i][j];
 int flag=-1;

		
	if(i<p-1&&mat[i+1][j]<min)
	{flag=1;
	min=mat[i+1][j];
	}
        if(j<q-1&&mat[i][j+1]<=min)
	{flag=0;
	min=mat[i][j+1];
	}
        if(j>0&&mat[i][j-1]<=min)
	{flag=3;
	min=mat[i][j-1];
	}
        if(i>0&&mat[i-1][j]<=min)
	{flag=2;
	min=mat[i-1][j];
	}
	if(min==mat[i][j]||flag==-1)
	{
	
	val=matc[i][j]='a'+count;
	count++;
	
	}
	else if(flag==0)
	{
		 val=populate(mat,matc,i,j+1);
	}
	else if(flag==1)
	{
		 val=populate(mat,matc,i+1,j);
	}
	else if(flag==2)
	{
		val= populate(mat,matc,i-1,j);
	}
	else if(flag==3)
	{
		 val=populate(mat,matc,i,j-1);
	}		
      
 matc[i][j]=val;

return val;
}
 
}

int main()
{
int n;

int i;
int j;
int k;
int **mat=(int **)malloc(sizeof(int *)*102);
char **matc=(char **)malloc(sizeof(char *)*102);;


for(i=0;i<102;i++)
{
mat[i]=(int *)malloc(sizeof(int)*102);
matc[i]=(char *)malloc(sizeof(int)*102);
}
scanf("%d",&n);

for(k=0;k<n;k++)
{
scanf("%d%d",&p,&q);

//initialize
for(i=0;i<p;i++)
{

	for(j=0;j<q;j++)
	{
	matc[i][j]=0;
	}

}

for(i=0;i<p;i++)
{

	for(j=0;j<q;j++)
	{
	scanf("%d",&mat[i][j]);	
	}

}
count=0;
	
for(i=0;i<p;i++)
{

	for(j=0;j<q;j++)
	{
	populate(mat,matc,i,j);
	}

}
printf("Case #%d:\n",k+1);
for(i=0;i<p;i++)
{

	for(j=0;j<q;j++)
	{
	printf("%c ",matc[i][j]);	
	}
	printf("\n");
}
	




}


return 0;}
