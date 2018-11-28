// round11.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include<stdlib.h>


int _tmain(int argc, _TCHAR* argv[])
{
	int n;
	FILE* file;
	FILE* file2;
	char* filename = "D:\\A.txt";
    char* filename2 = "D:\\A_final.txt";
    /* bianliang */
	  //char tempbuffer[100];           //  need read space
	  //char *temp_buffer = tempbuffer; //  need read space
    int letternum;
    int keynum;
	int maxletternum;
	int letterbuf[1000];
	int resultbuf[1000][100];

    file = fopen( filename, "r" );
    file2 = fopen( filename2, "w" );

    if(!fscanf(file,"%d",&n))
	{
		return -1;
	}

	//fgets(temp_buffer, 100, file);  //need read space
	for(int i=0;i<n;i++)
	{ 



        fscanf(file,"%d %d %d",&maxletternum,&keynum,&letternum);
		for(int time = 0; time<letternum;time++)
            fscanf(file,"%d",&letterbuf[time]);
        
	   bool exhangeflag = false;
	   int arrangebuffer;
	   for(int time = 0; time<letternum-1;time++ )  // arrange NA
	   {
		  exhangeflag = false;
		  for(int rangenum=0;rangenum<letternum-1-time; rangenum++)
	      {
              if(letterbuf[rangenum]<letterbuf[rangenum+1])  // arrange by arrive time 
		      {
			     arrangebuffer = letterbuf[rangenum];
                 letterbuf[rangenum] = letterbuf[rangenum+1];
                 letterbuf[rangenum+1] = arrangebuffer;

			     exhangeflag = true;
              }             
          }
		  if(exhangeflag == false)
			  break;
       }
	   int result = 0;
	   int currentkey = 1;
	   int currentposition = 1;

	   for(int time = 0; time<letternum; time++)
	   {
             resultbuf[currentkey][currentposition] = letterbuf[time];
			 result += currentposition*letterbuf[time];
			 currentkey++;
			 if(currentkey>keynum)
			 {   currentkey=1;
				 currentposition++;
			 }
	   }







	  
	   fprintf(file2,"Case #%d: ",i+1);
       fprintf(file2,"%d",result);
       fprintf(file2,"\n");
	}

	fclose(file);
	fclose(file2);
	return 0;
}

