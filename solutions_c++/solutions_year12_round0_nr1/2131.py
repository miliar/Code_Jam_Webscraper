#include<stdio.h>
#include<math.h>
#include<stdlib.h>
#include<inttypes.h>
#include<string.h>
#include<inttypes.h>

int main()
{ 
  int numberCases;
  int length,temp,i,k;
  char google[]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
  char input[101];
  char output[101];
  scanf("%d",&numberCases);
  gets(input);
  for(i=0;i<numberCases;i++)
  {
          gets(input);
          length=strlen(input);
          for( k=0;k<length;k++)
          {
                if(input[k]!=' ')
                {
                               temp=input[k];
                               temp= temp - 97;
                               output[k]=google[temp];
                }  
                else
                    output[k]=input[k];
                  
          }
          output[k]='\0';
          printf("Case #%d: %s\n",i+1,output);
  }
  
  return 0;
}
