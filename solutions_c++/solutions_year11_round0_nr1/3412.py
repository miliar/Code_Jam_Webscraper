# include<stdio.h>
# include<string.h>
# include<conio.h>
# include<iostream.h>
main()
{
freopen("input.txt","r",stdin);
freopen("output.txt","w",stdout);
int n,c,j,a[2000],i,k,diff[2000],h;
scanf("%d",&n);
scanf("\n");
for(i=0;i<n;i++)
 {
 scanf("%d",&c);
 scanf("\n");
 scanf("%d",&j);
 scanf("\n");
 for(k=0;k<j;k++)
  {
  scanf("%d",&a[k]);
  diff[k]=c-a[k];
   for(h=0;h<k;h++)
     {
     if(diff[h]==a[k])
     printf("Case #%d: %d %d",(i+1),(h+1),(k+1));
     }
   }

 scanf("\n");
 printf("\n");
 }
//getch();
}