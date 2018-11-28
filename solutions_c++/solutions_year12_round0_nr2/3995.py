# include<stdio>
# include<string>
# include<conio>
# include<algorithm>
using namespace std;
main()
{
freopen("input.txt","r",stdin);
//freopen("output.txt","w",stdout);
int m;
scanf("%d",&m);
scanf("\n");
for(int i=0;i<m;i++)
 {
  int n,s,p,flag,count=0;
  int sc[1000];
  scanf("%d %d %d",&n,&s,&p);
  printf("%d %d %d",n,s,p);
  for(int j=0;j<n;j++)
   {
    scanf(" %d",&sc[j]);
    printf(" %d",sc[j]);
   }
   printf("\n");
  for(int j=0;j<n;j++)
   {
    int l,m;
    flag=0;
    for(int k=10;k>=0;k--)
     {
       for(l=0;l<=2;l++)
        {
         m=sc[j]-(k+(k-l));
         if(m<=10 && m>=0 && k-l>=0 && abs(k-m)<2 && abs(k-l-m)<2 && abs(k-(k-l))<2)
          {
           if(k>=p || k-l>=p || m>=p)
               {
                printf("%d %d %d \n",k,k-l,m);
                flag=1;
                count++;
                printf(" %d ",count);
                break;
               }
           }
         }
		if(flag==1)
         break;
     }
    if(flag!=1)
    {
    for(int k=10;k>=0;k--)
     {
       for(l=0;l<=2;l++)
        {
         m=sc[j]-(k+(k-l));
         if(m<=10 && m>=0 && k-l >=0 && abs(k-m)<3 && abs(k-l-m)<3 && abs(k-(k-l))<3)
          {
           if(abs(k-m)==2 || abs(k-l-m)==2 || abs(k-(k-l))==2)
            {
            if(s>0)
             {
             printf("%d %d %d *\n",k,k-l,m);
             if(k>=p || k-l>=p || m>=p)
               {
                s--;
                flag=1;
                count++;
                printf(" %d ",count);
                break;
               }
             }
            }
           else
             {
              printf("%d %d %d\n",k,k-l,m);
              if(k>=p || k-l>=p || m>=p)
               {
                flag=1;
                count++;
                printf("\n %d \n",count);
                break;
               }
             }
           }
         }
       if(flag==1)
         break;
     }
    }
     printf("\n");
   }
  printf("Case #%d: %d",(i+1),count);

  printf("\n");
 }
getch();
}