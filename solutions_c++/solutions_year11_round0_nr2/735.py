#include <cstdio>
#include <cstring>
int main(){
   int t;
   char **com, **del, *seq;
   int c,d,n;
   char *stack,size;
   char t1,t2;
   char freq[26];
   FILE *fp=fopen("B-large.in","r");
   FILE *fo=fopen("out.txt","w");
   fscanf(fp,"%d", &t);
   for(int i=0;i<t;i++){
      fscanf(fp,"%d", &c);
      com=new char*[c];
      for(int j=0;j<c;j++){
         com[j]=new char[4];
         fscanf(fp, "%s", com[j]);
      }
      fscanf(fp, "%d", &d);
      del=new char*[d];
      for(int j=0;j<d;j++){
         del[j]=new char[4];
         fscanf(fp, "%s", del[j]);
      }
      fscanf(fp, "%d", &n);
      seq=new char[n+1];
      size=0;
      stack=new char[n+1];
      fscanf(fp, "%s", seq);
      memset(freq,0,26);
      for(int j=0;j<n;j++){
         stack[size++]=seq[j];
         freq[seq[j]-'A']++;
         if(size>=2&&c!=0){
            for(int k=0;k<c;k++){
               t1=stack[size-1];
               t2=stack[size-2];
               if(t1==com[k][0]&&t2==com[k][1]||t1==com[k][1]&&t2==com[k][0]){
                  size-=2;
                  freq[t1-'A']--;freq[t2-'A']--;freq[com[k][2]-'A']++;
                  stack[size++]=com[k][2];
                  k--;
               }
            }
         }
         for(int k=0;k<d;k++)
            if(freq[del[k][0]-'A']&&freq[del[k][1]-'A']){
               memset(freq,0,26);
               size=0;
            }
      }
      fprintf(fo,"Case #%d: [",i+1);
      if(size!=0)fprintf(fo,"%c",stack[0]);
      for(int j=1;j<size;j++)
         fprintf(fo,", %c", stack[j]);
      fprintf(fo,"]\n");
      for(int j=0;j<c;j++)
         delete[] com[j];
      for(int j=0;j<d;j++)
         delete[] del[j];
      delete[] com;delete[] del;delete[] seq;delete[] stack;
   }
   fclose(fp);fclose(fo);
}
