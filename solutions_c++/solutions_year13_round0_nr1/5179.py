#include<stdio.h>
#include<conio.h>
#include<iostream.h>
#include<math.h>

int compute(int a[4][4])
{
     
     int i,s1,s2,sum=0;
     int r=4;//Game has not completed
     
     for(i=0;i<=3;i++)
     {
                      s1=a[i][0]+a[i][1]+a[i][2]+a[i][3];
                      s2=a[0][i]+a[1][i]+a[2][i]+a[3][i];
                      
                      if(s1==4 ||s1==6 ||s2==4 ||s2==6)
                      return 1;//X won
                      if(s1==80 ||s1==63 ||s2==80 ||s2==63)
                      return 2;//O won
                      
                      sum=sum+s1;
     }
     s1=a[0][0]+a[1][1]+a[2][2]+a[3][3];
     s2=a[0][3]+a[1][2]+a[2][1]+a[3][0];
     if(s1==4 ||s1==6 ||s2==4 ||s2==6)
     return 1;//X won
     if(s1==80 ||s1==63 ||s2==80 ||s2==63)
     return 2;//O won
     
     if(sum==151||sum==168)
     return 3;//Draw
     
     return r;
}
main()
{
      int a[4][4];
      FILE *fp,*fw;
      fw=fopen("output_large.txt","w");
      fp=fopen("A-large.in","r");
      int ary[10],i=0,n=0,j=0,val;
      char s1[]="X won";
      char s2[]="O won";
      char s3[]="Draw";
      char s4[]="Game has not completed";
      char s[]="Case #";
      char ss[]=": ";
     char c=fgetc(fp);
     while(c!='\n')
     {
                   ary[i]=c-48;
                   c=fgetc(fp);
                   i++;
     }
                  
        i--;
                   while(i>=0)
                   {
                         n=n+ary[j]*pow(10,i);
                         j++;
                         i--;
                   }
                            // cout<<n;
                             
                                     
                   
     for(j=1;j<=n;j++)
     {
               for(i=0;i<=3;i++)
               {
                                c=fgetc(fp);
                                if(c=='X')
                                 a[i][0]=1;
                                 else if(c=='O')
                                 a[i][0]=20;
                                 else if(c=='.')
                                 a[i][0]=-200;
                                 else
                                 a[i][0]=3;
                                 
                                 c=fgetc(fp);
                                if(c=='X')
                                 a[i][1]=1;
                                 else if(c=='O')
                                 a[i][1]=20;
                                 else if(c=='.')
                                 a[i][1]=-200;
                                 else
                                 a[i][1]=3;
                                 
                                 c=fgetc(fp);
                                if(c=='X')
                                 a[i][2]=1;
                                 else if(c=='O')
                                 a[i][2]=20;
                                 else if(c=='.')
                                 a[i][2]=-200;
                                 else
                                 a[i][2]=3;
                                 
                                 c=fgetc(fp);
                                if(c=='X')
                                 a[i][3]=1;
                                 else if(c=='O')
                                 a[i][3]=20;
                                 else if(c=='.')
                                 a[i][3]=-200;
                                 else
                                 a[i][3]=3;
                                 
                                 c=fgetc(fp);
                                 
               }
               val=compute(a);
               
               fputs(s,fw);
               fprintf(fw,"%d",j);
               fputs(ss,fw);
               
               if(val==1)
               fputs(s1,fw);
               else if(val==2)
               fputs(s2,fw);
               else if(val==3)
               fputs(s3,fw);
               else
               fputs(s4,fw);
               
               fputc('\n',fw);
               c=fgetc(fp);
     
     }
               

}
