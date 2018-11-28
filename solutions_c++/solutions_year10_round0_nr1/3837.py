#include<stdio.h>
#include<math.h>
#include<conio.h>

void exit(int);
main()
{
      int K,i;
      FILE* fp;
     fp =  fopen("jam.out" , "w");
      int time,N,check,cases;
      //printf("no.of cases");
      scanf("%d",&cases);
      for(i=1;i<=cases;i++)
      {
    //  printf("enter the number of snapper");
      scanf("%d",&N);
      
     // printf("enter the number of times snapped your fingers");
      scanf("%d",&K);
      time=int(pow(2,N));
      time=time-1;
     check=K%(time+1);
     
         if(check==time)
         {
             printf("Case #" );
             printf("%d: ",i);
             printf("ON\n");
             fprintf(fp ,"%s%d%s%s" ,"Case #" , i , ": " ,"ON\n" );
          }
          
           else
          { 
             printf("Case #");
             printf("%d: ",i);
             printf("OFF\n");
             fprintf(fp ,"%s%d%s%s" ,"Case #" , i , ": " ,"OFF\n" );
           }
           
}
        fclose(fp);
      getch();
}
