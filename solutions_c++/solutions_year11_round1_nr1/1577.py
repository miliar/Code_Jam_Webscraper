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
for(int i=0;i<m;i++)
{
 int n,e=0;
 int pd,pg;
 scanf("%d ",&n);
 scanf("%d ",&pd);
 scanf("%d ",&pg);
 //printf("%d %d %d\n",n,pd,pg);
 for(int j=1;j<=n;j++)
  {
   float tw;
   tw=((float)pd/100)*(float)j;
   //printf("pd=%d j=%d tw=%f\n",pd,j,tw);
   if((int)tw != tw)
    {
     e=0;
    // printf("here1\n");
     continue;
    }
   else
   {
    for(int x=1;x<1000;x++)
    {
      float g;
      if(pg==0)
       break;
      g=(float)x*(100/(float)pg);
      //printf("%d %d %f\n",j,x,g);
      if((int)g == g && g>j && x>=(int)tw)
      {
      int loss1=j-(int)tw;
      int loss2=(int)g-x;
      if(loss2>=loss1)
      {
      e=1;
      break;
      }
      }
      if((int)g == g && g==j && x==(int)tw )
      {
      int loss1=j-(int)tw;
      int loss2=(int)g-x;
      if(loss2>=loss1)
      {
      e=1;
      break;
      }
      }

    }

   }
   if(e==1)
    break;

  }
 if(e==0)
     printf("Case #%d: Broken",(i+1));
   if(e==1)
     printf("Case #%d: Possible",(i+1));
 scanf("\n");
 //getch();
 printf("\n");
}
//getch();
}
