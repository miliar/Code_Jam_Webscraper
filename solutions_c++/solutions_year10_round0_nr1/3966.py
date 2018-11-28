#include<stdio.h>


int funct(int n,int k)
{
int i,num=1; 
i=1;
         while(i<=n){num=num*2; i++;}


if( (k+1)%num == 0 ) return 1;
else return 0;
}


int main()
{
freopen("A-large.in","rt",stdin);
freopen("A-large.out","wt",stdout);    

int tests,i;
i=1;
scanf("%d",&tests);    
 while(i<=tests)
 {
 int n,nn,k;
 scanf("%d %d",&n,&k);
 nn=funct(n,k);
 if(nn==1)
 printf("Case #%d: ON\n",i);
 else
 printf("Case #%d: OFF\n",i);
 i++;    
}    
    
    
    
}
