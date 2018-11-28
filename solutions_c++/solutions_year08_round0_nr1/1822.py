#include<iostream>
#include<string>
#include<fstream>
using namespace std;


	string Engines[150];
	string Queries[1100];
	int Cengine[200];
	int Ncase;
	int Nengine;
	int Nquery;
	

	
int isengine(string s)
{
	int ii;
	for(ii=0;ii<Nengine;ii++)
		if(Engines[ii]==s)return ii;
	return -1;
}


int countChoice()
{
	for(int jj=0;jj<Nengine;jj++)Cengine[jj]=0;
	int ss=0;
	int cho=0;
	int ocurengine=0;
	while(ss<Nquery)
	{
		int fla=isengine(Queries[ss]);
		if(-1==fla)
		{
			ss++;
		}
		else
		{
			if(0==Cengine[fla])
			{
				Cengine[fla]++;
				ocurengine++;
				if(ocurengine==Nengine)
				{
					cho++;
					for(int jj=0;jj<Nengine;jj++)Cengine[jj]=0;
					Cengine[fla]++;
					ocurengine=1;
					continue;
				}
				else ss++;
				
			}
			else ss++;
		}
	}
	return cho;
}
int main()
{
	ifstream fin;
	ofstream fout;
	fin.open("A.in");
	fout.open("A.out");
	
	
	fin>>Ncase;
	
	int i;
	
	int Choice=0;
	for(i=0;i<Ncase;i++)
	{
	
		fin>>Nengine;
		int j;
		string temp;
		getline(fin,temp);
		for(j=0;j<Nengine;j++)
		{
			getline(fin,Engines[j]);
		}

		fin>>Nquery;
		
		int k;
		getline(fin,temp);
		for(k=0;k<Nquery;k++)
		{
			getline(fin,Queries[k]) ;
		}
		
		Choice=countChoice();


		fout<<"Case #"<<(i+1)<<": "<<Choice<<endl;

	}
	fin.close();
	fout.close();

	return 0;
}

