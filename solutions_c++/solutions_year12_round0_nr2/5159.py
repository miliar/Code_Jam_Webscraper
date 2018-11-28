#include <stdio.h>
#include <string.h>
#include <stdlib.h>


void sort(int arr[10],int num)
{
int i , j ,k,temp,min;
k =-1;
for(i =1; i <= num; i++)
	{
	min = arr[i];
	k =-1;
	for (j = i +1 ; j <= num; j ++)
		{
			if (min > arr[j])
			{
			min = arr[j];
			k = j;
			}
		}

		if (k !=-1)
		{
		temp= arr[i];
		arr[i] = arr[k];
		arr[k] = temp;
		}
	}
/*printf("Array : \n");
for(i= 1 ; i <= num ; i++)
	printf("%d  ",arr[i]);
	*/
}


int getmax(int num,int Sind)
{
int quo=0;
int rem =0;

if(num ==0)
return 0;

quo=num/3;
rem =num%3;


if( rem == 0)
	{
	if(Sind)
		return (quo+1);
	else return(quo);
	}
if( rem == 1)
	{
	if(Sind)
		return (quo+1);
	else return(quo+1);
	}
if( rem == 2)
	{
	if(Sind)
		return (quo+2);
	else return(quo +1);
	}

	return 1;}


int getnextNum(char stringA[],int *j)
{
int num =0;
num = atoi(&stringA[*j]);
while(1)
	{
	if( (stringA[*j]==' ') ||
		 (stringA[*j]=='\n')||
		 (stringA[*j]=='\0') )
		 {
		 (*j)++;
		 break;
		 }
	else
		{
		(*j)++;
		}
	}
return num;
}


int main()
{
int j,index ;
FILE *fo,*fi;
char strout[120];
char strinp[120];
char temp[120];
int noOfTest =0;
int i =0;
int count =0;
int max =0;
int N,S,P,arr[100],Sind,tempS;

fo = fopen("output.in","w");
fi = fopen("input.in","r");

strcpy(strinp, "");
fgets(strinp,100,fi);

noOfTest=atoi(&strinp[0]);

for( index =1; index <= noOfTest; index ++)
 {

	strcpy(strinp,"");
	fgets(strinp,120,fi);   /* no of windows */
	j =0;
	N = getnextNum(strinp,&j);
	S= getnextNum(strinp,&j);
	P = getnextNum(strinp,&j);


	for (i =1; i <= N ; i++ )
		{
		arr[i]= getnextNum(strinp,&j);
		}



	sort(arr,N);

	count =0;
	Sind =0;
	tempS = S;
	for(i =1 ; i <= N ; i++)
	{
		Sind =0;
		max =0;

		if(tempS >=1)
		{
		Sind = 1;
		tempS--;
		}

		max = getmax(arr[i],Sind);
			if(max >= P)
			{
			count++;
			}
			else
			{
				if(Sind == 1)
					{
					tempS++;
					}
			}

	}

  /*	printf("\nCount = %d\n", count); */

	strcpy(strout,"");
  /*	printf("%s\n",strinp);*/
	sprintf(strout,"Case #%d: %d\n",index,count);
  /*	printf("%s",strout);*/
	fputs(strout,fo);
 }
fclose(fi);
fclose(fo);
return 1;
}
