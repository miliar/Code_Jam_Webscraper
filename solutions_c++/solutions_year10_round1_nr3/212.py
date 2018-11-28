#include <cstdio>
#include <iostream>
#include <fstream>

#define max(a,b) ((a)>(b)?(a):(b))
#define min(a,b) ((a)<(b)?(a):(b))

int main(int argc, char **argv)
{
   FILE *fin;
   std::ofstream fout;  
   int *a; /*game is lost for (m,n) iff a[m]<=n<=b[m]*/
   int *b;
   int i,j;
   int T,a1,a2,b1,b2;
   __int64 sum;

   a=(int*) malloc(sizeof(int)*1000001);
   b=(int*) malloc(sizeof(int)*1000001);

//   printf("%p, %p\n",a,b);
   if (argc!=3) 
   {
     printf("Use: numbergame input output\n");
     exit(1);            
   }
   
//   printf("Hallo");
   a[1]=1;
   b[1]=1;
   a[2]=2;
   b[2]=3;
   i=2;
   j=2;
   while(j<=1000000)
   {
//     printf("%d\n",j);
     for (j=b[i-1]+1;j<=b[i];j++)
     {
       if (j>1000000) break;
       a[j]=i;
       b[j]=a[j]+j-1;
     }
     i++;
   }
   
//   for (i=1;i<=20;i++) printf("a[%d]=%d, b[%d]=%d\n",i,a[i],i,b[i]);
   
   fin=fopen(argv[1],"r");
   fout.open(argv[2]);
   
   fscanf(fin,"%d\n",&T);
   for (i=1;i<=T;i++)
   {
     fscanf(fin,"%d %d %d %d\n",&a1,&a2,&b1,&b2);
     sum=0;
     for (j=a1;j<=a2;j++)
     {
         if (b1<=a[j]) sum+=(min(a[j],b2+1)-b1);
         if (b2>=b[j]) sum+=(b2-max(b1-1,b[j]));
     }
     fout << "Case #" << i << ": " << sum << std::endl;
   }
   
   fclose(fin);
   fout.close();
}
