#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <string.h>
#include <math.h>
#include <iostream>
using namespace std;
int i, j, k, e, n, t, L, c, time, count, len, x0, res, res1, res2;
int a[1000], b[1000], cc[1000], flag[1000];
void getX0()
{
	x0=0;
	while (len>b[x0]) x0++;
	x0++;
}
int onStar()
{
	int ii, m_flag=0;
	for (ii=0; ii<n; ii++)
	{
		if (b[ii]==len)
		{
			m_flag=1;
			break;
		}
	}
	return m_flag;
}
void setFlag(int num)
{
	if (num==2&&x0==n) return;
	if (num==2&&x0==n-1)
	{
		flag[x0]=1;
		return;
	}
	if (num==1&&x0==n) return;
	int ii, jj, max, index;
	for (ii=0; ii<num; ii++)
	{
		max=0;
		for (jj=x0; jj<n; jj++)
		{
			if (flag[jj]==0&&a[jj]>max)
			{
				max=a[jj];
				index=jj;
			}
		}
		flag[index]=1;
	}
}
void main()
{
	FILE *rFile=fopen("D:\\B-small-attempt2.in", "r"); e=ferror(rFile); assert(e==0);
	FILE *wFile=fopen("D:\\R1C-out.txt", "w"); e=ferror(wFile); assert(e==0);
	fscanf(rFile, "%d", &t);
	//scanf("%d", &t);
	for (i=1; i<=t; i++)
	{
		fscanf(rFile, "%d %d %d %d", &L, &time, &n, &c);
		//scanf("%d %d %d %d", &L, &time, &n, &c);
		for (j=0; j<c; j++) fscanf(rFile, "%d", &cc[j]);
			//scanf("%d", &cc[j]);
		count=0;
		for (j=0; j<n; j++)
		{
			a[j]=cc[count];
			count=(count+1)%c;
		}
		for (j=0; j<n; j++)
		{
			b[j]=0;
			for (k=0; k<=j; k++) b[j]+=a[k];
		}
		len=time/2;
		getX0();
		if (L==0)
			res=b[n-1]*2;
		else if (onStar())
		{
			for (j=0; j<n; j++) flag[j]=0;
			setFlag(L);
			//求最小值
			res=0;
			for (j=0; j<n; j++)
			{
				if (flag[j]) res+=a[j];
				else res+=a[j]*2;
			}
		}
		else
		{
			for (j=0; j<n; j++) flag[j]=0;
			flag[x0-1]=1;
			setFlag(L-1);
			//求出一个
			res1=time+b[x0-1]-len;
			for (j=x0; j<n; j++)
			{
				if (flag[j]) res1+=a[j];
				else res1+=a[j]*2;
			}
			for (j=0; j<n; j++) flag[j]=0;
			setFlag(L);
			//求出另一个
			res2=0;
			for (j=0; j<n; j++)
			{
				if (flag[j]) res2+=a[j];
				else res2+=a[j]*2;
			}
			res=min(res1, res2);
		}
		fprintf(wFile, "Case #%d: %d\n", i, res);
		printf("Case #%d: %d\n", i, res);
	}
	fclose(rFile); e=ferror(rFile); assert(e==0);
	fclose(wFile); e=ferror(wFile); assert(e==0);
	system("pause");
}
