#include <stdio.h>
#include <string.h>
#include <limits.h>
#define  _RUN_FLAG_

#include<vector>

using namespace std;


 const int MAXBUFSIZE = 9001;

 


 int printStr(int  *p,int begin,int end)
 {
     int i = begin;
    printf("**printStr*\n");
     for(;i<=end;i++)
     {
        printf(" %d",p[i]);
      }
     printf("***\n"); 
}


 int printChar(char  *p,int begin,int end)
 {
     int i = begin;
     printf("**printChar*\n");
     for(;i<=end;i++)
     {
        printf("=%d(%c)=",p[i],p[i]);
      }
     printf("***\n");  
}


int main()
{

  
 FILE *stream;

  FILE *out;
 
   
  char buf[MAXBUFSIZE];
  
  	  char result[1024];
  int   num  = 0;
  
    int N = 0;
	int tmp = 0;
  unsigned int K = 0;
  int R = 0;
  
   unsigned int t = 0;
  char p[50];
  char f[50];

  int group[1000] ;
  char *spa;
  char *tc;
  int j = 1;
int i = 0;
int index;
int g;

unsigned int sum = 0;
 unsigned int s = 0;

 int tmpN = 0;   
    
 // if ((stream=fopen("A-small-attempt0.in.txt", "rb+"))== NULL)
 
 // if ((stream=fopen("A-large.in.txt", "rb+"))== NULL) 
      if ((stream=fopen("C-small-attempt0.in.txt", "rb+"))== NULL) 
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
  

     if(freopen("log.txt",   "w",   stdout)==   NULL)
     fprintf(stderr,   "error   redirecting   stdout\n");  

  
  
  fgets(buf,MAXBUFSIZE,stream);
  num  = atoi(buf);
  printf("%d ",num);

   j = 1;
  while(fgets(buf,MAXBUFSIZE,stream))
  {
      spa = strchr(buf,' ');
      *spa = 0;
      R = atoi(buf);
     // *spa = ' ';
	tc = strchr((char*)(spa+1),' ');
	*tc = 0;
  	K = atoi((char*)(spa+1));
	
	//*tc=  ' ' ;
	N =  atoi((char*)(tc+1));
      
      printf("R:%d,K=%d, N:%d\n**",R,K,N);  


	  fgets(buf,MAXBUFSIZE,stream);
       
       
      printf("buf:%s",buf);
      //  printChar(buf,0,10);
	  index = 0;
	  i = 0;
	  while(buf[i] !=0 &&  buf[i] != '\n' )
	  	{
	  	    g = 0;
	  	   
	  	    while(buf[i] !=0 && buf[i] != '\n' && isdigit(buf[i]))
	  	    	{
	  	    	    g = g*10 +buf[i] -'0';
			        i++;	
	  	    	}
	  	    	if(g > 0)
                  {
                       group[index++] = g; 
                       }
	  	    	if( buf[i] ==0  || buf[i] == '\n')
	  	           	break;
	  	           	
		 while(buf[i] !=0 &&  buf[i] != '\n' && !isdigit(buf[i]))
			{
			i++;
			};
			if(buf[i] ==0 &&  buf[i] == '\n')
		    break;
			
	  	}
	  printf("Group:\n");
	  printStr(group,0,index-1);
	  if(index  != N)
	  	{
	  	   printf("****** ERROR index  != N *\n");
	  	}
      //memset(p,0,50);
      //p [1] = 1;
      //memset(f,0,50);

	  t = 0;
	  sum = 0;

index = 0;
tmpN = 0;
	  while(t < R)
	  	{
s = 0;
//index = 0;
tmpN = 0;
while((tmpN < N) &&(s + group[index]) <= K)
{
  s+= group[index];
  index= (index+1)%N;
  tmpN++;
}

sum += s;
printf("Round=%d,s=%u,sum=%u\n",t,s,sum);
		t++;
	  	}
      
      
      /**
      Case #1: 21
Case #2: 100
Case #3: 20

      **/
      
			sprintf(result,"Case #%d: %u\n",j,sum);
	    	   fputs(result,out);
		   
      j++;
   }


   

						   

  
   fclose(stream);
 fclose(stdout);   
 getchar();
    

    
}



