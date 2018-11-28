//written on C++ (compatible with DevC++ / MS Visual C++ 6)
#include<stdio.h>

int h[1001][11];

int happy(int num,int b)
{
    int b1[32],i,n,num1,num2;
    if(num<=1000)return h[num][b];
    num1=num;
    while(1)
    {num2=num1;
     n=0;
     while(num2){b1[n]=num2%b;num2/=b;n++;}
     num1=0;
     for(i=0;i<n;i++)num1+=(b1[i]*b1[i]);
     if(num1==1)return 1;
     return h[num1][b];
    }
}

int happy1(int num,int b)
{
    int b1[32],i,n,num1,num2,nums[1000],ok,x;
    num1=num;x=0;
    while(1)
    {num2=num1;
     n=0;
     while(num2){b1[n]=num2%b;num2/=b;n++;}
     num1=0;
     for(i=0;i<n;i++)num1+=(b1[i]*b1[i]);
     if(num1==1)return 1;
     for(i=0;i<x;i++){if(num1==nums[i])return 0;}
     nums[x]=num1;x++;
    }
}

int main()
{
    char x[100];
    int bases[10],i,j,n,num,ok,t;
    freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
    scanf("%d\n",&t);
	for(i=2;i<=1000;i++)for(j=2;j<=10;j++)h[i][j]=happy1(i,j);
    for(i=1;i<=t;i++)
	{
     gets(x);
     j=0;n=0;
     while(1)
     {bases[n]=x[j]-'0';
      if(bases[n]==1){bases[n]=10;j++;}
      j++;n++;
      if(!x[j])break;
      j++;
     }
     num=2;
     while(1)
     {ok=1;
      for(j=0;j<n;j++){if(!happy(num,bases[j])){ok=0;break;}}
      if(ok)break;
      num++;
     }
     printf("Case #%d: %d\n",i,num);
    }
    return 0;
}
