#include<string.h>
#include<stdio.h>
 
int main()
{       int t,i,length,num,base;
        char gg[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
        char str[102],tmp;
        num=1;
          scanf("%d%c",&t,&tmp);
        while(t--)
        {       gets(str);
                length=strlen(str);
                printf("Case #%d: ",num++);
                for(i=0;i<length;i++)
                {       base=str[i]-'a';
                        if(base>=0&&base<=25)
                                printf("%c",gg[base]);
                        else
                                printf(" ");
                }
                printf("\n");
        }
       
        return 0;
}