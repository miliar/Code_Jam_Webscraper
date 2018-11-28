#include<stdio.h>

int main()
{
int N,n;
char ch;
freopen("A-small-attempt0.in","rt",stdin);
freopen("googlerese.out","wt",stdout);
scanf("%d",&N);
scanf("%c",&ch);
for(n=1;n<=N;n++)
{
printf("Case #%d: ",n);
while(1)
{                 
                  
               ch = getc(stdin);
               if(ch=='\n')
               {
               printf("\n");
               break;
               }
               if(ch==EOF)
               break;
               if(ch=='a')
               printf("y");
               if(ch=='b')
               printf("h");
               if(ch=='c')
               printf("e");
               if(ch=='d')
               printf("s");
               if(ch=='e')
               printf("o");
               if(ch=='f')
               printf("c");
               if(ch=='g')
               printf("v");
               if(ch=='h')
               printf("x");
               if(ch=='i')
               printf("d");
               if(ch=='j')
               printf("u");
               if(ch=='k')
               printf("i");
               if(ch=='l')
               printf("g");
               if(ch=='m')
               printf("l");
               if(ch=='n')
               printf("b");
               if(ch=='o')
               printf("k");
               if(ch=='p')
               printf("r");
               if(ch=='q')
               printf("z");
               if(ch=='r')
               printf("t");
               if(ch=='s')
               printf("n");
               if(ch=='t')
               printf("w");
               if(ch=='u')
               printf("j");
               if(ch=='v')
               printf("p");
               if(ch=='w')
               printf("f");
               if(ch=='x')
               printf("m");
               if(ch=='y')
               printf("a");
               if(ch=='z')
               printf("q");
               if(ch==' ')
               printf(" "); 
               }
}                             
}
