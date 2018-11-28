// GjamCpp.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdio.h>
#include <conio.h>
#include <string>
#include <iostream>

int main()
{
	int i,j,k;
	//printf("Hello world!\n");

	int Number_of_TestCases=0;
	int l=1;
	scanf("%d",&Number_of_TestCases);
	int R=0;
	int C=0;
	
	char** Matrix;
	while(l<=Number_of_TestCases)
	{
		scanf("%d %d",&R,&C);
		Matrix = new char*[R+1];
		for(int i=0;i<R;i++)
			Matrix[i] = new char[C+1];

		for(int j=0;j<R;j++)
			scanf("%s", Matrix[j]);

		for(int i=0;i<R;i++)
			for(int j=0;j<C;j++)
			{
				if((Matrix[i][j] == '#')&&(j+1 < C) && (Matrix[i][j+1] == '#') && (i+1 < R) && (Matrix[i+1][j] == '#') && ((i+1 < R) && (j+1 < C)) && (Matrix[i+1][j+1] == '#') )
				{
					Matrix[i][j] = '/';
					Matrix[i][j+1] = '\\';
					Matrix[i+1][j] = '\\';
					Matrix[i+1][j+1] = '/';
				}
			}

			bool Isimpossible = false;
		for(int i=0;i<R;i++)
		{
			for(int j=0;j<C;j++)
			{
				if(Matrix[i][j] == '#')
				{
					Isimpossible = true; break;
				}

			}
			if(Isimpossible == true) break;

		}
		
		
		printf("Case #%d:\n",l);
		if(Isimpossible == true) printf("Impossible\n");
		else
		{
			for(int i=0;i<R;i++)
			{
				
				for(int j=0;j<C;j++)
					printf("%c",Matrix[i][j]);
				printf("\n");
			}
		}

		for(int i=0;i<R;i++)
			delete Matrix[i];
		delete Matrix;


		l++;
	}
	return 0;
}
