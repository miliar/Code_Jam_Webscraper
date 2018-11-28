#include<stdio.h>
#include<mem.h>
#include<string.h>
int viz[101],n,m,s,q,i,j,k,l,p,nr,qr[1001];
char se[101][102],qu[102],c;

int egale(){
int i,n;
n=strlen(qu);
if(n-strlen(se[k]))
 return 0;
for(i=0;i-n;i++)
  if(qu[i]-se[k][i])
   return 0;
return 1;
}

int main(){
FILE *in=fopen("A-SMAL~1.in","r"),*out=fopen("A.out","w");
fscanf(in,"%d",&n);
for(i=1;i-n-1;i++){
 fscanf(in,"%d",&s);
 c=fgetc(in);
  for(j=1;j-s-1;j++)
   fgets(se[j],101,in);//,l=strlen(se[j]);
 fscanf(in,"%d",&q);
 c=fgetc(in);
  for(j=1;j-q-1;j++){
   fgets(qu,101,in);
    for(k=1;k-s-1;k++)
      if(egale()){
       qr[j]=k;
       break;
      }
  }
 memset(viz,0,sizeof(viz));
 nr=0;l=0;
  for(j=1;j-q-1;j++)
    if(!viz[qr[j]]){
      if(nr==s-1){
       memset(viz,0,sizeof(viz));
       nr=0;l++;
      }
     viz[qr[j]]=1;nr++;
    }
 fprintf(out,"Case #%d: %d\n",i,l);
}
fclose(in);
fclose(out);
return 0;
}
