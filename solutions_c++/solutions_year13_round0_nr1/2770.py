#include <stdio.h>
#include <malloc.h>
#include <string.h>


int main()
{

// get the number of test cases
unsigned int testcase = 0;

//static const char filename[] = "A-small-practice.in";
static const char filename[] = "A-large.in";
//A-large-practice.in
//static const char filename[] = "A-large-practice.in";

FILE *file = fopen ( filename, "rt" );

static const char filename1[] = "Out.txt";
FILE *file1 = fopen ( filename1, "wt" );

//static const char filename2[] = "In1.txt";
//FILE *file2 = fopen ( filename2, "wt" );

//static const char filename3[] = "In2.txt";
//FILE *file3 = fopen ( filename3, "wt" );


unsigned int counter =0;
printf("karthikeyan: file=%x\n", file);
// get the number of elements
unsigned int n=0, count =0;
int result = 0;

char v1[16];
int v2[16];
char line[10];
char out[100];
int i=0 , j=0, xwin=0, owin=0;

//             scanf("%d", &j);             
             
int board_complete = 1;

if (file)
{
             // test case
             fgets(line, 10, file);
          	 sscanf (line, "%u", &testcase);
             printf("karthikeyan: size of testcase =%d\n", testcase);
             //scanf("%d", &j);             
             memset(line, '0', 10);
             
             for(counter=1; counter<=testcase; counter++)
             {
                  board_complete = 1;
                  memset(line, '0', 10);                        
                  //get tic
                  for(i=0; i<16;)
                  {
                        fgets(line, 10, file);
        	            strncpy(v1+i, line, 4);
                        printf("%c %c %c %c \n", v1[i],v1[i+1],v1[i+2],v1[i+3]);
                        i= i+4;
                        memset(line, '0', 4);
                  }
                  //scanf("%d", &j);             
                  // convert to numbers
                  for(i=0; i<16;i++)
                  {
                           if(v1[i]=='X')
                           {
                              v2[i] = 1;
                           }
                           else if (v1[i]== 'O')
                           {
                               v2[i] = -1; 
                           }
                           else if (v1[i] == 'T')
                           {
                                v2[i] = 100;
                           }
                           else if (v1[i] == '.')
                           {
                                v2[i] = 0;
                                board_complete = 0;
                           }
                  }

                  for(i=0; i<16;)
                  {
                        printf("%d %d %d %d \n", v2[i],v2[i+1],v2[i+2],v2[i+3]);
                        i= i+4;
                  }
                  //scanf("%d", &j);             
                    // algorithm
                    // check rowise
                    result = 0;
                    xwin = 0;
                    owin = 0;
                    i=0;
                  for(count=0; count<4;count++)
                  {
                  
        	            result = v2[i] + v2[i+1] + v2[i+2] + v2[i+3];
                        if((result == -4) || (result == 97))
                        {
                            printf("R: O win\n");
                            owin = true;
                            break;
                        } 
                        else if ((result == 4) || (result == 103))
                        {
                            printf("R: X win\n");
                            xwin = true;
                            break;
                        }
                        i= i+4;
                        printf("R: result=%d\n", result);
                  }


                  if(xwin || owin)
                  {
                      printf("R: winner written\n");
                      sprintf(out,"Case #%u: %s\n",counter,xwin?"X won":"O won");
                      fputs(out, file1);
                      fgets(line, 10, file);
                      continue;
                  }
                  //scanf("%d", &j);             
                  // check column wise
                   i=0;
                   result = 0;
                  for(count=0; count<4;count++)
                  {
                  
        	            result = v2[i] + v2[i+4] + v2[i+8] + v2[i+12];
                        if((result == -4) || (result == 97))
                        {
                            printf("C: O win\n");
                            owin = true;
                            break;
                        } 
                        else if ((result == 4) || (result == 103))
                        {
                            printf("C: X win\n");
                            xwin = true;
                            break;
                        }
                        i++;
                                                printf("C: result=%d\n", result);
                  }

                  if(xwin || owin)
                  {   printf("C: winner written\n");
                      sprintf(out,"Case #%u: %s\n",counter,xwin?"X won":"O won");
                      fputs(out, file1);
                      fgets(line, 10, file);
                      continue;
                  }
                               //scanf("%d", &j);             
                  // check diagnoal 1
                  i=0;
                  result = 0;

     	            result = v2[0] + v2[5] + v2[10] + v2[15];
                    if((result == -4) || (result == 97))
                        {
                            owin = true;
                        } 
                        else if ((result == 4) || (result == 103))
                        {
                            xwin = true;
                        }

                  if(xwin || owin)
                  {
                                                printf("D1: winner written\n");
                      sprintf(out,"Case #%u: %s\n",counter,xwin?"X won":"O won");
                      fputs(out, file1);
                      fgets(line, 10, file);
                      continue;
                  }

                  // check diagnoal 2
                  i=0;
                  result = 0;

     	            result = v2[3] + v2[6] + v2[9] + v2[12];
                    if((result == -4) || (result == 97))
                        {
                            owin = true;
                        } 
                        else if ((result == 4) || (result == 103))
                        {
                            xwin = true;
                        }


                  if(xwin || owin)
                  {
                                                printf("D2: winner written\n");
                      sprintf(out,"Case #%u: %s\n",counter,xwin?"X won":"O won");
                      fputs(out, file1);
                  }
                  else if(board_complete)
                  {
                                                                       printf("D2: drw\n");
                      sprintf(out,"Case #%u: %s\n",counter,"Draw");
                      fputs(out, file1);
                  }
                  else
                  {
                                                                                             printf("D2: not complete\n");
                      sprintf(out,"Case #%u: %s\n",counter,"Game has not completed");
                      fputs(out, file1);
                  }
             fgets(line, 10, file);
//scanf("%d", &j);
             
 } // for loop

}

fclose(file);
fclose(file1);
//fclose(file2);
//fclose(file3);

//scanf("%d", &j);

}
