#include <stdio.h>
#include <stdlib.h>


int main()
{
 FILE *input = fopen("input.txt","r");
 FILE *output = fopen("output.txt","w");
 
 unsigned int num_cases, num_googlers, num_surprises, lower_limit, total_score;
 unsigned int num_passed = 0 , val, remainder;
 
 fscanf(input,"%u\n",&num_cases);
 for( int i = 1; i <= num_cases; ++i )
  {
    num_passed = 0;
    fscanf(input,"%u %u %u",&num_googlers,&num_surprises,&lower_limit);    
    for( unsigned int j = 0; j < num_googlers; ++j )
     {
       fscanf(input,"%u",&total_score);
       val = total_score/3;
       remainder = total_score%3;
       if( (val + (remainder ? 1 : 0)) >= lower_limit ) { ++num_passed; continue; }
       if( (!num_surprises) || (remainder==1) ) { continue; }
       
       if( (remainder == 0) && (val) ) ++val;
       else if( remainder == 2 )val+=2;
       
       if( val >= lower_limit ) { ++num_passed; --num_surprises;  } 
     }
    fprintf(output,"Case #%u: %u\n",i,num_passed);
    
  }
 
 
 fclose(input);
 fclose(output);
}
