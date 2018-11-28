
#include "stdafx.h"
#include<stdlib.h>


int _tmain(int argc, _TCHAR* argv[])
{
	int n;
	FILE* file;
	FILE* file2;
	char* filename = "C:\\B.txt";
    char* filename2 = "C:\\B_final.txt";
	int turnaround_time;
	int fromA;
	int fromB;
	char departuretime[6],arrivetime[6];
	char *departure_time = departuretime,*arrive_time = arrivetime; 
	int tempdeptime, temparrtime;
	int NA[100][2],NB[100][2],NA2[100][2],NB2[100][2];
	int maxA, maxB;
	int subbufferA[100],subbufferB[100];
	int tableA[100],tableB[100];



	file2 = fopen( filename2, "w" );
    file = fopen( filename, "r" );

	if(!fscanf(file,"%d",&n))
	{
		     return -1;
	}
	for(int i=0;i<n;i++)
	{
	   if(!fscanf(file,"%d",&turnaround_time))
	   {	 
		   return -1;
	   }
	   fscanf(file,"%d %d",&fromA,&fromB);


        maxA = fromA;
		maxB = fromB;
	   for(int AB = 0; AB<fromA;AB++)
	   {
		   fscanf(file,"%s %s",departure_time,arrive_time);
           tempdeptime = (departuretime[0]-48)*1000+(departuretime[1]-48)*100+(departuretime[3]-48)*10+(departuretime[4]-48);

           temparrtime = (arrivetime[0]-48)*1000+(arrivetime[1]-48)*100+(arrivetime[3]-48)*10+(arrivetime[4]-48)+turnaround_time;
		   if((arrivetime[3]-48)*10+(arrivetime[4]-48)+turnaround_time>=60)
		   {
			  temparrtime = (arrivetime[0]-48)*1000+(arrivetime[1]-48+1)*100+(arrivetime[3]-48)*10+(arrivetime[4]-48)+turnaround_time-60;
		      if((arrivetime[0]-48)*10+(arrivetime[1]-48+1)==24)
              temparrtime = 24*100+(arrivetime[3]-48)*10+(arrivetime[4]-48)+turnaround_time-60;
		   }
           NA[AB][0] = tempdeptime;
		   NA2[AB][0] = tempdeptime;
           NA[AB][1] = temparrtime; 
           NA2[AB][1] = temparrtime;
	   }
	   for(int BA = 0; BA<fromB;BA++)
	   {
		   fscanf(file,"%s %s",departure_time,arrive_time);
           tempdeptime = (departuretime[0]-48)*1000+(departuretime[1]-48)*100+(departuretime[3]-48)*10+(departuretime[4]-48);
           temparrtime = (arrivetime[0]-48)*1000+(arrivetime[1]-48)*100+(arrivetime[3]-48)*10+(arrivetime[4]-48)+turnaround_time;
		   if((arrivetime[3]-48)*10+(arrivetime[4]-48)+turnaround_time>=60)
		   {
			   temparrtime = (arrivetime[0]-48)*1000+(arrivetime[1]-48+1)*100+(arrivetime[3]-48)*10+(arrivetime[4]-48)+turnaround_time-60;
		       if((arrivetime[0]-48)*10+(arrivetime[1]-48+1)==24)
               temparrtime = 24*100+(arrivetime[3]-48)*10+(arrivetime[4]-48)+turnaround_time-60;
		   }
		   NB[BA][0] = tempdeptime;
		   NB2[BA][0] = tempdeptime;
           NB[BA][1] = temparrtime;
		   NB2[BA][1] = temparrtime;
       }
	   bool exhangeflag = false;
	   int arrangebuffer;
	   for(int time = 0; time<fromA-1;time++ )  
	   {
		  exhangeflag = false;
		  for(int rangenum=0;rangenum<fromA-1-time; rangenum++)
	      {
              if(NA[rangenum][1]>NA[rangenum+1][1])  
		      {
			     arrangebuffer = NA[rangenum][1];
                 NA[rangenum][1] = NA[rangenum+1][1];
                 NA[rangenum+1][1] = arrangebuffer;
                 
			     arrangebuffer = NA[rangenum][0];
                 NA[rangenum][0] = NA[rangenum+1][0];
                 NA[rangenum+1][0] = arrangebuffer; 
			     exhangeflag = true;
              }
			  if(NA[rangenum][1]==NA[rangenum+1][1])
			  {
				  if(NA[rangenum][0]>NA[rangenum+1][0])
				  {
			         arrangebuffer = NA[rangenum][1];
                     NA[rangenum][1] = NA[rangenum+1][1];
                     NA[rangenum+1][1] = arrangebuffer;
                 
			         arrangebuffer = NA[rangenum][0];
                     NA[rangenum][0] = NA[rangenum+1][0];
                     NA[rangenum+1][0] = arrangebuffer; 
			         exhangeflag = true;

				  }

			  }

             
          }
		  if(exhangeflag == false)
			  break;
       }
	   for(int time = 0; time<fromA-1;time++ ) 
	   {
		  exhangeflag = false;
		  for(int rangenum=0;rangenum<fromA-1-time; rangenum++)
	      {
              if(NA2[rangenum][0]>NA2[rangenum+1][0])   
		      {
			     arrangebuffer = NA2[rangenum][0];
                 NA2[rangenum][0] = NA2[rangenum+1][0];
                 NA2[rangenum+1][0] = arrangebuffer;
                 
			     arrangebuffer = NA2[rangenum][1];
                 NA2[rangenum][1] = NA2[rangenum+1][1];
                 NA2[rangenum+1][1] = arrangebuffer; 
			     exhangeflag = true;
              } 
			  if(NA2[rangenum][0]==NA2[rangenum+1][0])
			  {
				  if(NA2[rangenum][1]>NA2[rangenum+1][1])
				  {
					  arrangebuffer = NA2[rangenum][0];
                      NA2[rangenum][0] = NA2[rangenum+1][0];
                      NA2[rangenum+1][0] = arrangebuffer;
                 
			          arrangebuffer = NA2[rangenum][1];
                      NA2[rangenum][1] = NA2[rangenum+1][1];
                      NA2[rangenum+1][1] = arrangebuffer; 
			          exhangeflag = true;

				  }

			  }
             
          }
		  if(exhangeflag == false)
			  break;
       }


	   for(int time = 0; time<fromB-1;time++ )  
	   {
		  exhangeflag = false;
		  for(int rangenum=0;rangenum<fromB-1-time; rangenum++)
	      {
              if(NB[rangenum][1]>NB[rangenum+1][1])   
		      {
			     arrangebuffer = NB[rangenum][1];
                 NB[rangenum][1] = NB[rangenum+1][1];
                 NB[rangenum+1][1] = arrangebuffer;
                 
			     arrangebuffer = NB[rangenum][0];
                 NB[rangenum][0] = NB[rangenum+1][0];
                 NB[rangenum+1][0] = arrangebuffer; 
			     exhangeflag = true;
              } 
			  if((NB[rangenum][1]==NB[rangenum+1][1]))
			  {
				  if(NB[rangenum][0]>NB[rangenum+1][0])
				  {
					  arrangebuffer = NB[rangenum][1];
                      NB[rangenum][1] = NB[rangenum+1][1];
                      NB[rangenum+1][1] = arrangebuffer;
                 
			          arrangebuffer = NB[rangenum][0];
                      NB[rangenum][0] = NB[rangenum+1][0];
                      NB[rangenum+1][0] = arrangebuffer; 
			          exhangeflag = true;

				  }
			  }
             
          }
		  if(exhangeflag == false)
			  break;
       }
	   for(int time = 0; time<fromB-1;time++ )  
	   {
		  exhangeflag = false;
		  for(int rangenum=0;rangenum<fromB-1-time; rangenum++)
	      {
              if(NB2[rangenum][0]>NB2[rangenum+1][0])  
		      {
			     arrangebuffer = NB2[rangenum][0];
                 NB2[rangenum][0] = NB2[rangenum+1][0];
                 NB2[rangenum+1][0] = arrangebuffer;
                 
			     arrangebuffer = NB2[rangenum][1];
                 NB2[rangenum][1] = NB2[rangenum+1][1];
                 NB2[rangenum+1][1] = arrangebuffer; 
			     exhangeflag = true;
              } 
			  if(NB2[rangenum][0]==NB2[rangenum+1][0])
			  {
				  if(NB2[rangenum][1]>NB2[rangenum+1][1])
				  {
   			          arrangebuffer = NB2[rangenum][0];
                      NB2[rangenum][0] = NB2[rangenum+1][0];
                      NB2[rangenum+1][0] = arrangebuffer;
                 
			           arrangebuffer = NB2[rangenum][1];
                       NB2[rangenum][1] = NB2[rangenum+1][1];
                       NB2[rangenum+1][1] = arrangebuffer; 
			           exhangeflag = true;
				  }

			  }
             
          }
		  if(exhangeflag == false)
			  break;
       }



	   for(int t = 0; t<fromB;t++)
	   {
		   subbufferA[t] = -1;
		   tableB[t] = 1;

	   }

	   for(int t = 0; t<fromA;t++)
	   {
		   subbufferB[t] = -1;
		   tableA[t] = 1;
	   }
	   int count = 0;
	   bool subflag = false;
	   bool cmpflag =false;
	   for(int time =0; time<fromA;time++)
	   {
		   subflag = false;
		   for(int time2 = 0; time2<fromB; time2++)
		   {
			   if(NA2[time][0]>NB[time2][1]||NA2[time][0]==NB[time2][1])
			   {
				   cmpflag =false;
				   for(int cmp = 0;cmp<count;cmp++)
				   {
					   
					   if(subbufferA[cmp] == time2)      //do not exsist
					   {
						   cmpflag =true;
						   break;
					   }
				   }
				   if(cmpflag ==true)
					   continue;
				   else
				   {
				     subbufferA[count] = time2;
				     count++;
				     subflag =true;
				     break;
				   }
			   }
		   }
		   if(subflag == true)
		   {
			   tableA[time] = 0;
		   }


	   }

	  count = 0;
	   for(int time = 0; time<fromB;time++)
	   {
		   subflag = false;
		   for(int time2 = 0; time2<fromA; time2++)
		   {
			   if(NB2[time][0]>NA[time2][1]||NB2[time][0]==NA[time2][1])
			   {
				   cmpflag =false;
				   for(int cmp = 0;cmp<count;cmp++)
				   {
					   if(time2 == subbufferB[cmp])
					   {
						   cmpflag =true;
						   break;
					   }
				   }
				   if(cmpflag ==true)
					   continue;
				   else
				   {
				     subbufferB[count]=time2;
				     count++;
				     subflag = true;
				     break;
				   }
			   
			   }
		   }
		   if(subflag == true)
		   {   
			   tableB[time] = 0;
		   }


	   }
	   int numA=0, numB=0;
	   for(int t =0;t<fromA;t++)
	   {
		   if(tableA[t]==1)
			   numA++;
	   }
	   for(int t =0;t<fromB;t++)
	   {
		   if(tableB[t]==1)
			   numB++;
	   }


       fprintf(file2,"Case #%d:",i+1);
       fprintf(file2," %d %d",numA,numB);
       fprintf(file2,"\n");

      

	}

	fclose(file);
	fclose(file2);
	return 0;
}

