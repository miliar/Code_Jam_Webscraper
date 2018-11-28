#include <cstdio>
int main(){
   int t,n,count,temp;
   int *seq;
   FILE *fp=fopen("D-large.in","r");
   FILE *fo=fopen("out.txt","w");
   fscanf(fp,"%d", &t);
   for(int i=0;i<t;i++){
      count=0;
      fscanf(fp,"%d", &n);
      seq=new int[n];
      for(int j=0;j<n;j++){
         fscanf(fp,"%d",seq+j);
         if(seq[j]!=j+1)count++;
      }
      fprintf(fo,"Case #%d: %d.000000\n",i+1,count);
      delete[] seq;
   }
   fclose(fp);fclose(fo);
}
