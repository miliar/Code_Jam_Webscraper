//#include <stdafx.h>
#include <iostream>
#include<stdio.h>
//#include<conio.h>
#include<malloc.h>
using namespace std;
int main()
{
	int i,n,h,w,j,flag,j1,k1,idx,k,min,j2,k2;
	int **map;
	char **bsn;
	char **res;
	char snk='a';
	FILE *fp,*fp2;
	fp=fopen("B-large.in","r");
	fp2=fopen("B-output.txt","w");
    //scanf("%d",&n);
	fscanf(fp,"%d",&n);
    for(i=0;i<n;i++)
	{
	 snk='a';
                    // scanf("%d%d",&h,&w);
      fscanf(fp,"%d%d",&h,&w);
	  map=(int**)malloc(sizeof(int*)*(h+2));
	  bsn=(char**)malloc(sizeof(char*)*(h+2));
	  res=(char**)malloc(sizeof(char*)*(h+2));
	  for(j=0;j<h+2;j++)
	  {
			map[j]=(int*)malloc(sizeof(int)*(w+2));
			bsn[j]=(char*)calloc(w+2,sizeof(char));
			res[j]=(char*)malloc(sizeof(char)*(w+2));
	  }

	  for(j=0;j<h+2;j++)
	  {
			for(k=0;k<w+2;k++)
			{
				bsn[j][k]=' ';
			}

	  }


	  h=h+1;
	  w=w+1;
	  j=0;

	  while(j<=w)
	  {
			map[0][j]=11000;
			map[h][j]=11000;
			j++;
	  }
	  j=0;
	  while(j<=h)
	  {
		map[j][0]=11000;
		map[j][w]=11000;
		j++ ;
	  }
      
	  for(j=1;j<h;j++)
	  {
			for(k=1;k<w;k++)
			{
				//scanf("%d",&map[j][k]);
				fscanf(fp,"%d",&map[j][k]);
			}
	  }
      
	  
      idx=0;
	  for(j=1;j<h;j++)
	  {
			for(k=1;k<w;k++)
			{
					


							j2=j;
							k2=k;
							flag=0;
							while(1)//find sink when indirect...
							{
								flag=0;
                                j1=j2;
								k1=k2;
								idx=0;
								if(map[j1][k1]<=map[j1+1][k1]&&map[j1][k1]<=map[j1-1][k1]&&map[j1][k1]<=map[j1][k1+1]&&map[j1][k1]<=map[j1][k1-1])
								{
									idx=0;
									if(bsn[j1][k1]==' ')
									{
										bsn[j1][k1]=snk;
										res[j][k]=snk++;
									      //	bsn[j1][k1]=1;
										break;
									}
									else
									{
										res[j][k]=bsn[j1][k1];
									       //	bsn[j1][k1]=1;
										break;

									}
								}
								if(flag==0)
								{

								min=map[j1-1][k1];
								flag=1;
								}
								if(map[j1][k1-1]<min)
								{
									min=map[j1][k1-1];
									j2=j1;
									k2=k1-1;
									idx=4;
								}

								if(map[j1][k1+1]<min)
								{
									min=map[j1][k1+1];
									j2=j1;
									k2=k1+1;
									idx=2;
								}
								if(map[j1+1][k1]<min)
								{
									min=map[j1+1][k1];
									j2=j1+1;
									k2=k1;
									idx=3;
								}
								if(idx==0)
								{
									min=map[j1-1][k1];
									j2=j1-1;
									k2=k1;
									idx=0;

								}

							}

			}


	  }
      fprintf(fp2,"Case #%d:\n",i+1);
      for(j=1;j<h;j++)
      {
                      for(k=1;k<w;k++)
			          {

							
                            fprintf(fp2,"%c",res[j][k]);
                            if(k!=(w-1))
                            {
                                       fprintf(fp2," ");
                                       }
                      }
                      if(i==(n-1)&&j==(h-1))
                      {
                      }
                      else
                      {
                          fprintf(fp2,"\n");
                      }
       }

       }
	fclose(fp2);
	return 0;
}

