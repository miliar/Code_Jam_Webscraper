#include<stdio.h>
#include<string.h>
#include<math.h>

char sa[5009][19],temp[200000];
long p[5009],i,j;
long a,b,c,n,m,t,t1,len,count,k;

int main()
{
  freopen("A-large.in","r",stdin);
  freopen("a_out.txt","w",stdout);
       
while(scanf("%ld %ld %ld",&b,&a,&c)==3)    
{

for(i=0;i<a;i++)
scanf("%s",sa[i]);

for(j=1;j<=c;j++)
{

scanf("%s",temp);

len = strlen(temp);
n=0;
m=0;
while(n<len)
{
if(temp[n]>='a'&&temp[n]<='z')
{
p[m] = pow(2,temp[n]-'a');
m++;
n++;
}
else if(temp[n]=='(')
{
 p[m]=0;
 n++;
 while(temp[n]!=')')
 {
 if(temp[n]>='a'&&temp[n]<='z')
 {
   p[m]+= pow(2,temp[n]-'a');
 }
 n++;
 }
 n++;
 m++;    
}
else
n++;            
}
count = 0;
if(m==b)
for(i=0;i<a;i++)
{
for(k=0;k<b;k++)
{
t = pow(2,sa[i][k]-'a'+1);
t1 = p[k] % t;
t = t /2;
if(t1<t)
break;  
}
if(k==b)
count++;
} 
if(j!=1)
printf("\n");
printf("Case #%ld: %ld",j,count);                 
}                
}        
return 0;    
}
