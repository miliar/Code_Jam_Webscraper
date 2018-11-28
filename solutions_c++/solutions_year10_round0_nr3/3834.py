#include<iostream>
#include<stdio.h>
#include<string.h>
#include<conio.h>
#include<process.h>
#include<stdlib.h>
using namespace std;

//#include "FileFunctions.h"

char* fnReadLine()
{

	
	return NULL;
}

int main(int* argc, char** argv)
{
	int LineNo=0, TestCases=0, Cnt=0, Tokens[3], Groups[10], R=0, k=0, N=0,flag=0;
	int Gi[10], left,Earnings=0,TE=0, chk=0;
	char line[128],*p;
	
//	int cur_char;

    FILE *out_file = fopen("output.txt", "w");
	if (out_file == NULL) {
				fprintf(stderr,"Can not open output file\n");
				exit (8);
			}

	FILE *file = fopen ( "C-small-attempt0.in", "r" );
	if ( file != NULL )
	{

		fgets ( line, sizeof(line), file);
		TestCases=atoi(line);

		//cout<<TestCases<<"testCases"<<endl;
		for(int i=0;i<TestCases;i++)
		{
			chk=R=k=N=Cnt=left=Earnings=TE=0;

			fgets ( line, sizeof(line), file );
			
			p = strtok (line," ");
			Cnt=0;

				while (p != NULL)
				{
					Tokens[Cnt++]=atoi(p);
					p = strtok (NULL, " ");

				}

				R=Tokens[0];
				k=Tokens[1];
				N=Tokens[2];

			fgets ( line, sizeof(line), file );

			p = strtok (line," ");
			Cnt=0;

				while (p != NULL)
				{
					Groups[Cnt++]=atoi(p);
					Gi[Cnt-1]=Groups[Cnt-1];
					p = strtok (NULL, " ");

				}
				
				for(int c=0;c<Cnt;c++)
					//cout<<Gi[c];
				

			Cnt=0; 
			//cout<<R<<k<<N<<endl;
			
			TE=0;
			for(int j=0;j<R;j++)
			{
				left=k;
				Earnings=0;
				
				chk=0;								
				while( Gi[Cnt] <= left )
				{
					if(chk++==N)
						break;
					
					left-=Gi[Cnt];
					Earnings+=Gi[Cnt];
					
					Cnt++;
					if(Cnt == N )
					{
						Cnt=0;
						
					}
					
					
					
				}

				TE+=Earnings;				
			}
			
			//cout<<"Case #"<<i+1<<": "<<TE<<"\n";
			fprintf(out_file, "Case #%d: %d\n",i+1,TE);

					
		}

		fclose ( file );
		fclose(out_file);
	}
	else
	{
		perror ( "input.txt cannot open" ); /* why didn't the file open? */
	}
	
	return 0;
}
