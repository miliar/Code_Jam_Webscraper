#include<cstdio>
#include<algorithm>
#include<string>
using namespace std;

int main()
{

  int T,i,j;
  
  char ch, X[504][25],num[504],L[25];
  scanf("%d", &T);
  for(i=0;i<T;i++)
  { num[i]=0;
    scanf("%s", X[i]);
    strcpy(L, X[i]);
    num[i]=strlen(X[i]);
    next_permutation(X[i],X[i]+num[i]);
    int f=0;
   if(X[i][0]=='0')
   {
    strcpy(X[i],L);
    f=3;
    sort(X[i],X[i]+num[i]);
    reverse(X[i],X[i]+num[i]);
    for(j=num[i]-1;j>=0;j--)
    {
      if(X[i][j]!='0')
      break;
    }
    reverse(X[i],X[i]+j+1);
    int o=j;
    X[i][num[i]]='0';
    num[i]++;
    sort(X[i]+1,X[i]+num[i]);
    num[i]++;
     X[i][num[i]]='\0';
   }
 
   for(j=0;j<num[i]-1;j++)
   {
        if(X[i][j]>X[i][j+1])
        f=1;
   }
   if(f==0)
   {
      for(j=num[i];j>1;j--)
     {
        X[i][j]=X[i][j-1];
     }
     X[i][1]='0';
     num[i]++;
   }
   X[i][num[i]]='\0';
 
 }
  
  for(i=0;i<T;i++)
{

   printf("Case #%d: %s\n",i+1,X[i]);
}
return 0;
}

