#include<stdio.h>
#include<string.h>
int main()
{
    freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	
    char a[110][110],b[110];
int i=0,n,m,c[110],j=0,count,ans=0,t;
scanf("%d",&t);
while(t)
{
i=0;
ans=0;
j=0;
    scanf("%d",&n);
    gets(a[0]);
    while(i<n)
    {
    gets(a[i]);
    //puts(a[i]);
    
    i++;
}
//fflush(stdin);
//printf("ggg");
scanf("%d",&m);
gets(b);
//printf("hhh");
j=0;
count=0;
for(int i=0;i<n;i++)
c[i]=0;
while(j<m)
{
          //printf("aaaaaaaaaa\n");
j++;
i=0;

gets(b);
while(strcmp(b,a[i])!=0)
{// printf("bbbbbbb\n");
i++;}
if(c[i]!=1)
{
if(count<n-1)
{
             count++;
c[i]=1;
}
else
{count=1;

    for(int k=0;k<n;k++)
c[k]=0;
c[i]=1;
ans++;
}
}}
printf("Case #%d: %d\n",21-t,ans);
t--;}//while(1);
return 0;
}

    

