#include<stdio.h>
#include<math.h>
int main()
{int i,j,k;
int testcases;
int a[10000];
FILE *file;
FILE *outfile;
file=fopen("f.in","r");
outfile=fopen("f.out","w");
fscanf(file,"%d",&testcases);
int count=0;
while(count<testcases)
{ int sum=0,max=0;
  int number=0;
fscanf(file,"%d",&number);
for(i=0;i<number;i++)
fscanf(file,"%d",&a[i]);
int xorcheck=0;
 for(i=0;i<number;i++)
  {
  xorcheck=xorcheck^a[i];
  }
 if(xorcheck==0)
 {                  
  sum=0;
  sum++;
  int smallest=a[0];
 for(i=0;i<number;i++)
  { sum=sum+a[i];
  if(smallest>a[i])
  { smallest=a[i];
  }
  }
sum -=smallest;
sum--;  
if(max<sum)
max=sum;
fprintf(outfile,"Case #%d: %d\n",count+1,max);
}
else
fprintf(outfile,"Case #%d: NO\n",count+1);

count++;
}
}
