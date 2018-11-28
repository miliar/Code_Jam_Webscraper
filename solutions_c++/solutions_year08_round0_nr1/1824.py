#include<stdio.h>
#include<string.h>
char A[109][109],temp[109];
long n,m,i,j,k,start,mid,end;
long count,B[109],test,test1,N;

int main()
{
    
//////freopen("A-large.in","r",stdin);
///////freopen("A_large_out.in","w",stdout);    

gets(temp);   
sscanf(temp,"%ld",&test);    
    
for(test1=1;test1<=test;test1++)    
{    
gets(temp);    
sscanf(temp,"%ld",&n);    
for(i=0;i<n;i++)
{
gets(A[i]);
B[i]=0;                
}    

for(i=0;i<n-1;i++)    
for(j=0;j<n-1-i;j++)
if(strcmp(A[j],A[j+1])>0)    
{
strcpy(temp,A[j]);
strcpy(A[j],A[j+1]);
strcpy(A[j+1],temp);                             
}    
gets(temp);    
sscanf(temp,"%ld",&m);    
N=n;
count=0;
for(i=1;i<=m;i++)
{
gets(temp);
start=0;end=n-1;
mid=(start+end)/2;
while(start<=end)
{
k=strcmp(temp,A[mid]);
if(k==0)
break;
else if(k>0)
start=mid+1;
else
end=mid-1;
mid=(start+end)/2;                
}
if(B[mid]==0)
{
if(N==1)
{
count++;
for(j=0;j<n;j++)
B[j]=0;
N=n;
}
B[mid]=1;
N--;             
}                 
}

    
printf("Case #%ld: %ld\n",test1,count);
    
    
}   
    
return 0;    
}
