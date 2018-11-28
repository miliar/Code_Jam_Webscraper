#include<string.h>
#include<iostream.h>
#include<fstream.h>
#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
#define SMAX 100
#define QMAX 1000


int ntest;
char Sl[SMAX][100];
int Ql[QMAX];
int q,s;
int n;
int state[QMAX][SMAX];

int Lookup(char temp[])
	{
   	for(int i=0; i<s; i++)
          if(strcmp(temp,Sl[i]) == 0)
          	return (i+1);

   	return -1;
   }

void Print()
	{	
	/*for(int i=0; i<q; i++)
      	{
         	cout<<Ql[i]<<endl;
         }*/
	int i,j;
	for(i=0; i<q; i++)
	{
		for(j=0; j<s; j++)
		{
			cout<<state[i][j]<<" ";
		}
		cout<<endl;

   }
}

void Make()
{
	int i,j;
	for(i=0; i<q; i++)
	{
		for(j=0; j<s; j++)
		{
			if(j==Ql[i]-1)
				state[i][j] = 0;
			else
				state[i][j] = 1;

		}
	}
	//Print();
}

int Least(int start)
{
	int i,j;
	int leastcol = 0;
	int count = start;
	for(i=0; i<s; i++)
	{
		j=start;
		while(state[j][i]==1&&j<q)
		{
			j++;
		}
		if(j==q)
			return 0;
		if(j > count)
		{
			count = j;
			leastcol = i;
		}
	}
	return (1+Least(count));

}

void Readfile()
{
 FILE* in;
 char temp[100];
 in = fopen("F:\\A-large.in","r");
 fgets(temp,100,in);
 n = atoi(temp);
 FILE* out;
 out = fopen("F:\\A-large.out","w");
 //For each test case
 for(int i=0; i<n; i++)
 	{
		cout<<endl;	 
	 fgets(temp,100,in);
			s = atoi(temp);
      //Read the search engine names
      for(int k=0; k<s; k++)
	  {

		   fgets(Sl[k],100,in);
	  }
       fgets(temp,100,in);
		q = atoi(temp);
      //Read the query list
      for(int j=0; j<q; j++)
      	{
             fgets(temp,100,in);
         	 Ql[j] = Lookup(temp);
         }
   	  
	  //Call the function which makes the thingo
		Make();
		fprintf(out,"Case #%d: %d\n",(i+1),(Least(0)));
	  //Print();
   }
}

void main()
{
	
	FILE* in;
	in = fopen("F:\\A-large.in","a");
	fputs("\n",in);
	fclose(in);

	Readfile();
}