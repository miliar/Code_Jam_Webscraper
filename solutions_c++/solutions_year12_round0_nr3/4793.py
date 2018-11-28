// a.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"

#include<stdio.h>
#include<string.h>
#include<math.h>
#include<stdlib.h>
                                 //#define longlong _int64

#define MAXINT 2147483647
int main()
{
    int n;
    FILE *fin,*fout;
	fin=fopen("c:\C-small-attempt2.in","r");
	fout=fopen("c:\data.out","a");


	fscanf(fin,"%d\n",&n);
	//getchar();
	for(int s=1;s<=n;s++)
	{
       char str[104];int ans;ans=0;
        int n,m,num[10],biao[10000];
		memset(biao,0,sizeof(biao));
		fscanf(fin,"%d%d",&n,&m);
        if(m<10)ans=0;
		else for(int i=n;i<=m;i++)
		{
          int  l=0;int q;q=i;
		   while(q>=10)
		   {
			   num[l]=q%10;
			   q=q/10;
			   l++;
		   }
		   num[l]=q;
		   for(int j=0;j<l;j++)
		   {
			   int k;
			   k=0;int bei;bei=1;
			   for(int d=j+1;d<=l;d++){k=k+num[d]*bei;bei=bei*10;}
			   for(int d=0;d<=j;d++){k=k+num[d]*bei;bei=bei*10;}

			   if(k<=m&&k>=n&&/*biao[k]!=1&&*/i<k){/*biao[k]=1;printf("%d %d\n",i,k);*/ans++;}
		   }

		}
		fprintf(fout,"Case #%d: ",s);
		fprintf(fout,"%d\n",ans);
		
	}
	fclose(fin);
	fclose(fout);


	return 0;


}

