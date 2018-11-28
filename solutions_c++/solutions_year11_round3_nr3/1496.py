#include<stdio.h>
#include<conio.h>
FILE *fp,*fp2;
  
int main()
{
  int k,l,t;
  fp=fopen("f.in","r");
  fp2=fopen("f.out","w");  
  fscanf(fp,"%d",&t);
  for (int x=1;x<=t;x++)
  {int n,l,h;
   int freq[100];
  fscanf(fp,"%d %d %d",&n,&l,&h);
  printf("{%d}\n",n);
  for(int i=0;i<n;i++)
  {
  fscanf(fp,"%d",&freq[i]);
  }
  fprintf(fp2,"Case #%d: ",x);
  if(l==1)
  {
  fprintf(fp2,"%d\n",l);
  }
  int flag=1;
  for(int i=l;i<=h;i++)
  {flag=1;
  for(int j=0;j<n && flag==1;j++)
  {if(freq[j]%i!=0 && i%freq[j]!=0)
  {flag=0;
  printf("%d %d\n",i,freq[j]);
  continue;
  }
  }
  if(flag==1)
  {if(i!=1)fprintf(fp2,"%d\n",i);
   break;
  }
  
  }
  if(flag==0)
  fprintf(fp2,"NO\n");    
  }
  getch();       
 return 0;   
}
