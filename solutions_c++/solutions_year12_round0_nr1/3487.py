#include<stdio.h>
#include<string.h>

int main()
{
  char mymap[]="yhesocvxduiglbkrztnwjpfmaq";
  char in[128];
  int n;
  scanf("%d\n", &n);
  
  for(int i = 1; i <= n; i++)
  {
    gets(in);
    printf("Case #%d: ", i);
    for(int i = 0; i < strlen(in); i++)
    {
//      printf("%c", in[i]);
      if(in[i]==' ') printf(" ");
      else printf("%c", mymap[in[i]-'a']);
    }
    printf("\n");
  }
      
  return 0;
}