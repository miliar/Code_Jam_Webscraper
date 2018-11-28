

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
	for(int s=0;s<svs;s++)
	{
		if(min<0 || arr[s]<min) min=arr[s];
	}
	return min;
}




int main()
{
	ifstream indata; // indata is like cin
	int numCases,wordLength,numWords; // variable for input value
ofstream myfile;
  myfile.open ("resultBig.txt");

	indata.open("A-large.in"); // opens the file
	
	if(!indata) { // file couldn't be opened
		printf("Error: file could not be opened\n");
		exit(1);
	}

	indata >> wordLength;
	indata >> numWords;
	indata >> numCases;
	int *matches=new int[numWords];
	for(int i=0;i<numWords;i++) matches[i]=0;
	int *wordPtrs=new int[numWords];
	for(int i=0;i<numWords;i++) wordPtrs[i]=0;
	char **words=new char*[numWords];
		
	printf("%d %d %d\n",wordLength,numWords,numCases);
	
	for(int i=0;i<numWords;i++)
	{
		words[i]=new char[1000];
		indata>>words[i];
		printf("%s\n",words[i]);
	}

	for(int c=0;c<numCases;c++)
	{
		char str2[1000];		
		indata>>str2;
		//printf("%s\n",str2);
		int len=strlen(str2);
		int ptr=0;
		for(int i=0;i<numWords;i++) matches[i]=0;
		for(int i=0;i<numWords;i++) wordPtrs[i]=0;
		while(1)
		{
			if(str2[ptr]=='(')
			{
				ptr++;
				while(str2[ptr]!=')')
				{
					for(int i=0;i<numWords;i++)
					{
						if(str2[ptr]==words[i][wordPtrs[i]]) matches[i]++;
					}
					ptr++;					
				}
				ptr++;
				for(int i=0;i<numWords;i++) wordPtrs[i]++;
			}
			else
			{
				for(int i=0;i<numWords;i++)
				{
					if(str2[ptr]==words[i][wordPtrs[i]]) matches[i]++;
				}
				ptr++;
				for(int i=0;i<numWords;i++) wordPtrs[i]++;
			}
			if(ptr>=strlen(str2))break;
		}

  
  

		int count=0;
		for(int i=0;i<numWords;i++)
		{
			//printf("i=%d matches=%d\n",i,matches[i]);
			if(matches[i]==wordLength) count++;
		}
		printf("Case #%d: %d\n",c+1,count);
		myfile<<"Case #"<<c+1<<": "<<count<<"\n";
	}
myfile.close();	
	return 0;
}
