#include <cstdio>
#include <cstring>
int main(){
   int t,n;
   int *seq;
   int x,min,sum;
   FILE *fp=fopen("C-large.in","r");
   FILE *fo=fopen("out.txt","w");
   fscanf(fp,"%d", &t);
   for(int i=0;i<t;i++){
      x=min=sum=0;
      fscanf(fp,"%d", &n);
      seq=new int[n];
      for(int j=0;j<n;j++){
         fscanf(fp,"%d",seq+j);
         sum+=seq[j];
         x^=seq[j];
         if(!min)min=seq[j];
         if(min>seq[j])min=seq[j];
      }
      fprintf(fo,"Case #%d: ", i+1);
      if(x){
         fprintf(fo,"NO\n");
      }else{
         fprintf(fo,"%d\n", sum-min);
      }
      delete[] seq;
   }
   fclose(fp);fclose(fo);
}
