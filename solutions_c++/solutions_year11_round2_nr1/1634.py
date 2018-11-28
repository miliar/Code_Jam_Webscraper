#include<stdio.h>
#include<conio.h>
#include<stdlib.h>

void main()
{
FILE *f,*f1;
char a[100][100],c;
int n1,n,i,j,k,w,t,to[100],wo[100];
float wp[100], oowp[100], owp[100],temp,rpi[100];


f = fopen("input.txt","r");

f1 = fopen("output.txt","w");

fscanf(f,"%d",&n1);
for(k=0;k<n1;k++)
{
fscanf(f,"%d",&n);
printf("n-%d",n);
c = fgetc(f);
for(i=0;i<n;i++)
{

for(j=0;j<n;j++)
{
a[i][j] = fgetc(f);

printf("a%c",a[i][j]);
//fscanf(f,"%c ",&a[i][j]);
}
c = fgetc(f);
}



for(i=0;i<n;i++)
{
t=0;w=0;
for(j=0;j<n;j++)
{
     if(a[i][j]=='1')
     {
     t++;
     w++;
     }
     else if (a[i][j] =='0')
     {
     t++;
     }
}
to[i]=t;
wo[i]=w;
if(t==0)
wp[i]=0;
else
wp[i] = (float)w/(float)t;

}


for(i=0;i<n;i++)
{
t=0;temp = 0;
for(j=0;j<n;j++)
{

     if(a[i][j]=='1')
     {
     if((to[j]-1)!=0)
     temp = temp + ((float)wo[j]/(float)(to[j]-1));
     t++;
     }
     else if (a[i][j] =='0')
     {
     if((to[j]-1)!=0)
     temp = temp + ((float)(wo[j]-1)/(float)(to[j]-1));
     t++;
     }

}
if(t==0)
owp[i] = 0;
else
owp[i] = (float)temp/(float)t;
}



for(i=0;i<n;i++)
{
t=0;temp = 0;
for(j=0;j<n;j++)
{

     if(a[i][j]!='.')
     {
     temp = temp + owp[j];
     t++;
     }

}
if(t==0)
oowp[i]=0;
else
oowp[i] = (float)temp/(float)t;
}


for(i = 0;i<n;i++)
{
rpi[i] = (.25*wp[i]) + (.5*owp[i]) + (.25 * oowp[i]);
}

fprintf(f1,"Case #%d:\n",k+1);
printf("Case #%d:\n",k);
for(i = 0;i<n;i++)
{
fprintf(f1,"%f\n",rpi[i]);
printf("%f\n",rpi[i]);
}

}
}