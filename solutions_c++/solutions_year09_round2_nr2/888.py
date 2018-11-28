#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
using namespace std;
int main()
{
    int n,x,y;
    char A[21],B[21],c;
    scanf("%d",&n);
    for(x=1;x<=n;x++)
    { scanf("%s",A);
      strcpy(B,A);
      sort(A,A+strlen(A));
      strrev(A);
      
      if(strcmp(B,A)<0)
      {  next_permutation(B,B+strlen(B));
         printf("Case #%d: %s\n",x,B);
      }
      else
      { strrev(A);y=0;
        while(A[y]=='0')
          y++;
        c=A[0]; A[0]=A[y]; A[y]=c;  
        for(y=strlen(A)+1;y>=2;y--)
          A[y]=A[y-1];
        A[1]='0';
        printf("Case #%d: %s\n",x,A);
      } 
      }    
    return 0;
}
