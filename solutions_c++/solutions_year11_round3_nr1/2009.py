# include<stdio.h>
# include<string.h>
# include<conio.h>
# include<iostream.h>
main()
{
freopen("input.txt","r",stdin);
freopen("output.txt","w",stdout);
int m;

scanf("%d",&m);
scanf("\n");
for(int i=0;i<m;i++)
 {
  int r,c ;
  int tab[55][55];
  int imp=0;
  scanf("%d %d",&r,&c);
  scanf("\n");
  for(int j=0;j<r;j++)
   {
    for(int k=0;k<c;k++)
    {
     scanf("%c",&tab[j][k]);
     //printf("%c",tab[j][k]);
    }
    scanf("\n");
   }
   for(int j=0;j<r;j++)
   {
    for(int k=0;k<c;k++)
    {
     if(tab[j][k]=='#' && tab[j][k+1]=='#' && tab[j+1][k]=='#' && tab[j+1][k+1]=='#')
      {
       tab[j][k]='/';
       tab[j][k+1]='a';
       tab[j+1][k]='a';
       tab[j+1][k+1]='/';
       }
      }
    }
    for(int j=0;j<r;j++)
   {
    for(int k=0;k<c;k++)
    {
     if( tab[j][k]=='#')
      imp=1;
    }

   }
    scanf("\n");
   printf("Case #%d:\n",(i+1));
   if(imp==0)
   {
    for(int j=0;j<r;j++)
   {
    for(int k=0;k<c;k++)
    {
      if(tab[j][k]=='a')
      {
       printf("\\");
      }
      else
       printf("%c",tab[j][k]);

    }
    printf("\n");
   }
  }
  else
   printf("impossible");
   //getch();
  scanf("\n");
  printf("\n");
 }
//getch();
}
