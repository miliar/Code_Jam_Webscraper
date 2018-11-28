#include <stdio.h>
#include <stdlib.h>
#include <iostream>

using namespace std;

int main()
{
  char foo[] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};
//char foo[] = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};
  int testcases;
  char temp;
  FILE *f = fopen("input", "r");
  
  fscanf(f, "%d\n", &testcases);
  for(int i = 0; i < testcases; i++)
  {
    printf("Case #%d: ", i+1);
    fscanf(f, "%c", &temp);
    while(!feof(f) && (temp != '\n'))
    {
      if(temp == ' ') printf(" ");
      else printf("%c", foo[temp-97]);
      fscanf(f, "%c", &temp);
    }
    printf("\n");
  }
  
  return 0;
}
