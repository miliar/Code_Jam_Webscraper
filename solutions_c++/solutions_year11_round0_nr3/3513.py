#include<stdio.h>
#include<conio.h>
#include<malloc.h>

int main()
{
 
 int t,n,i,j;
 int *c;
 int count=0;
 int big,small,temp;
 scanf("%d",&t);
 while(t>0)
 {
           count++;
           scanf("%d",&n);
           c=(int *)malloc(n * sizeof(int));
           for(i=0;i<n;i++)
           scanf("%d",&c[i]);
           for(i=0;i<n-1;i++)
            {
            for(j=i+1;j<n;j++)
            {
                if(c[i]>c[j])
                {
                temp=c[i];
                c[i]=c[j];
                c[j]=temp;
                }
            }
            }
            temp=0;
//    while(n>0)
            for(i=0;i<n;i++)  
            {
               temp=temp^c[i];
            }
            if(temp!=0) 
            {
                printf("Case #%d: NO\n",count);
            }
            else
            {
            temp++;
            while(temp<n)
            {
            big=small=0;
            for(i=temp;i<n;i++)
            {
             big=big^c[i];
            }
            for(j=0;j<temp;j++)
            {
             small=small^c[j];
            }
            if(small>=big)
            {
                          big=0;
                          for(i=temp;i<n;i++)
                          big=big+c[i];
                          printf("Case #%d: %d\n",count,big);
                          break;
            }
            temp++;
            }
            }   
    
 t--;
 }
 getch();
 return 0;   
}
