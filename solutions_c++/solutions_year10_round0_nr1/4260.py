 #include<stdio.h>
#include<conio.h>

#include<math.h>

int cnt,n;
long k;

int main()
{
int i;
long tmp1,tmp2,p;
char fp[32],in[32];
FILE *fin,*fout;


fin=fopen("as2.in","r");
fout=fopen("a-out.txt","w");

fscanf(fin,"%d",&cnt);

for(i=0;i<cnt;i++)
{
fscanf(fin,"%d %d",&n,&k);

tmp1=pow(2,n);
tmp2=tmp1-1;
p=1;

while(1)
{
if(tmp2==k)
{fprintf(fout,"Case #%d: ON\n",i+1);
break;
}
else if(tmp2>k)
{fprintf(fout,"Case #%d: OFF\n",i+1);
break;
}
else if(tmp2<k)
{
p=p+1;
tmp2=p*tmp1-1;
}
}
}
}
 