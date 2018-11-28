#include <stdio.h>
#include <string.h>

#define  _RUN_FLAG_

#include<vector>

using namespace std;


 int printStr(char *p,int begin,int end)
 {
     int i = begin;
    
     for(;i<=end;i++)
     {
        printf(" %d",p[i]);
      }
     printf("\n"); 
}

int main()
{

  
 FILE *stream;

  FILE *out;
 
   
  char buf[1024];
  
  	  char result[1024];
  int   num  = 0;
  
    int N = 0;
	int tmp = 0;
  unsigned int K = 0;
   unsigned int t = 0;
  char p[50];
  char f[50];
  char *spa;
  int j = 1;
int i = 0;
    
  if ((stream=fopen("A-small-attempt0.in.txt", "rb+"))== NULL)
  {
	 printf("Cannot open output file.\n");
	 getchar();
	 return 1;
  }

  if ((out=fopen("out.txt", "w+"))== NULL)
	{
	   printf("Cannot open output file.\n");
	   getchar();
	   return 1;
	}
  

     if(freopen("test.txt",   "w",   stdout)==   NULL)
     fprintf(stderr,   "error   redirecting   stdout\n");  


  
  fgets(buf,1024,stream);
  num  = atoi(buf);
  printf("%d ",num);

   j = 1;
  while(fgets(buf,1024,stream))
  {
      spa = strchr(buf,' ');
      *spa = 0;
      N = atoi(buf);
      *spa = ' ';
      K = atoi((char*)(spa+1));
      
      printf("N:%d, K:%d,%s",N,K, buf);  
      
      memset(p,0,50);
      p [1] = 1;
      memset(f,0,50);
      
      t = 0;
      while(t < K)
      {
              i = 1;
			  while( (i<=N) && (p[i] == 1))
			  	{
			  	 if(f[i] ==1 )
				 	f[i] = 0;
				 else 
				 	f[i] = 1;
                  p[i]= 0;
				   i++;
			  	}
			  i = 1;
			  p[i] = 1;
			  
			   if(f[i] ==1)
			{
				
				tmp = i+1;
				p[tmp] = 1;
				
				while(tmp < N && f[tmp] == 1)
					{
                      tmp++;
					 p[tmp] = 1;
					
					};
			}
			 else 
			 	{
			 	
			 	}
			 //	printf("***t=%d*Power,Flag*\n",t);
			   // printStr(p,1,N);
		       //  printStr(f,1,N);
              t++;
              }

		 /**
   
   
		 Case #1: OFF
   Case #2: ON
   Case #3: OFF
   Case #4: ON
   **/
   //printf("\n\nresult\n");
   if(p[N] ==  1&&f[N] == 1)
	 {
			sprintf(result,"Case #%d: ON\n",j);
	   }
		 else 
		   {
			sprintf(result,"Case #%d: OFF\n",j);
	   }
	   printf(" %s ",result);
		   fputs(result,out);

   j++;

						   
   }
  
   fclose(stream);
 fclose(stdout);   
 getchar();
    

    
}
