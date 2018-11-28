#include<cstdio>
#include<string>
#include<iostream>
using namespace std;

int main()
{ 
  int j, k,l,h;
  long long int W[20];
  char T[]="welcome to code jam", m='1';
  char P[503];
  int N, i;
  long long int Test[101];
  scanf("%d", &N);
  for(i=0;i<N;i++)
 {
 scanf("%c", &m);
  h=0;
  while(true)
  {
     P[h++]=m;
     scanf("%c", &m);
     if(m=='\n')
     break;
  }
  P[h]='\0';
   for(j=0;j<20;j++)
  {
    W[j]=0;
  }
   l=strlen(P);
   for(j=0;j<l;j++)
  { if(P[j]=='w')
    {
        W[0]+=1;
    }
    for(k=1;k<19;k++)
    {
       if(P[j]==T[k])
       {
         W[k]+=W[k-1];
       }
    }
  }
 
  Test[i]=W[18];
  
}
 for(i=0;i<N;i++)
{
  Test[i]=Test[i]%10000;
}
 for(i=0;i<N;i++)
{ printf("Case #%d: ", i+1);
  if(Test[i]>=1000)
  {
    printf("%d\n", Test[i]);
  }
  else if(Test[i]>=100)
  {
    printf("0%d\n", Test[i]);
  }
  else if(Test[i]>=10)
 {
    printf("00%d\n", Test[i]);
  }
  else if(Test[i]>=0)
 {
    printf("000%d\n", Test[i]);
  }
}
return 0;
}

