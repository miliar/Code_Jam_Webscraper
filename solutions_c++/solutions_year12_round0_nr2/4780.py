#include<stdio.h>
 int n,s,p,t,i,fc,y;
   
int main()
{
    int ca=1;
 freopen ("B-large.in","r",stdin);
  freopen("B-large.out","w",stdout);
   scanf("%d",&t);
   while(t--){
      fc=0;
   scanf("%d%d%d",&n,&s,&p);
   for(i=1;i<=n;i++)
   {

      scanf("%d",&y);
    
       if(y/3>=p)
       fc++;
       else if(((y/3+2==p)&&(y%3==2)&&(s!=0)))
       {
           fc++;
           s--;
       }
       else if(((y/3+1==p)&&(y%3>=1))||(((y/3==p)&&(y%3>=0))))
       {
           fc++;
       }
       else if(((y/3+1==p)&&(y%3==0)&&(s!=0)&&(y!=0)))
       {
           s--;
           fc++;
       }
   }
   printf("Case #%d: %d\n",ca,fc);
ca++;
    }
  fclose (stdin);
   fclose (stdout);
   return 0;
}
