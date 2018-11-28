// tri.cpp : Defines the entry point for the console application.
//

// stdafx.h : include file for standard system include files,
// or project specific include files that are used frequently, but
// are changed infrequently
//

#pragma once


#define WIN32_LEAN_AND_MEAN		// Exclude rarely-used stuff from Windows headers
#include <stdio.h>
#include <tchar.h>

#include <fstream>
#include <math.h>
#include <string.h>

using namespace std;

int n,t,na,nb;
int arrA[100],departA[100],arrB[100],departB[100];

void sort()
{
	for(int i=0;i<na;i++)
		for(int j=i;j<na;j++)
		{
			if(arrA[j]<arrA[i])
				swap(arrA[j],arrA[i]);		
		}

	for(int i=0;i<na;i++)
		for(int j=i;j<na;j++)
		{
			if(departA[j]<departA[i])
				swap(departA[j],departA[i]);		
		}

	for(int i=0;i<nb;i++)
		for(int j=i;j<nb;j++)
		{
			if(arrB[j]<arrB[i])
				swap(arrB[j],arrB[i]);		
		}

	for(int i=0;i<nb;i++)
		for(int j=i;j<nb;j++)
		{
			if(departB[j]<departB[i])
				swap(departB[j],departB[i]);		
		}

}
int IstrainatA(int hh, int mm ) 
{
	return 0;

}


int _tmain(int argc, _TCHAR* argv[])
{
	
	char temp[100];
	ifstream obj1("B-large.in");
	ofstream obj2("B-large.out");
	obj1.getline(temp,100);
	n = atoi(temp);		
	
	int count = 1;
	while(n--)
	{
		int ah,am,dh,dm;
		obj2<<"Case #"<<count++<<": ";
		obj1>>t>>na>>nb;
		obj1.getline(temp,100);
		for(int i=0;i<na;i++)
		{
			obj1.getline(temp,100);
			sscanf(temp,"%d:%d %d:%d",&dh,&dm,&ah,&am);//see it
			arrA[i] = am+ah*60;
			departA[i] = dm+dh*60;
		}
		for(int i=0;i<nb;i++)
		{
			obj1.getline(temp,100);
			sscanf(temp,"%d:%d %d:%d",&dh,&dm,&ah,&am);//see it
			arrB[i] = am+ah*60;
			departB[i] = dm+dh*60;
		}
		sort();
		int countA=na,countB=nb;


		for(int i=0;i<na;i++)
		{
			for(int j=0;j<nb;j++)
			{
				if( (arrB[j]+t)<=(departA[i])&&arrB[j]!=-1)
				{
					arrB[j]=-1;
					countA--;
					break;					
				}
			}				
		}
		for(int i=0;i<nb;i++)
		{
			for(int j=0;j<na;j++)
			{
				if( (arrA[j]+t)<=(departB[i])&&arrA[j]!=-1)
				{
					arrA[j]=-1;
					countB--;
					break;					
				}				
			}		
				
		}

		obj2<<countA<<" "<<countB<<"\n";

	}

	return 0;
}

