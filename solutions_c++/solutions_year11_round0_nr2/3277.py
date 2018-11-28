# include<stdio.h>
# include<string.h>
# include<conio.h>
# include<iostream.h>
main()
{
freopen("input.txt","r",stdin);
freopen("output.txt","w",stdout);
int i,j,k,n,m,c,d,l,pos;
char com[3][40],opp[2][40],inv[100],fin[100],z;
scanf("%d",&n);
scanf("\n");
for(i=0;i<n;i++)
 {
 scanf("%d ",&c);
 for(j=0;j<c;j++)
  {
   for(k=0;k<3;k++)
   {
   scanf("%c",&com[k][j]);
   //printf("%c",com[k][j]);
   }
   scanf(" ");
   //printf("\n");
   }

 scanf("%d ",&d);
  for(j=0;j<d;j++)
  {
   for(k=0;k<2;k++)
   {
   scanf("%c",&opp[k][j]);
   //printf("%c",opp[k][j]);
   }
   scanf(" ");
   //printf("\n");
  }
  scanf("%d ",&l);
  for(k=0;k<l;k++)
   {
   scanf("%c",&inv[k]);
   //printf("%c",inv[l]);
   }

  pos=0;
 for(j=0;j<l;j++)
  {
   if(j==0 || pos==0)
    {
      fin[pos]=inv[j];
      pos++;
      continue;
    }
   fin[pos]=inv[j];

   for(k=0;k<c;k++)
    {

     if(com[0][k]==fin[pos-1] && fin[pos]==com[1][k])
       {
        fin[pos]='0';
        fin[pos-1]=com[2][k];
        pos--;
        k=0;
       }
     if(com[0][k]==fin[pos] && fin[pos-1]==com[1][k])
       {
        fin[pos]='0';
        fin[pos-1]=com[2][k];
        pos--;
        k=0;
       }

   }
   for(k=0;k<d;k++)
    {
     if(opp[0][k]== fin[pos])
      {
       for(z=0;z<(pos);z++)
        {
         if(fin[z]== opp[1][k])
          {
          memset(fin,0,(pos)) ;
          pos=0;
          break;
          }
        }
      }
      if(opp[1][k]== fin[pos])
      {
       for(z=0;z<(pos);z++)
        {
         if(fin[z]== opp[0][k])
          {
            memset(fin,0,(pos));
            pos=0;
            break;
          }
        }
      }
    }

   pos++;
  }
 scanf("\n");
 printf("Case #%d: [",(i+1));
 k=0;
 for(z=0;z<(pos);z++)
    {
     k++;
     if(fin[z]=='\0')
      continue;
     printf("%c",fin[z]);
     if(z!=(pos-1) && pos!=1)
      printf(", ");
    }
 printf("]\n");
 }
//getch();
}
