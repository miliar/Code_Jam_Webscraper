#include<iostream>
#include<cstdio>
using namespace std;
char s[101][100];
int check[101];
char q[1001][101];
int test,n,m;

void init()
{
int i;
for(i=1;i<=n;i++) check[i]=0;
}



int slove()
{
int i,j,sum=0;
i=1;
int total=0;
while(i<=m)
{
for(j=1;j<=n;j++)
 if (strcmp(s[j],q[i])==0)
 {
   check[j]++;
   if (check[j]==1) sum++;
   if (sum==n)
   {
   total++;
   init();
   sum=0;
   }
   else i++;
   break; 	   
 }
}
return total;
}

int main()
{
int i,j,k;
freopen("A-large.in","r",stdin);
freopen("o.out","w",stdout);
scanf("%d",&test);
for(i=1;i<=test;i++)
{
scanf("%d",&n);
getchar();
for(j=1;j<=n;j++) 
{
	gets(s[j]);
    check[j]=0;
}

scanf("%d",&m);
getchar();
for(j=1;j<=m;j++) gets(q[j]);

printf("Case #%d: %d\n",i,slove());
}
return 0;
}
