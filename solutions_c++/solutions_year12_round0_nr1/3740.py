#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;


void read_params(const char *file_path)
{
  FILE *f = NULL;
          char ans[]={"yhesocvxduiglbkrztnwjpfmaq"};
        char s[120];
        int T,i,l,j;
  if (file_path)
  {
    f = fopen(file_path, "rt");
    if (f)
    {
      fscanf(f, "%d\n", &T);
      
      int T1=0;
        while(T--)
        {
		fgets(s,120,f);
                l=strlen(s);
		T1++;
		printf("Case #%d: ", T1);
                for(i=0;i<l-1;i++)
                {
                        if(s[i]>='a'&&s[i]<='z')
                        {
                                j=s[i]-'a';
                                printf("%c",ans[j]);
                        }
                        else
                                printf("%c",s[i]);
                }
                printf("\n");
                
        }
      fclose(f);
    }
  }
}

int main (int argc, char **argv)
{
  if (argc >1)
  {
    read_params(argv[1]);
  }
  return 0;
}