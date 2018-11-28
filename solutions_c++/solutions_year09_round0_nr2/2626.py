#include<stdio.h>
#include<time.h>
     int mat[10000][2];   // this is the adjacency matrix
    int inputs[100][100][100];          // THIS STORES IN THE INPUT
     int sink[10000];   // this  is the list of  all the sinks
  void   getmin(int test,int i,int j,int *i_min,int *j_min,int r,int c)
  {
	  int min=inputs[test][i][j];
	* i_min=i;
	 * j_min=j;
	  if(i!=0)
       {	
	   // printf("Top open"); 
	     if(inputs[test][i-1][j] <min)
	     {
		  min=inputs[test][i-1][j];
		//  printf("Min%d: ",min);
		  *i_min=i-1;
	 	  *j_min= j;
	     }
       }
        if(j!= 0)
       {
	  //  printf("Left open");
	     if(inputs[test][i][j-1] <min)
	     {
		  min=inputs[test][i][ j-1];
		//  printf("Min%d: ",min);
		  *i_min=i;
		  *j_min=j-1;
	     }
       }
       if(j!=c-1)
       {
	  //  printf("Right Open");
	     if(inputs[test][i][j+1] < min)
	     {
		  min=inputs[test][i][j+1];
	//	  printf("Min%d: ",min);
		  *i_min=i;
		  *j_min=j+1;
	     }
       }
       if(i!=r-1)
       {
	  //  printf("Bottom Open");
	     if(inputs[test][i+1][j] <min)
	     {
		  min=inputs[test][i+1][j];
		 // printf("Min%d: ",min);
		  *i_min=i+1;
		  *j_min=j;
	     }
       }
       
      
  
  }
int  reachsink(int row)
  { 
       int dest=mat[row][0];
       if(sink[row]==1)      // it has reached a sink
	    return dest;
       else
	    reachsink(dest);
  }
  
  

    
int main()
{
     int times ,r[100],c[100] ,i_min,j_min;
     
    
   int k_min,set;
   int curr_dess,val;
   int label;
     int curr_val,min_val,flag;
     scanf("%d",&times);
     
     for(int i=0;i<times;i++)
     {
	  set=0;
	   scanf("%d %d",&r[i],&c[i]) ;
	    for(int j=0;j<r[i];j++)
	    {
		 for(int k=0;k<c[i];k++)
	 	 {
		      scanf("%d",&inputs[i][j][k]);          // storing values into the nxn  matrix 
			 //mat[j][k]=0;
		 }  
	     }
     }
     for(int i=0;i<times;i++)
     {
	     for(int j=0;j<10000;j++)
	     {
		  sink[j]=0;
		    mat[j][0]=-1;
		     mat[j][1]=-1;
	     }
  	    for(int j=0;j<r[i];j++)
	    {
		
		 for(int k=0;k<c[i];k++)
	 	  { 
		     // printf("Cell under consideration: %d\n", inputs[j][k]);
		      getmin(i,j,k,&j_min,&k_min,r[i],c[i]);
		     curr_val=j*c[i]+ k;
		     min_val=j_min*c[i]+k_min;
		  //   printf("%d goes to %d\n",curr_val,min_val);
		    mat[curr_val][0]=min_val;
		   // mat[curr_val][100]=min_val;
		    if(curr_val==min_val)
		    {
			// printf("Sink at cell %d",curr_val);
			 sink[curr_val]=1;
		    }
		 } 
	    }
	  
	     for(int j=0;j<r[i]*c[i];j++)
	    {
		
	      mat[j][0]= reachsink(j);
	      
	    //  printf("\nDestination of %d  set to %d" ,j, mat[j][100]);
	    }
	 
set=0;
	    for(int j=0;j<r[i]*c[i];j++)
	  {         
	       curr_dess=mat[j][0];
	       if(sink[curr_dess]!=1)           // i.e a lebel has   already been set for the sink 
	       {
		//    printf("Label found for dest sink %d: %d\n", curr_dess,sink[curr_dess]);
		    mat[j][1]=sink[curr_dess];
	       }
	       else
	       {
	       label=(int)( 'a'+ set);
	       set++;
		mat[j][1]=label;
		sink[curr_dess]=label;
	       }	
	       }	
     
	printf("Case #%d:",i+1)  ;
	for(int  j=0;j<(r[i]*c[i]);j++)
	{
	    if(j%c[i]==0){
		 printf("\n");
	    }
	     printf("%c ",(char)mat[j][1]);
	}
printf("\n");
     }   
       
	    return 0;
}