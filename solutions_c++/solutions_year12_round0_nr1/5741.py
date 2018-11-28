#include<cstdio>
#include<cstring>
#include<ctype.h>
char str1[512] = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
char alpha[27];
char str2[512] = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
void process()
{
    int len = strlen(str1);

    for(int i = 0; i < len ; i++)
    {
        if(!isspace(str1[i]))
        {
            alpha[str1[i] - 'a'] = str2[i];

        }
    }
     alpha['q' - 'a'] = 'z';
     alpha['z' - 'a'] = 'q';
  /*  for(int i = 0; i < 26 ; i++)
    {
        printf("%c %c\n",'a'+i,alpha[i]);
    }*/
}


int main()
{
    process();

    int t;
   // char line1[25] = "y qee";

    //for(int i = 0; i < strlen(line1) ; i++) if(!isspace(line1[i])) line1[i] = alpha[line1[i] - 'a'];

//    printf("%s",line1);

    scanf("%d\n",&t);
    int cs = 1;
    char line[256];
    while(t--)
    {
       // scanf("%s",line);
        gets(line);

        int len = strlen(line);
        for(int i = 0; i<len ; i++ )
        {
            if(!isspace(line[i]))
            {
                line[i] = alpha[line[i] - 'a'];
            }
        }

        printf("Case #%d: %s\n",cs++,line);
    }

    return 0;
}
