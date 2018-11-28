#include <stdio.h>
#include <stdlib.h>

unsigned int pow( unsigned int x , unsigned int n )
{  
 if( n == 0 ) return 1;
 if( n == 1 ) return x;
 unsigned int temp;
 bool isOdd = (n&1);
 if( isOdd ) --n; 
 temp =  pow( x, n>>1 );
 temp *= temp;
 if( isOdd ) temp *= x;
 return temp;  
}


int array[288];
unsigned int size = 0;

void SelectionSort( int array[], unsigned int size )
{
  for( unsigned int i = 0; i < (size-1); ++i )
   {
    unsigned int largest_index = i;
    for( unsigned int j = i+1; j < size; ++j )
      {
        if( array[j] > array[largest_index] ) largest_index = j;
      }
    unsigned int temp = array[i];
    array[i] = array[largest_index];
    array[largest_index] = temp;
   }
}

int BinarySearch( int array[], int size, int key )
{
  int high = size-1;
  int low = 0;
  while( low <= high )
  {
    int index = (high+low)/2;
    if( array[index] == key ) return index;
    if( array[index] > key  ) low = index+1;
    else high = index-1;
  }
  return -1;
}

int main()
{
   unsigned int A, B, n, m;
   unsigned int num_cases;
   unsigned int num_length = 0;
   unsigned int multiplier,divider;
   unsigned int num_pairs = 0;
   
   FILE *input = fopen("input.txt","r");
   FILE *output = fopen("output.txt","w");
   
   
   fscanf(input,"%u\n",&num_cases);
   
   for( unsigned int i = 1; i <= num_cases; ++i )
    {
      
      fscanf(input,"%u %u\n",&A,&B);
      n = A;
      num_pairs = 0;
      num_length = 0;
      while( A ) { ++num_length; A/=10; }
      
      
      while( n < B )
      {
          bool first = true;
          divider = 10;
          multiplier = pow(10,num_length-1);
          for( unsigned int k = 0; k < (num_length-1); ++k )
          {
            m = n%divider;
            m = (m*multiplier) + (n/divider);
            multiplier /= 10;
            divider *= 10;
            if( (m > n) && (m <= B) ) ++num_pairs;
          }
          ++n;
      }
      
      fprintf(output,"Case #%u: %u\n",i,num_pairs);
      
    }
   
   fclose(input);
   fclose(output);
}
