#include<stdio.h>
#include<string.h>
char mp[30];
FILE*f1=fopen("A-small-attempt0.in","r");
FILE*f2=fopen("out.out","w");
int main()
{
    
    char ar1[]="ejp mysljylc kd kxveddknmc re jsicpdrysi";
    char tr1[]="our language is impossible to understand";
    char ar2[]="rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
    char tr2[]="there are twenty six factorial possibilities";
    char ar3[]="de kr kd eoya kw aej tysr re ujdr lkgc jv";
    char tr3[]="so it is okay if you want to just give up";
    int i;
     mp[25] = 'q';
     mp[16] = 'z';
    for(i=0;i<strlen(ar1);i++)
    {
     //printf("%d\n",i);
     if(ar1[i] != ' ')
     mp[ar1[i]-'a']=tr1[i];
    }
    for(i=0;i<strlen(ar2);i++)
     if(ar2[i] != ' ')
     mp[ar2[i]-'a']=tr2[i];
    for(i=0;i<strlen(ar3);i++)
     if(ar3[i] != ' ')
     mp[ar3[i]-'a']=tr3[i];    
     
     /*for(i=0;i<26;i++)
     printf("%c %c\n",'a'+i,mp[i]);
     for(i=0;i<26;i++)
     printf("%d   %d\n",i,mp[i]-'a');*/
     int t;
     char x;
     fscanf(f1,"%d%c",&t,&x);
     i=0;
    fprintf(f2,"Case #1: ");
    while(i < t)
    {
     x='7';
     fscanf(f1,"%c",&x);
     if(x == '7')
     break;
     //printf("%c zzz %d\n",x,i);
     //scanf("%*c");
     if(x < 'a' || x > 'z')
     {
      if(x == '\n')
      {
       i++;
       if(i!=t)
       {
       fprintf(f2,"\n");
       fprintf(f2,"Case #%d: ",i+1);
       }
       continue;
      }
      fprintf(f2,"%c",x);
      continue;
     }
     fprintf(f2,"%c",mp[x-'a']);
    }
    //scanf("%*d");
}
