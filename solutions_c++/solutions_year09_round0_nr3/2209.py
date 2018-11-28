#include<stdio.h>
#include<string.h>

char temp[1009],mah[100];
long cas1,cas,len,i,j,A[100];

int main()
{
  freopen("C-large.in","r",stdin);
  freopen("C_out.txt","w",stdout);
     
strcpy(mah,"welcome to code jam");    
gets(temp);   
sscanf(temp,"%ld",&cas);    
    
for(cas1=1;cas1<=cas;cas1++)
{
gets(temp);

len = strlen(temp);

for(j=0;j<19;j++)
A[j]=0;

for(i=0;i<len;i++)
{
 for(j=18;j>=1;j--)
 if(temp[i]==mah[j])
 {
                    A[j]+= A[j-1];
                    A[j] = A[j]%10000;                   
 }
 if(mah[0]==temp[i])
 {
                    A[0]++;
                    A[0]=A[0]%10000;
 }
}

if(cas1!=1)
printf("\n");
printf("Case #%ld: %04ld",cas1,A[18]%10000);

}        
return 0;    
}
