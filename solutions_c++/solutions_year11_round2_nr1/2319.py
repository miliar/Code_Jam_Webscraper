# include<stdio.h>
# include<string.h>
# include<conio.h>
# include<iostream.h>
main()
{
freopen("input.txt","r",stdin);
//freopen("output.txt","w",stdout);
int m;
scanf("%d",&m);
scanf("\n");
for(int i=0;i<m;i++)
 {
  int n,not;
  char tab[110][110];
  long double wp[110],owp[110],oowp[110];
  scanf("%d",&n);
  scanf("\n");
  for(int j=0;j<n;j++)
   {
     for(int k=0;k<n;k++)
     {
     scanf("%c",&tab[j][k]);
     }
     scanf("\n");
   }
  /*
  for(int j=0;j<n;j++)
   {
    for(int k=0;k<n;k++)
     {
          printf("%c",tab[j][k]);
     }
     printf("\n");
   }
     */
   for(int j=0;j<n;j++)
   {
    not=0;
    wp[j]=0;
    int w=0;
    for(int k=0;k<n;k++)
    {
      if(tab[j][k]=='.')
       not++;
     if(tab[j][k]=='1')
       w+=1;
    }
   // printf(" w=%d ",w);
   wp[j]=(long double)w/(n-not);
  // printf("%Lf ",wp[j]);
   }
   //printf("\n");
   //getch();
   for(int j=0;j<n;j++)
    {
     owp[j]=0;

     long double t=0;
     long double w,s;
     s=0;
     w=0;
       for(int k=0;k<n;k++)
       {
        if(tab[j][k]=='.')
         continue;
        else
        {     w=0;
              t++;
              not=1;
              for(int k1=0;k1<n;k1++)
              {
               if(k1==j)
                 continue;
               else
                {
                 if(tab[k][k1]=='.')
                  not++;

                if(tab[k][k1]=='1')
                  w+=1;
                }
              }
           //printf("%d ",(n-not));
            s+=(long double)w/(n-not);
        }
       }
     //printf("t=%Lf w=%Lf",t,w);
     owp[j]=(long double)s/t;
     //printf("%Lf ",owp[j]);
    }
   //printf("\n");
   //getch();

   for(int j=0;j<n;j++)
    {
     oowp[j]=0;
     long double t=0;
     long double w;
     w=0;
       for(int k=0;k<n;k++)
       {
        if(tab[j][k]=='.')
         continue;
        else
        {
         w+=owp[k];
         t++;
        }
       }
     oowp[j]=(long double)w/t;
     //printf("%Lf ",oowp[j]);
    }
     //printf("\n");
     //getch();
     printf("Case #%d:\n",(i+1));
   for(int j=0;j<n;j++)
    {
     long double fin;
     fin=0.25*wp[j] +0.5*owp[j] + 0.25*oowp[j];
     printf("%.12Lf\n",fin);
    }
   scanf("\n");

 }
getch();
}
