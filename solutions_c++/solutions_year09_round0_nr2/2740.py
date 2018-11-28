#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;
int h,w,t,a[110][110],b[110][110],val,m;
	
	int fun(int x,int y)
	{if(b[x][y]!=0)
	return b[x][y];
        int minx=x,miny=y,min=a[x][y];
        if(a[x-1][y]<min)
        {minx=x-1;
        miny=y;
        min=a[x-1][y];}
         if(a[x][y-1]<min)
        {minx=x;
        miny=y-1;
        min=a[x][y-1];}
         if(a[x][y+1]<min)
        {minx=x;
        miny=y+1;
        min=a[x][y+1];}
         if(a[x+1][y]<min)
        {minx=x+1;
        miny=y;
        min=a[x+1][y];}
        if(minx==x&&miny==y)
        return val++;
        if(b[minx][miny]!=0)
        {return b[minx][miny];}
        else
        {b[minx][miny]=fun(minx,miny);
        }
        return b[minx][miny];
        }
        
 
int main()
{
    freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	
	scanf("%d",&t);
	m=t;
	while(t)
	{t--;
	scanf("%d %d",&h,&w);
	//memset(a,32760,110*110);
		for(int i=0;i<=h+2;i++)
	{
            for(int j=0;j<=w+2;j++)
            {
                    a[i][j]=32000;
                    }
                    }
	for(int i=1;i<=h;i++)
	{
            for(int j=1;j<=w;j++)
            {
                    scanf("%d",&a[i][j]);
                    }
                    }
                    	
      memset(b,0,110*110);
      val=97;
      	for(int i=1;i<=h;i++)
	{
            for(int j=1;j<=w;j++)
            {
    b[i][j]= fun(i,j);                                       
}}
printf("Case #%d:\n",m-t);
   	for(int i=1;i<=h;i++)
	{
            for(int j=1;j<=w;j++)
            {printf("%c ",b[i][j]);
            }printf("\n");
            }
}return 0;
}
