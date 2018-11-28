// GoogleCode2.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

int **A,**B;
int H,W;
int newID;
int rekurzio(int,int);
int _tmain(int argc, _TCHAR* argv[])
{
	int T,t,i,j;
	FILE *f,*g;
	fopen_s(&f,"B-large.in","r");
	fopen_s(&g,"B-large.out","w");
	fscanf(f,"%d",&T);
	for (t=0; t<T; ++t) {
		fscanf(f,"%d %d",&H,&W);
		A=new int*[H];
		B=new int*[H];
		for (i=0; i<H; ++i) {
			A[i]=new int[W];
			B[i]=new int[W];
		}
		for (i=0; i<H; ++i)
			for (j=0; j<W; ++j) {
				fscanf(f,"%d",&A[i][j]);
				B[i][j]=-1;
			}
		newID=1;
		for (i=0; i<H; ++i)
			for (j=0; j<W; ++j)
				if (B[i][j]==-1)
					B[i][j]=rekurzio(i,j);
		fprintf(g,"Case #%d:\n",t+1);
		for (i=0; i<H; ++i) {
			for (j=0; j<W; ++j)
				fprintf(g,"%c ",B[i][j]+96);
			fprintf(g,"\n");
		}
	}
	fclose(f);
	fclose(g);
	return 0;
}
int rekurzio(int i, int j) {
	int dir,minv;
	dir=-1;
	minv=A[i][j];
	if (B[i][j]!=-1)
		return B[i][j];
	if (i-1>=0)
		if (A[i-1][j]<minv) {
			minv=A[i-1][j];
			dir=1;
		}
	if (j-1>=0)
		if (A[i][j-1]<minv) {
			minv=A[i][j-1];
			dir=2;
		}
	if (j+1<W)
		if (A[i][j+1]<minv) {
			minv=A[i][j+1];
			dir=3;
		}
	if (i+1<H)
		if (A[i+1][j]<minv) {
			minv=A[i+1][j];
			dir=4;
		}
	if (dir==-1) {
		B[i][j]=newID;
		newID++;
	}
	else if (dir==1) 
		B[i][j]=rekurzio(i-1,j);
	else if (dir==2)
		B[i][j]=rekurzio(i,j-1);
	else if (dir==3)
		B[i][j]=rekurzio(i,j+1);
	else if (dir==4)
		B[i][j]=rekurzio(i+1,j);
	return B[i][j];
}
