// Snapper Chain.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <vector>
#include <string>
#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <math.h>
using namespace std;

void comp(int k)
{
	long long c=2;
	int i;

	for (i=1; i<=k; i++)
	{
		c=c*2;
		cout<<c<<endl;
	}
}

vector <long long> read_string2(char input_str2[10000])
{
	int j=0;
	vector <long long> v;
	char TempChar[]="0";
	string TempStr;
	int length=strlen(input_str2);
	long long temp=0;
	int index;
	long long powL=1;
	while (j<length)
	{
	
	while(j<length && ((input_str2[j]>'0'-1) && (input_str2[j]<'9'+1) ) )
			{
				
				TempChar[0]=input_str2[j];
			TempStr.append(TempChar);
			
				j++;
			}
	if (!TempStr.empty())
	
	{
		for (index=0;index<TempStr.length(); index++)
		{
			temp=temp*10+(TempStr[index]-'0');
			
		}
		v.push_back(temp);
		temp=0;
	}
	
	TempStr.clear(); 
	j++;
	}

return v;
}



void snnaper(string file_name)
{

string TempStr;
	int i,j,num_of_cases;
	
vector<long long> v;	
ofstream output("large_sol.txt");
fstream input(file_name.c_str());

if (!input)
{
	cout<<" cannot open file"<<endl;
	cerr<<" misssssssssssssssssssssssssss";
	return;
}
char input_str2[10000];

long long p2=2;
//computing the table
long long Schain[31];
Schain[0]=0;
for(i=1; i<31; i++)
{
	Schain[i]=p2;
	p2=p2*2;
}




input.getline(input_str2,10000);
num_of_cases=atoi(input_str2);
for (i=0; i<num_of_cases; i++)
{
	input.getline(input_str2,10000);
	v=read_string2(input_str2);
	

	if ( (v[1] %Schain[v[0]])== (Schain[v[0]]-1))
		output<<"Case #"<<i+1<<": "<<"ON\n";
	else
		output<<"Case #"<<i+1<<": "<<"OFF\n";

	v.clear();
}

input.close();
output.close();
}

int _tmain(int argc, _TCHAR* argv[])
{
	snnaper("AL0.txt");
	
	getchar();
	return 0;
}

