// Theme Park.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <vector>
#include <string>
#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <math.h>
#include <queue>
#include <stack>
using namespace std;


long long roller_coster2(queue <long long> q,int R,int k)
{
	long long sum=0,BigSum=0;
	int index;
	int counter=0;
	int flag=0;
	
	queue <long long> temp_queue;


	for (index=0; index< R; index++)
	{
		sum=0;
		flag=0;
		while ((sum< k && !flag) && !q.empty())
		{
			if( q.front()<= k- sum)
			{
				sum=sum+q.front();

				temp_queue.push(q.front());
				q.pop();

			}
			else 
				flag=1;
			
		}
		BigSum=BigSum+sum;
		sum=0;
		while(!temp_queue.empty())
		{
			q.push(temp_queue.front());
			temp_queue.pop();
		}
	}


return BigSum;

}
long long roller_coster(queue <long long> q,int R,int k)
{
	long long sum=0,BigSum=0;
	int index;
	int counter=0;
	cout<<"***************"<<q.size()<<"\n";
	queue <long long> temp_queue,temp2;
	vector< queue <long long> > v;
	v.push_back(q);
	for (index=0; index< R; index++)
	{
		sum=0;
		
		while (sum< k && !v.empty())
		{
			
			
			if (v.back().front()<=k-sum)
			{
			cout<<"prob1\n";
				sum=sum+v.back().front();
				
				temp2.push(v.back().front());
				
				v.back().pop();
			cout<<"prob1\n";	

			}
			else
			{
			temp_queue.push(v.back().front());
			cout<<"prob2\n";
			v.back().pop();
			cout<<"prob2\n";
			
			}
			if (v.back().empty())
			{ 
			v.pop_back();
			
			}
			
		}
		BigSum=BigSum+sum;
		cout<<"the sum is:  "<<sum<<"\n";
		counter++;
		sum=0;
		if (!v.empty())
			{
			while(!temp2.empty())
			{
				cout<<"prob3\n";
			

				v[0].push(temp2.front());
				cout<<"here?? ";
				temp2.pop();
				cout<<"prob3\n";
			}
			}
		else
			{
			v.push_back(temp2);
			while(!temp2.empty())
				temp2.pop();
			}
		if(!temp_queue.empty())
		v.push_back(temp_queue);
		while(!temp_queue.empty())
		{
			cout<<"prob4\n";
			temp_queue.pop();
			cout<<"prob4\n";	
		}
		if (v.back().empty())
				v.pop_back();
	}

	cout<<"%%%%%%%%%%%%%%%%%%"<<counter<<" %%%%%%%%%%%%\n";
return BigSum;

}

vector <long long> read_string2V(char input_str2[10000])
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

queue <long long> read_string2Q(char input_str2[10000])
{
	int j=0;
	queue <long long> v;
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
		v.push(temp);
		temp=0;
	}
	
	TempStr.clear(); 
	j++;
	}

return v;
}


void TP(string file_name)
{

string TempStr;
	int i,num_of_cases;
	long long temp;
vector <long long> v;
queue <long long> q;
ofstream output("sol.txt");
fstream input(file_name.c_str());

if (!input)
{
	cout<<" cannot open file"<<endl;
	cerr<<" misssssssssssssssssssssssssss";
	return;
}
char input_str2[10000];




input.getline(input_str2,10000);
num_of_cases=atoi(input_str2);
for (i=0; i<num_of_cases; i++)
{
	input.getline(input_str2,10000);
	v=read_string2V(input_str2);
	input.getline(input_str2,10000);
	q=read_string2Q(input_str2);
	cout<<"********************\n";
	cout<<v[0]<<"   "<<v[1]<<"\n";
	
	
	temp=roller_coster2(q,v[0],v[1]);
	output<<"Case #"<<i+1<<": "<<temp<<"\n";
	
	v.clear();

}

input.close();
output.close();
}


int _tmain(int argc, _TCHAR* argv[])
{
	TP("CS.txt");
	getchar();
	return 0;
}

