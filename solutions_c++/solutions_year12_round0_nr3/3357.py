#include <stdio.h>
#include <stdlib.h>
#include <Windows.h>
#include <vector>
#include <math.h>

using namespace std;



int data[500];
int num_count;
int data_count;
int data_location[500];

void main()
{
	FILE*	file1 = fopen("C-small-attempt0.in","r");
	FILE*	file2 = fopen("out.txt","w+");

	char test[500];
	int ssang1[250];
	int ssang2[250];
	int tester[250];
	int tester2;
	int A=0;
	int B=0;
	int jari;
	int count=0;
	int op;

	int* sf = new int[2000000];
	int* sf2 = new int[2000000];
	int i=0;
	int j=0;
	int k=0;
	int l=0;
	int indi;




	fscanf(file1,"%d\n",&k);

	for(l=0; l<k;l++)
	{
		A=0;B=0;
		count=0;

		fgets(test,500,file1);

		for(i=0;i<500;i++)
		{
			if(test[i] ==' ') 
			{ jari =i;
				for(j=0;j<i;j++)
					{
						ssang1[j]=int(test[j])-48;
						A += ssang1[j]*pow(10.0,jari-j-1);
						ssang2[j]=int(test[i+j+1])-48;
						B += ssang2[j]*pow(10.0,jari-j-1);
					}	
			}
		}
			printf("%d %d \n", A,B);
			for(j=A;j<=B;j++)
			{
				sf[j]=j;
				sf2[j] =0;
			}

			for(j=A;j<=B;j++)
			{ op = j;
				 for(int p=0; p<250;p++)
				 {
					 tester[p] = 0;
				 }

				 for(int p=0; p<jari;p++)
				 {
					 tester[p] = op/pow(10.0,jari-p-1);
					 op -= tester[p]*pow(10.0,jari-p-1);
				 }

				 for(int p=0; p<jari;p++)
				 {
					tester2=0;
					for(int m = p; m<jari+p;m++)
						{
						 if(m>=jari) tester2 += tester[m-jari]*pow(10.0,jari+p-m-1);
						 else tester2 += tester[m]*pow(10.0,jari+p-m-1);					
						}//fprintf(file2,"%d ", tester2);
					/////////////////////tester2 까지는 잘 찾으니까 문제는 여기다 . 

					if(tester2!=j)
					{
						for(int y= A; y<=B;y++)
						{
							if(tester2 == y )
								count++;
							sf2[y]=1;
						}
						
					}

				 }
				 	
				 
			 }
			fprintf (file2,"Case #%d: %d\n",l+1,count/2);
	
		printf ("%d 개\n",count/2);
		count =0;
		
			//fprintf(file2,"Case #%d: %s",l+1,trans);
	}

		


	
}