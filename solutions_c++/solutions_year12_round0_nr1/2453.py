// GoogleJam1.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <fstream>
#include <sstream>
using namespace std;
void main()
{
	char a[26],b[26];
	for(int i=0;i<26;i++)
		a[i]=97+i;
	char temp[1024],temp2[1024];
	fstream input,output;
	input.open("D://1.txt");
	input.getline(temp,1024);
	output.open("D://2.txt");
	output.getline(temp2,1024);
	int count=atoi(temp);
	while(count--)
	{
		input.getline(temp,1024);
		output.getline(temp2,1024);
		for(int i=0;i<strlen(temp);i++)
		{
			if(temp[i]==' ') continue;
			int j;
			for(j=0;j<28;j++)
			{
				if(temp[i]==a[j])
				break;
			}
			b[j]=temp2[i];
		}
	}
	b[16]='z';
	b[25]='q';
	fstream input1,output1;
	input1.open("D://3.txt");
	input1.getline(temp,1024);
	output1.open("D://4.txt");
	int count1=atoi(temp);
	int k=1;
	while(count1--)
	{
		output1<<"Case #"<<k++<<": ";
		char temp3[1024];
		input1.getline(temp3,1024);
		for(int i=0;i<strlen(temp3);i++)
		{
			if(temp3[i]==' ') 
			{
					output1<<" ";
					continue;
			}
			for(int j=0;j<26;j++)
			{
				if(temp3[i]==a[j])
				{
					output1<<b[j];
					break;
				}
			}
		}
		output1<<endl;
	}
}

