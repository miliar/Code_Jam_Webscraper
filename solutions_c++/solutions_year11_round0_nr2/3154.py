#include<conio.h>
#include<stdio.h>
#include<string.h>
#include<iostream>
using namespace std;

int main()
{
FILE *file;
FILE *outfile;
file = fopen( "a-large.in", "r" );
outfile = fopen("f.out","w");
int testcases,count=0;
fscanf(file,"%d",&testcases);
while(count<testcases)
{ 	   int i,j,k;
	   int flag[2][2];
	   for(i=0;i<2;i++)
		   for(j=0;j<2;j++)
	          flag[i][j]=-1;
	   i=0;j=0;
	   char replace[2],cancel[2],replaceby,sequence[10],newsequence[10];
	   fscanf(file,"%d",&i);
	   for(int counter=0;counter<i;counter++)
	   { replace[0] = getc(file);
	     if(replace[0] == ' ')
		 {   counter--;
		     continue;
		 }
		 replace[1] = getc(file);
		 replaceby = getc(file);
		 }
	   fscanf(file,"%d",&j);
	   for(int counter=0;counter<j;counter++)
	   { cancel[0] = getc(file);
   	     if(cancel[0] == ' ')
		 {   counter--;
		     continue;
		 }
		 cancel[1] = getc(file);
	     }
	   fscanf(file,"%d",&k);
	   int as=0;
	   for(int counter=0;counter<k;counter++,as++)
	   { sequence[counter] = getc(file);
	     if(sequence[counter] == ' ')
		 {   counter--;
		     continue;
		 }
	     newsequence[as] = sequence[counter];
	   	if( i == 1 )
	{ 
      if( newsequence[as]==replace[1])
		      {   
				  if(flag[1][0] == -1)
					  {flag[1][0] = as;
				       flag[1][1] = 1;
				      }
				  else if( (flag[1][1] == 0 || replace[1] == replace[0] ) && flag[1][0]==as-1 )
				  {      if(flag[0][0]== as-1)
						{
						flag[0][0]= -1;
						flag[0][1]= -1;
						}
						newsequence[--as] = replaceby;
						flag[1][1]=-1;
						flag[1][0]=-1;
						

				  }
				else if(flag[1][1] == 1)
				{      flag[1][0] = as;
				       flag[1][1] = 1;

				}
		      }
	  else if(newsequence[as]==replace[0])
			 {	if(flag[1][0] == -1)
					  {	flag[1][0] = as;
						flag[1][1] = 0;
	                  }
			 else if( flag[1][1] == 1 && flag[1][0]==as-1 )
				  {     
	                     if(flag[0][0]== as-1)
						{flag[0][0]= -1;
						flag[0][1]= -1;
						}
						newsequence[--as] = replaceby;
						flag[1][1]=-1;
						flag[1][0]=-1;
				  }
				else if(flag[1][1] == 0 )
				{      flag[1][0] = as;
				       flag[1][1] = 0;
				} 

			 }
	  if(flag[1][0] == as-1)
	  {
	     flag[1][1]=-1;
		 flag[1][0]=-1;
	  }
	   }
	if( j == 1 )
	   {
	   if(newsequence[as]==cancel[1])
		{ 
				  if(flag[0][0] == -1)
		          {    flag[0][0] = as;
		               flag[0][1] = 1; }
				  else if( flag[0][1] == 0 || (cancel[0]==cancel[1]))
				  {     while(as>0)
						{ as--;
						}
						flag[0][0]=-1;
						flag[0][1]=-1;
						flag[1][1]=-1;
						flag[1][0]=-1;
				  }
	              
	   }
	   else if(newsequence[as]==cancel[0])
		      {   
				  if(flag[0][0] == -1)
	               { flag[0][0] = as;
		             flag[0][1] = 0;
		           }
				  else if( flag[0][1] == 1 )
				  {  
				        while(as>0)
						{ as--;
						}
						
						flag[0][0]=-1;
						flag[0][1]=-1;
						flag[1][1]=-1;
						flag[1][0]=-1;
				  }

	              
	          }
	  }

	  
	  }
	fprintf(outfile,"Case #%d: [",count+1);
	 for(int t=1;t<as;t++)
	   {   if(t==1)
	       {
           fprintf(outfile,"%c",newsequence[1]);
		   continue;
	       }
		   fprintf(outfile,", %c",newsequence[t]);
	   }
   fprintf(outfile,"]\n");

        count++;
}
return 0;
}
