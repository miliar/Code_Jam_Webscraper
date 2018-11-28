#include <stdio.h>
#include <stdlib.h>
#include <conio.h>

#define T_MAX 100

//#define HW_MAX 10 //SMALL
//#define SINK_MAX 2 //SMALL
//#define WALL 11 //SMALL
#define HW_MAX 100 //BIG
#define SINK_MAX 26 //BIG
#define WALL 10001 //BIG

void main()
{
	int i,j,k,p,x,y,f,xt,yt,tmp;
	int h_stack[HW_MAX],w_stack[HW_MAX],top;
	int h_sink[SINK_MAX],w_sink[SINK_MAX];
	int t,h,w,altitude[HW_MAX+2][HW_MAX+2],sink[HW_MAX+2][HW_MAX+2],sink_num;
	char character[HW_MAX+2][HW_MAX+2],sque_sink[SINK_MAX];
	FILE *fp,*ft;
	fp=fopen("B-large.in","r");
	ft=fopen("B-large.out","w");
	if(!fp) exit(0);
	if(!ft) exit(0);
	fscanf(fp,"%d\n",&t);
	for(i=0;i<t;i++)
	{
		fscanf(fp,"%d %d\n",&h,&w);
		//建立地图
		for(j=0;j<h+2;j++)
		{
			for(k=0;k<w+2;k++)
			{
				if(k==0||j==0||j==h+1||k==w+1)
				{
					altitude[j][k]=WALL;
				}
				else
				{
					fscanf(fp,"%d",&altitude[j][k]);
				}
				if(k==w+1)
				{
					fscanf(fp,"\n");
				}
				else
				{
					fscanf(fp," ");
				}
			}
		}
		//搜索漩涡，建立漩涡数组
		for(j=0;j<SINK_MAX;j++)
		{
			h_sink[j]=0;
			w_sink[j]=0;
			sque_sink[j]=0;
		}
		p=1;
		sink_num=0;
		for(j=1;j<=h;j++)
		{
			for(k=1;k<=w;k++)
			{
				if(altitude[j][k]<=altitude[j-1][k]&&altitude[j][k]<=altitude[j][k-1]&&altitude[j][k]<=altitude[j+1][k]&&altitude[j][k]<=altitude[j][k+1])
				{
					sink[j][k]=p;
					h_sink[p-1]=j;
					w_sink[p-1]=k;
					sque_sink[p-1]=0;
					p++;
					sink_num++;
				}
				else
				{
					sink[j][k]=0;
				}
			}
		}
		//清空特征矩阵
		for(j=0;j<h+2;j++)
		{
			for(k=0;k<w+2;k++)
			{
				character[j][k]=0;
			}
		}
		//寻找路径
		f=-1;
		for(xt=1;xt<=h;xt++)
		{
			for(yt=1;yt<=w;yt++)
			{
				//选择初始节点
				if(character[xt][yt]!=0)
				{
					continue;
				}
				//清空栈
				top=0;
				for(p=0;p<HW_MAX;p++)
				{
					h_stack[p]=0;
					w_stack[p]=0;
				}
				//一次搜索路径
				j=xt;
				k=yt;
				while(j<=h&&k<=w)
				{
					h_stack[top]=j;
					w_stack[top]=k;
					top++;
					if(altitude[j-1][k]<altitude[j][k]&&altitude[j-1][k]<=altitude[j][k-1]&&altitude[j-1][k]<=altitude[j][k+1]&&altitude[j-1][k]<=altitude[j+1][k])
					{
						j--;
					}
					else if(altitude[j][k-1]<altitude[j][k]&&altitude[j][k-1]<altitude[j-1][k]&&altitude[j][k-1]<=altitude[j][k+1]&&altitude[j][k-1]<=altitude[j+1][k])
					{
						k--;
					}
					else if(altitude[j][k+1]<altitude[j][k]&&altitude[j][k+1]<altitude[j-1][k]&&altitude[j][k+1]<altitude[j][k-1]&&altitude[j][k+1]<=altitude[j+1][k])
					{
						k++;
					}
					else if(altitude[j+1][k]<altitude[j][k]&&altitude[j+1][k]<altitude[j-1][k]&&altitude[j+1][k]<altitude[j][k-1]&&altitude[j+1][k]<altitude[j][k+1])
					{
						j++;
					}
					else
					{
						for(p=0;p<sink_num;p++)
						{
							if(j==h_sink[p]&&k==w_sink[p])
							{
								break;
							}
						}
						if(sque_sink[p]==0)
						{
							f++;
							sque_sink[p]='a'+f;
						}
						//出栈
						while(top>0)
						{
							top--;
							x=h_stack[top];
							y=w_stack[top];
							character[x][y]=sque_sink[p];
						}
						break;
					}
				}
			}
		}
		////调整character
		//f=1;
		//for(j=1;j<=sink_num;j++)
		//{
		//	if(character[f][j]!=alp[j-1])
		//	{
		//		for(k=0;k<=h;k++)
		//		{
		//			for(p=0;p<=w;p++)
		//			{
		//				character[k][p]=j;
		//			}
		//		}
		//	}
		//	if()
		//}
		//输出character
		fprintf(ft,"Case #%d:\n",i+1);
		printf("Case #%d:\n",i+1);
		for(j=1;j<=h;j++)
		{
			for(k=1;k<=w;k++)
			{
				fprintf(ft,"%c",character[j][k]);
				printf("%c",character[j][k]);
				if(k==w)
				{
					fprintf(ft,"\n");
					printf("\n");
				}
				else
				{
					fprintf(ft," ");
					printf(" ");
				}
			}
		}









	}

	fclose(fp);
	fclose(ft);
	getch();
}