#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#include <string.h>

//#define D_DATA_MAX 11   //small
//#define N_DATA_MAX 281 //small
//#define D_MAX 25 //small
//#define N_MAX 10 //small
//#define L_MAX 10 //small

#define D_DATA_MAX 16   //big
#define N_DATA_MAX 421 //big
#define D_MAX 5000 //big
#define N_MAX 500 //big
#define L_MAX 15 //big


//void init(FILE *fp)
//{
//	int i,j;
//	int l=3,d=5,n=4;
//	char ddata[5][4]={"abc","bca","dac","dbc","cba"};
//	char ndata[4][50]={"(ab)(bc)(ca)","abc","(abc)(abc)(abc)","(zyx)bc"};
//	fp=fopen("small.in","w");
//	if(!fp) exit(0);
//	fprintf(fp,"%d %d %d\n",l,d,n);
//	for(i=0;i<d;i++)
//	{
//		fputs(ddata[i],fp);
//		fprintf(fp,"\n");
//	}
//	for(i=0;i<n;i++)
//	{
//		fputs(ndata[i],fp);
//		fprintf(fp,"\n");
//	}
//	fclose(fp);
//}
//void dis_in(FILE *fp)
//{
//	char c;
//	FILE *ft=fp;
//	while(!feof(ft))
//	{
//		//fgetc(fp,c);
//		fscanf(ft,"%c",&c);
//		putch(c);
//	}
//}
//void file_read(FILE *fp,int &l,int &d,int &n,char **ddata,char **ndata)
//{
//	FILE *ft=fp;
//	int i,j;
//	fscanf(fp,"%d %d %d\n",&l,&d,&n);
//	ddata=(char **)malloc((l+1)*n*sizeof(char));
//	ndata=(char **)malloc(sizeof(char));
//}

void main()
{
	int i,j,k,p,m,f;
	char word[L_MAX];
	char stack[L_MAX][29]={0};
	int l,d,n;
	int count;
	char ddata[D_MAX][D_DATA_MAX],ndata[N_MAX][N_DATA_MAX];
	//打开in文件
	FILE *fp=fopen("A-large.in","r"),*ft=fopen("A-large.out","w");;
	if(!fp) exit(0);
	if(!ft) exit(0);
	//读出文件内的数据
	fscanf(fp,"%d %d %d\n",&l,&d,&n);



	printf("%d %d %d\n",l,d,n);


	for(i=0;i<d;i++)
	{
		fscanf(fp,"%s\n",ddata[i]);
	}
	for(i=0;i<n;i++)
	{
		fscanf(fp,"%s\n",ndata[i]);
	}

	for(i=0;i<d;i++)
	{
		printf("%s ",ddata[i]);
	}
	printf("\n");
	for(i=0;i<n;i++)
	{
		printf("%s ",ndata[i]);
	}
	printf("\n");



	//做n个测试
	for(i=0;i<n;i++)
	{
		//建立l个栈
		k=0;
		p=0;
		f=0;//0表示没有括号
		for(j=0;ndata[i][j]!=NULL;j++)
		{
			if(ndata[i][j]=='(')
			{
				f=1;
				continue;
			}
			else if(ndata[i][j]==')')
			{
				f=0;
				k++;
				p=0;
				continue;
			}
			stack[k][p]=ndata[i][j];
			if(f==0)
			{
				k++;
				p=0;
			}
			else
			{
				p++;
			}
		}



		for(j=0;j<l;j++)
		{
			printf("%s ",stack[j]);
		}
		printf("\n");



		count=0;
		//检查
		for(j=0;j<d;j++)
		{
			f=0;
			for(k=0;k<l;k++)
			{
				for(p=0;stack[k][p]!=0;p++)
				{
					if(stack[k][p]==ddata[j][k])
					{
						f=1;
						break;
					}
					else
					{
						f=0;
					}
				}
				if(f==0)
				{
					break;
				}
			}
			if(f==1)
			{
				count++;
			}
		}
		fprintf(ft,"Case #%d: %d\n",i+1,count);
		for(j=0;j<L_MAX;j++)
		{
			for(k=0;k<29;k++)
			{
				stack[j][k]=0;
			}
		}
	}
	printf("output in the .out file\n");
	fclose(fp);
	fclose(ft);
	getch();
}