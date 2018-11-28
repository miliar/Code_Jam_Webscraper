//written on C++ (compatible with DevC++ / MS Visual C++ 6)
#include<stdio.h>

int m[40][40],m1[40],n,x;

void swap(int a,int b)
{
     int i,temp;
     temp=m1[a];m1[a]=m1[b];m1[b]=temp;
     for(i=0;i<n;i++){temp=m[a][i];m[a][i]=m[b][i];m[b][i]=temp;}
     //printf("%d %d\n",a,b);
     return;
}

int main()
{
    int a,aa,i,j,k,t;
    freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {scanf("%d\n",&n);
     for(j=0;j<n;j++)
     {for(k=0;k<n;k++){scanf("%c",&m[j][k]);m[j][k]-='0';}
      scanf("\n");
     }
     for(j=0;j<n;j++){m1[j]=n-1;while(!m[j][m1[j]])m1[j]--;}
     //for(j=0;j<n;j++)printf("%d\n",m1[j]);
     x=0;
     for(j=0;j<n;j++)
     {if(m1[j]>j)
      {a=j+1;while(m1[a]>j)a++;
       aa=a;
       for(k=0;k<aa-j;k++){swap(a-1,a);a--;x++;}
      }
     }
     printf("Case #%d: %d\n",i,x);
    }
    return 0;
}
