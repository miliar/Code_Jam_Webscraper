#include<stdio.h>

long i,j,N,K,cas,cas1,k,BB,R;
char A[109][109],B[109][109];

long Check(char c)
{

long h1 = 0;
long i1,j1,x1,y1,z1;

for(i1=0;i1<N;i1++)
for(j1=0;j1<N;j1++)
if(A[i1][j1]==c)
{
x1 = i1;
y1 = j1;
z1 = 0;

while(1)
{
if(A[x1][y1]!=c)
break;
z1++;
if(z1>=K)
return 1;
y1++;
if(y1>=N)
break;
}

x1 = i1;
y1 = j1;
z1 = 0;

while(1)
{
if(A[x1][y1]!=c)
break;
z1++;
if(z1>=K)
return 1;
x1++;
if(x1>=N)
break;
}

x1 = i1;
y1 = j1;
z1 = 0;

while(1)
{
if(A[x1][y1]!=c)
break;
z1++;
if(z1>=K)
return 1;
y1++;
x1++;
if(y1>=N||x1>=N)
break;
}

x1 = i1;
y1 = j1;
z1 = 0;

while(1)
{
if(A[x1][y1]!=c)
break;
z1++;
if(z1>=K)
return 1;
y1--;
x1--;
if(y1<0||x1<0)
break;
}

}

return 0;
}

int main()
{

// freopen("A-small-attempt1.in","r",stdin);
// freopen("A-small-out.out","w",stdout);

scanf("%ld",&cas);

for(cas1=1;cas1<=cas;cas1++)
{

scanf("%ld %ld",&N,&K);

for(i=0;i<N;i++)
scanf("%s",A[i]);


for(i=0;i<N;i++)
for(j=0;j<N;j++)
B[i][j]=A[N-j-1][i];


for(j=0;j<N;j++)
{
k=N-1;
for(i=N-1;i>=0;i--)
if(B[i][j]!='.')
{
A[k][j]=B[i][j];
k--;
}
while(k>=0)
{
A[k][j]='.';
k--;
}
}

BB = Check('B');
R = Check('R');

printf("Case #%ld: ",cas1);

if(BB==1&&R==1)
printf("Both");
else if(BB==1)
printf("Blue");
else if(R==1)
printf("Red");
else
printf("Neither");               

printf("\n");

}

return 0;    
}
