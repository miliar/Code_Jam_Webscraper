#include<stdio.h>
#include<stdlib.h>
char a[150][150]={0},b[150]={0},ans[150];
int main(){
    freopen("B-small-attempt1.in","r",stdin);
    freopen("B-small-attempt1.txt","w",stdout);
    int k,t,n,l,i,j,c;
    char x,y,z;
    scanf("%d",&t);
    for(k=1;k<=t;k++)
    {
     for(i='A';i<='Z';i++)
     {
      b[i]=0;
      for(j='A';j<='Z';j++) a[i][j]=0;
     }

     scanf("%d",&n);
     for(i=0;i<n;i++)
     {
      scanf(" %c %c %c",&x,&y,&z);
      a[x][y]=a[y][x]=z;
     }

     scanf("%d",&n);
     for(i=0;i<n;i++)
     {
      scanf(" %c %c",&x,&y);
      b[x]=y,b[y]=x;
     }

     l=0;
     scanf("%d",&n);
     for(i=0;i<n;i++)
     {
      scanf(" %c",&x);
      if(l==0) ans[l++]=x;
      else if(a[x][ans[l-1]]!=0) { l--,ans[l]=a[x][ans[l]],l++; }
      else
      {
       c=0;
       for(j=l-1;j>=0;j--)
        if(ans[j]==b[x]) { c=1; break; }

       if(c) l=0;
       else ans[l++]=x;
      }
     }
     printf("Case #%d: ",k);
     printf("[");
     for(i=0;i<l;i++)
     {
      printf("%c",ans[i]);
      if(i!=l-1) printf(", ");
     }
     printf("]\n");
    }
}

