/*
 * =====================================================================================
 *
 *       Filename:  welcome.cpp
 *
 *    Description:  timepass
 *
 *        Version:  1.0
 *        Created:  09/03/2009 09:53:14 PM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Bharath (IISc), ajeetbharath@gmail.com
 *        Company:  SilverOak Systems
 *
 * =====================================================================================
 */

#include<iostream>
#include<cstdio>
#include<cstring>

using namespace std;

typedef int INT;
typedef unsigned long ULONG;

const INT MAXLENGTH=500;

char searchstr[]="welcome to code jam";
int searchstrlen;

ULONG calculate(char* arr,INT length,INT index)
{
	INT i;
	ULONG downCount,totalCount=0;
	//cout<<"Index="<<index<<"Length="<<length<<endl;
	if(index == strlen(searchstr))
		return 1;
	for(i=0;i<(length-(searchstrlen-(index+1)));i++)
	{
		//cout<<"i="<<i<<",";
		if(arr[i]==searchstr[index])
		{
			downCount=calculate(arr+i+1,length-(i+1),index+1);
			totalCount+=downCount;
			totalCount=totalCount%10000;
			if(downCount==0)
				break;
		}
	}
	//cout<<endl;
	return totalCount;
}

int main()
{
	char array[MAXLENGTH+1];
	char str[100];
	INT i,no,readlen;
	cin>>no;
	//cout<<no<<endl;
	cin.get();
	searchstrlen=strlen(searchstr);
	for(i=1;i<=no;i++)
	{
		cin.getline(array,MAXLENGTH);
		//cout<<array<<endl;
		sprintf(str,"Case #%d: %04lu",i,calculate(array,strlen(array),0));
		cout<<str<<endl;
	}
	return 0;
}
