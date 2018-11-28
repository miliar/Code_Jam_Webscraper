// problem a.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdlib.h>
#include "string.h"


int _tmain(int argc, _TCHAR* argv[])
{
      int n;
	  FILE* file;
	  FILE* file2;
	  char* filename = "D:\\A.txt";
      char* filename2 = "D:\\A_final.txt";
	  char tempbuffer[100];
	  char *temp_buffer = tempbuffer;
	  int search_num,queries_num;
	  char searchbuffer[100][100];
	  char queriesbuffer[1000][100];            
	  char *search_buffer[100];              
	  char *queries_buffer[1000];
	  int searchbufferflag[100];
	  int count = 0;
	  int change = 0;
	  for(int t = 0; t<100; t++)                 
	  {
		  search_buffer[t] = searchbuffer[t];
		  searchbufferflag[t] = 0;
      }
	  for(int t =0; t<1000;t++)
     	  queries_buffer[t] = queriesbuffer[t];


     

	  file2 = fopen( filename2, "w" );
      file = fopen( filename, "r" );



	if(!fscanf(file,"%d",&n))
	{
		     return -1;
	}
    fgets(temp_buffer, 100, file);

	for(int i=0;i<n;i++)
	{
	    /*store the data*/
        fgets(temp_buffer, 100, file);
		search_num = atoi(temp_buffer);
		for(int s=0;s<search_num;s++) 
		{
			fgets(temp_buffer, 100, file);
			strcpy(search_buffer[s],temp_buffer);
        }
		fgets(temp_buffer, 100, file);
		queries_num = atoi(temp_buffer);
        
		for(int t = 0; t<100; t++)    
		{
           searchbufferflag[t] = 0;
		}
		count = 0;
		change = 0;
        for(int q = 0; q<queries_num; q++)   
		{
            fgets(temp_buffer, 100, file);
			strcpy(queries_buffer[q],temp_buffer);
			for(int s = 0; s<search_num;s++)  
			{
				if(strcmp(search_buffer[s],queries_buffer[q])==0)   // find the same
				{
					if(searchbufferflag[s]==0)
					{ 
						searchbufferflag[s] = 1;
						count++;

					}
					if(count == search_num)
					{
						for(int t = 0; t<100; t++)    // clear the flag 
		                {
                           searchbufferflag[t] = 0;
		                }
						count = 1;
						searchbufferflag[s] = 1;
						change++;
						break;
					}

				}
            }
		}

        fprintf(file2,"Case #%d:",i+1);

		fprintf(file2," %d",change);

        fprintf(file2,"\n");

        

	}

	return 0;
}

