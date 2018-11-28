#include <stdio.h>
#include <stdlib.h>

char map[] = "yhesocvxduiglbkrztnwjpfmaq";

int main()
{
 
 unsigned int num_cases = 0;
 FILE *input = fopen("input.txt","r");
 FILE *output = fopen("output.txt","w");
 
 fscanf(input,"%u\n",&num_cases);
 unsigned int curr_case = 1;
 char c;
 fprintf(output,"Case #%u: ",curr_case);
 while( curr_case <= num_cases )
 {
  if( (c=fgetc(input)) == '\n' ) 
   {
    if( curr_case == num_cases ) break;
    fprintf(output,"\nCase #%u: ",++curr_case);
   }
  else if( c == 32 ) fputc(' ',output);
  else fputc(map[(c-97)],output);
 }
 
 
 fclose(input);
 fclose(output);
 printf("\n\n");
 system("pause");
}
