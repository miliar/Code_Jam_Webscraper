#include<iostream>
#include<string>
#include<fstream>
using namespace std;
int main()
{
	ifstream fin("B-small-attempt0.in");
	ofstream fout("B-small-attempt0.out");
	int T,C,D,N;
	string C1; string D1;
	fin>>T;
	char arr[10];
	for(int i=0;i<10;i++)
		arr[i]=' ';
	for(int i=0; i<T; i++)
	{
		fin>>C;
		if(C==1)
			fin>>C1;
		else C1="  ";
		fin>>D;
		if(D==1)
			fin>>D1;
		else D1="  ";
		fin>>N;
		int x=0; bool inc=false;
		fin>>arr[x]; x++;
		while(x<N)
		{
			fin>>arr[x];
			if(((arr[x-1]==C1[0])&&(arr[x]==C1[1]))||((arr[x-1]==C1[1])&&(arr[x]==C1[0])))
			{
				arr[x-1]=C1[2];
				arr[x]=' ';
				N--;
				inc=true;
			}
			else
			{
				for(int o=0;o<x;o++)
					if(((arr[x]==D1[0])&&(arr[o]==D1[1]))||((arr[x]==D1[1])&&(arr[o]==D1[0])))
					{
						for(int j=0;j<=x;j++)
							arr[j]=' ';
						N-=x+1;
						x=0;
						inc=true;
					}
			}
			if(!inc) x++;
			inc=false;
		}
			fout<<"Case #"<<i+1<<": [";
			for(int y=0;y<N;y++)
			{
				if(y!=0)
					fout<<", ";
				fout<<arr[y];
			}
			fout<<']'<<endl;
	}
	return 0;
}