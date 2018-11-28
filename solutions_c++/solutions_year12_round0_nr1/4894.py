#include<stdio.h>
#include<string.h>
 int i;
    char a[100]="ejp mysljylc kd kxveddknmc re jsicpdrysi";
    char b[100]="rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
    char c[100]="de kr kd eoya kw aej tysr re ujdr lkgc jv";
    char x[100]="our language is impossible to understand";
    char y[100]="there are twenty six factorial possibilities";
    char z[100]="so it is okay if you want to just give up";
    char l[500];
    char m[26];
  int main()
  {
   
   
   for(i=0;i<strlen(a);i++)
    {
  
      m[a[i]-'a']=x[i];
 
    }
    for(i=0;i<strlen(b);i++)
    {
         m[b[i]-'a']=y[i];
 
    }
    for(i=0;i<strlen(c);i++)
    {
        m[c[i]-'a']=z[i];
 
    }
    m['q'-'a']='z';
    m['z'-'a']='q';


    int j=1,t;
    freopen ("A-small-attempt1.in","r",stdin);
    freopen("A-small-attempt1.out","w",stdout);
    scanf("%d",&t);
    gets(l);
    while(t--)
    {

        gets(l);
        printf("Case #%d: ",j);
 
     for(i=0;i<strlen(l);i++)
     printf("%c",m[l[i]-'a']);
     j++;
     printf("\n");
    }
    fclose (stdin);
    fclose (stdout);
return 0;
}
