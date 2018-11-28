#include<stdio.h>
int main()
{
 int r,n,k,t,s=0,i,a[200],l,y,e,p,x,tmp=0,sum=0;
 long int val=0;
FILE *fin,*fout;

fin=fopen("cin.in","r");
fout=fopen("out1.txt","w");
fscanf(fin,"%d",&t);
for(i=0;i<t;i++)
{
s=i+1;
fscanf(fin,"%d%d%d",&r,&k,&n);
for(y=0;y<n;y++)
{
fscanf(fin,"%d",&a[y]);
}

for(x=0;x<r;x++)
{
l=0;
while(l<n&&tmp<=k)
{tmp=tmp+a[l];
l++;
if(tmp<=k){
sum=tmp;
}
}

val+=sum;

tmp=0;sum=0;
e=0;
while(e<l)
{
a[n+e]=a[e];
e++;
}

p=0;
while(p<n)
{
a[p]=a[l+p-1];
p++;
}

}
fprintf(fout, "Case #%d: %ld\n",s,val);  
val=0;
}

fclose(fin);
fclose(fout);

}






