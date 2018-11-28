#include<iostream>
#include<fstream>
#include<string>
using namespace std;

int Check_Comb(string str, string arr[], int size);

int main()
{
	int match=0;
	int L,D,N;
	string *arr;
	string *arr1;

	ifstream file;
	ofstream file1;

	file.open("A-large.in");
	file1.open("large.txt");

	file>>L>>D>>N;

	arr=new string[D];
	for(int i=0;i<D;i++)
	{
		file>>arr[i];
	}
	
	arr1=new string[N];
	for(int j=0;j<N;j++)
	{
		file>>arr1[j];
		file1<<"Case #"<<j+1<<": "<<Check_Comb(arr1[j],arr,D)<<endl;
	}
	
	return 0;
}

int Check_Comb(string str, string arr[], int size)
{
	int i,j;
	bool check=false;
	int match=0;
	int m=0;
	for(i=0;i<size;i++)
	{
		for(j=0;j<str.length();j++)
		{
			if(str[j]=='(')
			{
				while(str[j]!=')')
				{
					if(str[j]==arr[i][m])
					{
						check=true;
					}
					j++;
				}

				if(check!=true)
				{
					break;
				}
				
				m++;
				check=false;
			}
			else
			if(str[j]!=arr[i][m])
			{
				break;
			}
			else
			if(str[j]==arr[i][m])
			{
				m++;
			}
		}

		if(j>=str.length())
		{
			match++;
		}
		
		m=0;
		check=false;
	}

	return match;
}