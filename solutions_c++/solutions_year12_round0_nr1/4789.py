// codejam1.cpp : main project file.

//#include "stdafx.h"
#include<iostream>
#include<stdio.h>
#include<cstring>
using namespace std;
//using namespace System;
char trans[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
int main()
{
	//freopen("a.txt","r",stdin);
	char arr[150];
	int tests;
	scanf("%d",&tests);
	cin.ignore();
	for(int l=1;l<=tests;l++)
	{
		
		gets(arr);
		int len=strlen(arr);
		int i,j,k;
		for(i=0;i<len;i++)
		{
			if(arr[i]==' ')
				continue;
			else
				arr[i]=trans[arr[i]-'a'];
		}
		//freopen("o.txt","w",stdout);
		printf("Case #%d: ",l);
		puts(arr);
		//printf("\n");

	}
    return 0;
}
