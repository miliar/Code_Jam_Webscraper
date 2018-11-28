// p1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include<stdlib.h>
#include<stdio.h>
#include<ctype.h>

int _tmain(int argc, _TCHAR* argv[])
{
	int N,S,P,T;
	//char strInp[1000],strn[10];
	//char googlers[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	int numbers[1000],A[1000],B[1000],C[1000],A2[1000],B2[1000],C2[1000];

	FILE * pFile;
	FILE * pOut;

	pFile = fopen ("C:\\Output\\p2s.in","r");
	pOut = fopen ("C:\\Output\\p2sOut.out","w");

	if (pFile == NULL) perror ("Error opening file");
   else {


	//( fgets (mystring , 100 , pFile) != NULL )
	fscanf(pFile, "%d",&T);

	

	for(int i=0;i<T;i++){

		fscanf(pFile, "%d",&N);
		fscanf(pFile, "%d",&S);
		fscanf(pFile, "%d",&P);

		fprintf(pOut,"Case #%d: ",i+1);

		for(int j=0;j<N;j++)
		{
				
			fscanf(pFile, "%d",&numbers[j]);		
		
		}



		//fprintf(pOut,"\n");

		for(int k=0;k<N;k++)
		{
			if(numbers[k]==0)
			{
				A[k]=0;
					B[k]=0;
					C[k]=0;

					A2[k]=0;
					B2[k]=0;
					C2[k]=0;
			}
			else if(numbers[k]==1)
			{

				A[k]=0;
					B[k]=0;
					C[k]=1;

					A2[k]=0;
					B2[k]=0;
					C2[k]=0;
			}
			else
			{
				if(numbers[k]%3==0)
				{
					A[k]=numbers[k]/3;
					B[k]=numbers[k]/3;
					C[k]=numbers[k]/3;

					A2[k]=(numbers[k]/3)-1;
					B2[k]=(numbers[k]/3);
					C2[k]=(numbers[k]/3)+1;
				}
				else if(numbers[k]%3==1)
				{
					A[k]=numbers[k]/3;
					B[k]=numbers[k]/3;
					C[k]=(numbers[k]/3)+1;

					A2[k]=(numbers[k]/3)-1;
					B2[k]=(numbers[k]/3)+1;
					C2[k]=(numbers[k]/3)+1;
				}
				else if(numbers[k]%3==2)
				{
					A[k]=numbers[k]/3;
					B[k]=(numbers[k]/3)+1;
					C[k]=(numbers[k]/3)+1;

					A2[k]=(numbers[k]/3);
					B2[k]=(numbers[k]/3);
					C2[k]=(numbers[k]/3)+2;
				}

			}
		}

		int count=0;
		int limit=S;
		for(int l=0;l<N;l++)
		{
			if(C[l]>=P && C2[l]>=P)
			{
				count++;
			}
			else if(C[l]<P && C2[l]>=P && limit>0)
			{
				count++;
				limit--;
			}
			/*else if(C[l]>=P && C2[l]>=P && limit>0)
			{
				count++;
			}*/
			else
			{

			}
		}
		fprintf(pOut,"%d\n",count);
      
    
   }

	
	 fclose (pFile);
	 fclose (pOut);
	}
	return 0;
}

