#include<string>
#include<iostream>
#include<fstream>
#include<cstring>
#include"string.h"
using namespace std;

int main()
{
	string *arr1;
	string *arr2;

	int totalcases;
	int seng;
	int queries;
	int temp=0;
	int temp1=0;
	int temp2=0;
	int switches=0;
	string current;
	string tempseng;

	int check=0;

	ifstream file;
	ofstream file1;
	file.open("A-large.in");
	file1.open("output.txt");



	file>>totalcases;
	for(int i=0;i<totalcases;i++)
	{
		file>>seng;
		arr1=new string[seng];
		getline(file,arr1[0]);
		for(int j=0;j<seng;j++)
		{
			getline(file,arr1[j]);
			//file>>arr1[j];
		}

		file>>queries;
		if(queries!=0)
		{
			arr2=new string[queries];
			getline(file,arr2[0]);
			for(int k=0;k<queries;k++)
			{
				getline(file,arr2[k]);
				//file>>arr2[k];
			}

			while(temp2<queries)
			{
				for(int m=0;m<seng;m++)
				{
					temp=0;
					current=arr1[m];

					for(int l=temp2;l<queries;l++)
					{
						if(current.compare(arr2[l])!=0)
						{
							temp++;
						}
						else
						{
							break;
						}
					}

					if(temp>temp1)
					{
						temp1=temp;
					}

				}

				temp2+=temp1;
				temp1=0;

				if(temp2<queries && temp2!=0)
				{
					switches++;
				}

			}

			temp2=0;

			file1<<"Case #"<<i+1<<": "<<switches<<endl;
			
		}
		else
		{
			file1<<"Case #"<<i+1<<": 0"<<endl;
		}

		switches=0;
	}

	return 0;
}