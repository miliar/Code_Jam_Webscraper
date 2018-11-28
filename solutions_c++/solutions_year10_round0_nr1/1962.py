#include <stdio.h>


int main(int argc, char *argv[]) 
{
  FILE *input;
  
  input = fopen(argv[1], "ra");
  
  int lines;
  fscanf(input, "%d\n", &lines);
  for(int i=0;i<lines;i++) {
    int radix, count;
    fscanf(input, "%d %d\n", &radix, &count);
    bool on = ((~0) << (radix) | count) == ~0;
    printf("Case #%d: %s\n", i+1, on ? "ON" : "OFF");
  }
}
