#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <stdio.h>
#include <stdarg.h>
#include <stddef.h>
#include <math.h>
#include <stdlib.h>
#include <memory.h>
#include <conio.h>

using namespace std;

#define lint long long

#define ss stringstream
#define pb push_back
#define sz size()
#define FOR(i,n) for(i=0;i<n;i++)
#define SFOR(i,m,n) for(i=m;i<n;i++)
#define FORD(i,n) for(i=n-1;i>=0;i--)

int A[110][110],B[110][110],C[110][110];

bool check(int h,int w)
{
	int i,j;
	FOR(i,w) FOR(j,h) if (B[i][j]==-1) return true;
	return false;
}
void stok(int i,int j,int i2,int j2,int w,int h)
{
				int mn=A[i][j];
				if ((i>0)&&(A[i-1][j]<mn))		mn=A[i-1][j];
				if ((i<w-1)&&(A[i+1][j]<mn))	mn=A[i+1][j];
				if ((j>0)&&(A[i][j-1]<mn))		mn=A[i][j-1];
				if ((j<h-1)&&(A[i][j+1]<mn))	mn=A[i][j+1];
				
				
				if (mn==A[i2][j2]) {
					if ((j>0)&&(A[i][j-1]==mn))		{	if (j2==j-1) B[i][j]=0; else	return;}
					else if ((i>0)&&(A[i-1][j]==mn)){	if (i-1==i2) B[i][j]=0; else	return;}
					else if ((i<w-1)&&(A[i+1][j]==mn)){	if (i+1==i2) B[i][j]=0; else    return;}
					else if ((j<h-1)&&(A[i][j+1]==mn)){	if (j+1==j2) B[i][j]=0; else    return;}
				
				}

}
bool func1(int k,int w,int h)
{
	int i,j,l;
	FOR(l,h+w)
	FOR(j,h)
		FOR(i,w)
		
			if (B[i][j]==0)
			{
				int mn=A[i][j];
				B[i][j]=k;
				if ((i>0)&&(A[i-1][j]<mn))		mn=A[i-1][j];
				if ((i<w-1)&&(A[i+1][j]<mn))	mn=A[i+1][j];
				if ((j>0)&&(A[i][j-1]<mn))		mn=A[i][j-1];
				if ((j<h-1)&&(A[i][j+1]<mn))	mn=A[i][j+1];
				if (mn!=A[i][j]) {
					if ((j>0)&&(A[i][j-1]==mn))			{if (B[i][j-1]==-1)	B[i][j-1]=0;}
					else if ((i>0)&&(A[i-1][j]==mn))	{if (B[i-1][j]==-1)	B[i-1][j]=0;}
					else if ((i<w-1)&&(A[i+1][j]==mn))	{if (B[i+1][j]==-1)	B[i+1][j]=0;}
					else if ((j<h-1)&&(A[i][j+1]==mn))	{if (B[i][j+1]==-1)	B[i][j+1]=0;}
				}
				if ((i>0)&&(A[i-1][j]>A[i][j])&&(B[i-1][j]==-1))	stok(i-1,j,i,j,w,h);
				if ((i<w-1)&&(A[i+1][j]>A[i][j])&&(B[i+1][j]==-1))	stok(i+1,j,i,j,w,h);
				if ((j>0)&&(A[i][j-1]>A[i][j])&&(B[i][j-1]==-1))	stok(i,j-1,i,j,w,h);
				if ((j<h-1)&&(A[i][j+1]>A[i][j])&&(B[i][j+1]==-1))	stok(i,j+1,i,j,w,h);
				
				
			
			}
return true ;
}

int main()
{
	
	
	int i,j,k,l,n,h,w;
	FILE * f1 = fopen("B-large.in","r");
	FILE * f2 = fopen("B-large.out","w");
	fscanf(f1,"%d\n",&n);
	
	FOR(l,n)
	{
		int temp;
		fscanf(f1,"%d%d\n",&h,&w);
		memset(A,-1,sizeof(A));
		memset(B,-1,sizeof(B));
		FOR(j,h) FOR(i,w) {
			fscanf(f1,"%d",&temp);
			A[i][j]=temp;
		}
		int k=0;
		while (check(h,w)){
			FOR(j,h)
				FOR(i,w)
					if (B[i][j]==-1)
					{
						k++;
						B[i][j]=0; 
						bool a = func1(k,w,h);	
					}
		}
		
		fprintf(f2,"Case #%d:\n",l+1);
		FOR(j,h){
			FOR(i,w)
		
			fprintf(f2,"%c ",'a'+B[i][j]-1);
			fprintf(f2,"\n");
		}



		



	}
	fclose(f1);
	fclose(f2);

	return 0;
}
