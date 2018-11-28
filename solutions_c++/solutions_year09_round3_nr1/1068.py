// google.cpp : Defines the entry point for the console application.
//
#include "stdafx.h"
#include<fstream.h>
#include<string.h>
#include<math.h>
#include<stdio.h>

using namespace std;

void sort(char d[], int start, int end)
{
	 for(int i=start; i<end; i++)
	 { for(int j=start; j< end-1; j++)
		{ if(d[j]>d[j+1])
		  { char temp = d[j];
			 d[j]= d[j+1];
			 d[j+1] = temp;
		  }
		}
	 }
}

int findDistinct(char str[], int len)
{ int count=0,i,j;
  for(i=0; i<len; i++)
  {  char c= str[i];
	  for(j=0; j<i; j++)
	  {	 if(str[j]==c)
			break;
	  }
	  if(j==i)
		count++;
  }
  return count;
}

unsigned long long evaluate(char str[], int len)
{
	int n= findDistinct(str,len);
	int i,j;

	char **rep = new char*[n];
	for(i=0; i<n; i++)
		rep[i] = new char[2];

	rep[0][0]=str[0];
	rep[0][1]=1;

	int index=1;
	int repindex=2;
	unsigned long long tot=0;
	if(n==1)
	{
		for(i=0; i<len; i++)
	{
		tot+= pow(float(2),i);
	}
		return tot;
	}

	while(str[index]==str[index-1])
	{ index++;
	}
	rep[1][0]=str[index];
	rep[1][1]=0;

	index++;
	
	while(str[index]!='\0')
	{  int flag=1;

		for(j=0; j<repindex; j++)
		{ if(rep[j][0]==str[index])
		  {  flag=0;
				break;
		  }
		}
		 if(flag)
		{ rep[repindex][0] = str[index];
		  rep[repindex][1] = repindex;
		  repindex++;
		}
		index++;
	}
jump1:
	for(i=0; i<len; i++)
	{ char ch = str[i];
	  for(int g=0; g<n; g++)
		 if(rep[g][0]==ch)
		  {	str[i]=rep[g][1];
				break;
		  }
	}

	

	
	for(i=0; i<len; i++)
	{
		tot+= str[len-i-1]*pow(double(n),i);
	}

	for(i=0; i<n; i++)
	  delete rep[i];
	delete rep;

	return tot;
}

void main()
{
	int T;
	char N[62];
	ifstream fin("C:\\Users\\Sau\\Desktop\\codejam\\A3.in");
	ofstream fout("C:\\Users\\Sau\\Desktop\\codejam\\out.txt");
	
	fin>>T;
	unsigned long long sec;

	for(int i=0; i<T; i++)
	{
		fin>>N;
		int len = strlen(N);

		sec = evaluate(N,len);
		fout<<"Case #"<<(i+1)<<": "<<sec<<"\n";
	}

	fin.close();
	fout.close();
}