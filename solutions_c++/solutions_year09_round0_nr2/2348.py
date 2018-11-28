

#include <stdio.h>
#include <fstream>
#include <iostream>
#include <stdlib.h>
#include <string>
#include <algorithm>
#include "stdafx.h"
using namespace std;


int minVal(int *arr,int svs)
{
	int min=-1;
	int idx=-1;
	for(int s=0;s<svs;s++)
	{
		if(min<0 || arr[s]<min) 
		{
			min=arr[s];
			idx=s;
		}
	}
	return idx;
}




int main()
{
	ifstream indata; // indata is like cin
	int numCases,wordLength,numWords; // variable for input value
ofstream myfile;
  myfile.open ("resultBig.txt");

	indata.open("B-large.in"); // opens the file
	
	if(!indata) { // file couldn't be opened
		printf("Error: file could not be opened\n");
		exit(1);
	}

	
	indata >> numCases;
	
		
	printf("%d\n",numCases);
	

	for(int c=0;c<numCases;c++)
	//for(int c=0;c<1;c++)
	{

		int H,W;
		
		indata>>H;
		indata>>W;
		int **nums=new int*[H];
		char **dir=new char*[H];
		char **plains=new char*[H];
		char curPlain='a';
		for(int x=0;x<H;x++) plains[x]=new char[W];
		for(int x=0;x<H;x++) dir[x]=new char[W];
		for(int x=0;x<H;x++) nums[x]=new int[W];
		printf("%d %d\n",H,W);
  
		for(int r=0;r<H;r++)
		{
			for(int c=0;c<W;c++)
			{
				indata>>nums[r][c];
				plains[r][c]='!';
				//printf("%d ",nums[r][c]);
			}
			//printf("\n");
		}
		//printf("\n");

		for(int r=0;r<H;r++)
		{
			for(int c=0;c<W;c++)
			{
				int vals[4];
				if(c+1<W) vals[0]=nums[r][c+1]; else vals[0]=100000; //			E c+1
				if(c-1>=0) vals[1]=nums[r][c-1]; else vals[1]=100000; //		W c-1
				if(r+1<H) vals[2]=nums[r+1][c]; else vals[2]=100000; //			S r+1
				if(r-1>=0) vals[3]=nums[r-1][c]; else vals[3]=100000; //		N r-1
				int dirc=minVal(vals,4);
				if(nums[r][c]<=vals[0] && nums[r][c]<=vals[1] && nums[r][c]<=vals[2] && nums[r][c]<=vals[3]) dir[r][c]='X';
				else
				{
					if(dirc==3) dir[r][c]='N';
					if(dirc==1)
					{
						if(r-1>=0 && nums[r][c-1]==nums[r-1][c]) dir[r][c]='N';
						else {dir[r][c]='W';}
					}
					if(dirc==0)
					{
						if(r-1>=0 && nums[r][c+1]==nums[r-1][c]) {dir[r][c]='N';}
						else if(c-1>=0 && nums[r][c+1]==nums[r][c-1]) {dir[r][c]='W';}
						else {dir[r][c]='E';}
					}
					if(dirc==2)
					{
						if(r-1>=0 && nums[r+1][c]==nums[r-1][c]) {dir[r][c]='N';}
						else if(c-1>=0 && nums[r+1][c]==nums[r][c-1]) {dir[r][c]='W';}
						else if(c+1<W && nums[r+1][c]==nums[r][c+1]) {dir[r][c]='E';}
						else {dir[r][c]='S';}
					}
				}
				//printf("%d ",nums[r][c]);
				//printf("%c ",dir[r][c]);
			}
			//printf("\n");
		}

		for(int r=0;r<H;r++)
		{
			for(int c=0;c<W;c++)
			{

				if(plains[r][c]=='!')
				{
					int *rows=new int[H*W];
					int *cols=new int[H*W];				
					int count=0;
					int curR=r;int curC=c;

					//char next=dir[r][c];
					while(1)
					{
						if(dir[curR][curC]=='X') break;
						if(plains[curR][curC]!='!') break;

						rows[count]=curR;
						cols[count]=curC;
						count++;
						if(dir[curR][curC]=='S')
						{
							curR++;
						}
						else if(dir[curR][curC]=='N')
						{
							curR--;
						}
						else if(dir[curR][curC]=='E')
						{
							curC++;
						}
						else if(dir[curR][curC]=='W')
						{
							curC--;
						}
					
					}
					if(dir[curR][curC]=='X')
					{
						if(plains[curR][curC]=='!')
						{
							plains[curR][curC]=curPlain;
							for(int x=0;x<count;x++)
								plains[rows[x]][cols[x]]=curPlain;
							curPlain+=1;
						}
						else
						{
							plains[curR][curC]=plains[curR][curC];
							for(int x=0;x<count;x++)
								plains[rows[x]][cols[x]]=plains[curR][curC];
							
						}
					}
					else
					{
						for(int x=0;x<count;x++)
							plains[rows[x]][cols[x]]=plains[curR][curC];
					}
				}
			}
		}
		
		printf("Case #%d:\n",c+1);
		myfile<<"Case #"<<c+1<<": "<<"\n";
		for(int r=0;r<H;r++)
		{
			for(int c=0;c<W;c++)
			{				
				printf("%c ",plains[r][c]);
				myfile<<plains[r][c]<<" ";
			}
			printf("\n");
			myfile<<"\n";
		}
		printf("\n");
	}
myfile.close();	
	return 0;
}
