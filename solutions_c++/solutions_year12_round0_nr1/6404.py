#include<stdio.h>
#include<conio.h>
#include<ctype.h>
main()
{

    char C[10]="Case ",D[10]="#",F[10]=": ",G[3500],E[50]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q','\0'};
    int t=30,i=0,A,x,k=1;
    FILE *f1,*f2;
    f1=fopen("input.txt", "r");
    f2=fopen("output.txt","w");


   while(feof(f1)==0)
  {
   if(i==0)
   {
   fprintf(f2,"%s%s%d%s",C,D,k,F);
   k++;
   }
  G[i]=getc(f1);
  if(G[i]==' ')
  {
   putc(G[i],f2);
   i++;
   continue;
  }
  else if(G[i]=='\n')
  {
      if(k==31)
   break;
    putc(G[i],f2);
    fprintf(f2,"%s%s%d%s",C,D,k,F);
   k++;

  }
  else{
         A=toascii(G[i]);
            A-=97;
            G[i]=E[A];
            putc(G[i],f2);
            i++;
            continue;
      }
        }

fclose(f1);
fclose(f2);


  getch();
    }



