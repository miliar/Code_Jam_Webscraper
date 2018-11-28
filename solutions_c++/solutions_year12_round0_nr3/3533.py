#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>
#include <math.h>

#include <iostream> 
#include <string> 
#include <sstream> 

int getNumDigits(int num);
void reverse(char* str);
void intToStr(char temp[],int num, int numDigits);
void rotateFirstDToLast(char temp[]);
int countFirstChar(char temp[]);
int isNumAlreadyPresent(int n, int m , int allNCases[], int allMCases[], int km);


char *InpFilename = "C:\\VINOD\\C-small-attempt1.in"; 
char *OutFilename = "C:\\VINOD\\C-small-1.txt"; 
#define LINE_MAX 100000

int main()
{
 FILE *fpr, *fpw; 
 fpr=fopen(InpFilename,"r");
 fpw=fopen(OutFilename,"w"); 
 
 int A = 0, B = 0, n = 0, m = 0, d = 0, countCase = 0;
 int i = 0, j = 0, k = 0, T = 0, it = 1;
 char temp[LINE_MAX];
 int allNCases[LINE_MAX], allMCases[LINE_MAX];
 fscanf(fpr,"%s", temp);
 T = atoi(temp);
 //printf("\nT: %d", T);
 while((fscanf(fpr,"%s", temp) == 1) && it <= T)
 {
     A = atoi(temp);
     fscanf(fpr,"%s", temp);
     B = atoi(temp);
     countCase = 0;
     k = 0;
     m = 0;
     n = 0;
     
     //printf("\nA: %d, B: %d", A, B);
     for(i = A; i <= B; i++)
     {
         n = i;
         d = getNumDigits(n);
         intToStr(temp, n, d);
         reverse(temp);
         
         if(countFirstChar(temp) != 1)
         {
             //printf("\n IntTemp: %s, n: %d, d: %d", temp, n, d);
             for(j = 0; j < d; j++)
             {
               //get each number by rotating 1st char to end
               rotateFirstDToLast(temp);
               m = atoi(temp);
               //A <= n < m <= B.
                   if( m > n && m <= B) 
                   {
                       if( !isNumAlreadyPresent(n, m , allNCases, allMCases, k))
                       {
                       countCase++; 
                       allMCases[k] = m; 
                       allNCases[k++] = n;
                      
                       }
                     
                    }//end of if loop
               }  // end of j<d for loop for each rotation  
           } // 
        
    } //end of for loop where i=A to i<B
   fprintf(fpw,"Case #%d: %d\n", it, countCase);
   it++;
   
   // printf("\n-----> count case: %d", countCase);
 } //end of while loop 

  
 
 fclose(fpr);
 fclose(fpw);

 //getchar();
 return 1;
    
}

int getNumDigits(int num)
{
  int count = 0;  
  while(num/10 > 0) 
  {
     num = num / 10;
     if(num > 0) count++;
  }   
  
  return count+1;
}

void reverse(char* str)
{
  char ch;   
  int n = strlen(str); 
  for(int i = 0; i< n/2 ; i++)
  {
     ch = str[i];
     str[i] = str[n-i-1];
     str[n-i-1] = ch;
  }      
  
}

void intToStr(char temp[],int num, int numDigits)
{
  int i = 0;      
  for(i = 0; i < numDigits; i++)
  {
       temp[i] = '0' + (num%10);
       num = num/10;
  }
  temp[i] = '\0';
}

void rotateFirstDToLast(char temp[])
{
  int i = 0;
  char ch = temp[0];
  for(i = 0; i < strlen(temp)-1; i++) temp[i] = temp[i+1];
  temp[i++] = ch;
  temp[i] = '\0';
  
}

int countFirstChar(char temp[])
{
     int cnt = 0;
     int i = 0;
     for(i=1; i < strlen(temp); i++)
     {
       if(temp[i] == temp[0]) { cnt++;  } // printf("\t MATCHED: temp[%d] = %c, 0: %c, cnt: %d", i, temp[i], temp[0], cnt);      }
       //else { printf("\t NM: temp[%d] = %c, 0: %c, cnt: %d", i, temp[i], temp[0], cnt); }
     }
    // printf("\ncnt: %d and strlenTemp-1: %d",cnt, (strlen(temp)-1));
      if(cnt == (strlen(temp)-1)) return 1;
      else return 0;
}


int isNumAlreadyPresent(int n, int m , int allNCases[], int allMCases[], int km)
{
    for(int i = 0; i < km ; i++)
    {
      if((allMCases[i] == n && allNCases[i] == m) || (allMCases[i] == m && allNCases[i] == n)) 
      {
         return 1;
      }
    }
    
    return 0;
}
