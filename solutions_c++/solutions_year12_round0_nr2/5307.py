#include <stdio.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <process.h> /* for system command */
#include <conio.h>  /* for clrscr */
#include <dos.h> /* for delay */
#include <math.h>

FILE *f1;            /****2****/
FILE *fr;
FILE *finp;

#define MaxVariable 300000//maximum length of a variable is 30 characters
#define BUFFER 200000//maximum line length is 200 characters per line
void getString(char *,int);//gets input into our buffer


int main(){
    int Input_Data[101][103];
    char Input[BUFFER];
    int count=0;
    int count_New =0;
    int j = 0;
    int i = 0;
    int Num_Test = 0;
    int index = 0;
    char delims[] = " ";//variables are separated by space character
    char delims_New[] = "\n";
    char *result = NULL;
    char **Variables_New=NULL;
    char *result_New = NULL;
    char **Variables=NULL;
    char **Test=NULL;
    int Magic_Num,Buffer,Magic_Total,Max_Addition,Total,Surprise_Allow;
    int Confirm = 0;
    int Surprise = 0;
    char *Temp;
    long lFileLen;
    char *cThisPtr;
    char *Num_Test_String;
    int *Endl_array;
    int Endl_index =0;
    int index_one = 0;
    int Length = 0;
    char *ptr;
    
    
    fr = fopen ("B-small-attempt4.in", "rt");
    finp = fopen ("Input.txt", "wt");
    //fscanf(fr,"%s ",Temp);
    fseek (fr, 0L, SEEK_END);
    lFileLen = ftell(fr);
    Temp = (char *)calloc(lFileLen + 1, sizeof(char));
    fseek(fr, 0L, SEEK_SET);
    fread(Temp, lFileLen, 1, fr);
    ptr = Temp;
               
    //Num_Test = atoi(Temp);
    //scanf("%d ",&Num_Test);
    //result_New = strtok( Temp, delims_new );//we divide our input string into pieces based on spaces
    
    //while( result_New != NULL ) 
    //{
    //     Variables_New=(char **)realloc(Variables_New,(count+1)*sizeof(char *));
    //     Variables_New[count]=(char *)malloc(MaxVariable*sizeof(char));
    //     Variables_New[count++]=result_New;
   //      result_New = strtok( NULL, delims_new );
  //   }
  
      result_New = strtok( ptr, delims_New );//we divide our input string into pieces based on spaces
   while( result_New != NULL ) {
         Variables_New=(char **)realloc(Variables_New,(count_New+1)*sizeof(char *));
         Variables_New[count_New]=(char *)malloc(MaxVariable*sizeof(char));
         Variables_New[count_New++]=result_New;
         result_New = strtok( NULL, delims_New );
    }
     
    Num_Test = atoi(Variables_New[0]);
     //Num_Test = 100;
     fprintf(finp,"%d\n",Num_Test);
     //result_New = strtok( NULL, delims_new );
     
    for(index = 0;index < Num_Test;index++)
    {
             // result_New = strtok( ptr, delims_new );
              //Length = Length + strlen(result_New) + 1;
    //Input = &result[index + 1];
              
    //printf("enter values:");
    //getString(Temp,lFileLen);//we input our string into buffer
    //printf("\nyou entered:%s\n",Input);
    //printf("splitting input\n");
    result = strtok( Variables_New[index+1], delims );//we divide our input string into pieces based on spaces
   while( result != NULL ) {
         Variables=(char **)realloc(Variables,(count+1)*sizeof(char *));
         Variables[count]=(char *)malloc(MaxVariable*sizeof(char));
         Variables[count++]=result;
         result = strtok( NULL, delims );
    }
     for (i=0;i<count;i++)
     {
         //printf("%d%s",atoi(Variables[i])," ");//we print our variable array
         Input_Data[index][i] = atoi(Variables[i]);
         fprintf(finp,"%d%s",Input_Data[index][i]," ");
     }
        fprintf(finp,"\n"); 
    count=0;
    result = NULL;
    Variables=NULL;
     }
     fclose(finp); 
     
     //for(i = 0;i<Num_Test;i++)
     //{
     //   for(j = 0;j<(Input_Data[i][0]+3);j++)
     //   {
     //    printf("%d%s",Input_Data[i][j]," ");
     //   }
     //   printf("\n");
     //}
     f1 = fopen ("out.txt", "wt");
     for(i = 0;i<Num_Test;i++)
     {
        Magic_Num = Input_Data[i][2];
        Buffer = 10-Magic_Num;
        Magic_Total = Magic_Num * 3;
        Max_Addition = Buffer * 3;
        
        for(j = 3;j<(Input_Data[i][0]+3);j++)
        {
           Total = Input_Data[i][j] - Magic_Total;
           if(Total >= 0)
           {
                    if(Max_Addition >= Total)
                    {
                                    Confirm = Confirm + 1;
                    }
           }
           else
           {
               Total = -Total;
               
               
               if(Total <= 2)
               {
                        if(Magic_Num > 0)
                        {
                                     Confirm = Confirm + 1;
                        }
               }
               else if(Total <= 4)
               {
                    if(Magic_Num > 1)
                    {
                                 Surprise = Surprise +1;
                    }
               }
           }
                    
        }
        if(Surprise > Input_Data[i][1])
        {
                  Surprise_Allow =  Input_Data[i][1];
        }
        else
        {
             Surprise_Allow = Surprise;
        }
        fprintf(f1,"%s%d%s%d\n","Case #",(i+1),": ",(Confirm + Surprise_Allow));
        Confirm = 0;
        Surprise = 0;
     }
     
    fclose (f1); 
    fclose(fr); 
    getchar();
    return 0;
}


void getString(char *string,int buffer){
    int i=0;
    //fgets ( string, buffer, stdin );
    for ( i = 0; i < buffer; i++ ){
        if ( string[i] == '\n' ){
            string[i] = '\0';
            break;
        }
    }
}
